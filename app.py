import os
import io
import base64
import re
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)
from sklearn.pipeline import Pipeline

# ── App setup ────────────────────────────────────────────────────────────────
app = Flask(__name__)
DATASET_PATH = "fake_reviews.csv"

# ── Text preprocessing ────────────────────────────────────────────────────────
def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# ── Train model ───────────────────────────────────────────────────────────────
def train_model():
    df = pd.read_csv(DATASET_PATH)
    df.dropna(subset=["review_text", "label"], inplace=True)
    df["clean_text"] = df["review_text"].apply(preprocess)

    X = df["clean_text"]
    y = df["label"].map({"real": 0, "fake": 1})

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=5000, stop_words="english")),
        ("knn",   KNeighborsClassifier(n_neighbors=5, metric="cosine")),
    ])
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    metrics = {
        "accuracy":  round(accuracy_score(y_test, y_pred) * 100, 2),
        "precision": round(precision_score(y_test, y_pred, zero_division=0) * 100, 2),
        "recall":    round(recall_score(y_test, y_pred, zero_division=0) * 100, 2),
        "f1":        round(f1_score(y_test, y_pred, zero_division=0) * 100, 2),
        "cm":        confusion_matrix(y_test, y_pred).tolist(),
        "report":    classification_report(y_test, y_pred, target_names=["Real", "Fake"]),
    }

    return pipeline, df, metrics

# ── Chart helpers ─────────────────────────────────────────────────────────────
PALETTE = {"real": "#4CAF50", "fake": "#F44336"}

def fig_to_b64(fig) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=130, transparent=True)
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)
    return encoded

def chart_label_dist(df):
    counts = df["label"].value_counts()
    fig, ax = plt.subplots(figsize=(5, 4))
    bars = ax.bar(counts.index, counts.values,
                  color=[PALETTE.get(l, "#888") for l in counts.index],
                  edgecolor="white", linewidth=1.5, width=0.5)
    for bar, val in zip(bars, counts.values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                str(val), ha="center", va="bottom", fontsize=12, fontweight="bold", color="white")
    ax.set_title("Fake vs Real Reviews", fontsize=14, color="white", pad=12)
    ax.set_xlabel("Label", color="#ccc")
    ax.set_ylabel("Count", color="#ccc")
    ax.tick_params(colors="white")
    ax.set_facecolor("#1e1e2e")
    fig.patch.set_facecolor("#1e1e2e")
    for spine in ax.spines.values():
        spine.set_edgecolor("#444")
    return fig_to_b64(fig)

def chart_rating_dist(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    for label, grp in df.groupby("label"):
        grp["rating"].value_counts().sort_index().plot(
            kind="bar", ax=ax, alpha=0.8,
            color=PALETTE.get(label, "#888"),
            label=label.capitalize(), width=0.35,
            position=0 if label == "real" else 1
        )
    ax.set_title("Rating Distribution by Label", fontsize=14, color="white", pad=12)
    ax.set_xlabel("Rating", color="#ccc")
    ax.set_ylabel("Count", color="#ccc")
    ax.tick_params(colors="white")
    ax.legend(facecolor="#2a2a3e", labelcolor="white", edgecolor="#555")
    ax.set_facecolor("#1e1e2e")
    fig.patch.set_facecolor("#1e1e2e")
    for spine in ax.spines.values():
        spine.set_edgecolor("#444")
    return fig_to_b64(fig)

def chart_confusion(cm):
    fig, ax = plt.subplots(figsize=(4.5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="RdYlGn",
                xticklabels=["Real", "Fake"],
                yticklabels=["Real", "Fake"],
                linewidths=0.5, linecolor="#333",
                ax=ax, cbar=False,
                annot_kws={"size": 16, "weight": "bold"})
    ax.set_title("Confusion Matrix", fontsize=14, color="white", pad=12)
    ax.set_xlabel("Predicted", color="#ccc")
    ax.set_ylabel("Actual", color="#ccc")
    ax.tick_params(colors="white")
    ax.set_facecolor("#1e1e2e")
    fig.patch.set_facecolor("#1e1e2e")
    return fig_to_b64(fig)

def chart_metrics_bar(metrics):
    labels = ["Accuracy", "Precision", "Recall", "F1 Score"]
    values = [metrics["accuracy"], metrics["precision"], metrics["recall"], metrics["f1"]]
    colors = ["#7c3aed", "#2563eb", "#059669", "#d97706"]
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.barh(labels, values, color=colors, edgecolor="white", linewidth=0.8, height=0.5)
    for bar, val in zip(bars, values):
        ax.text(val + 0.5, bar.get_y() + bar.get_height() / 2,
                f"{val}%", va="center", fontsize=11, fontweight="bold", color="white")
    ax.set_xlim(0, 115)
    ax.set_title("Model Performance Metrics", fontsize=14, color="white", pad=12)
    ax.set_xlabel("Score (%)", color="#ccc")
    ax.tick_params(colors="white")
    ax.set_facecolor("#1e1e2e")
    fig.patch.set_facecolor("#1e1e2e")
    for spine in ax.spines.values():
        spine.set_edgecolor("#444")
    return fig_to_b64(fig)

def chart_pie(df):
    counts = df["label"].value_counts()
    fig, ax = plt.subplots(figsize=(4.5, 4))
    wedges, texts, autotexts = ax.pie(
        counts.values,
        labels=[l.capitalize() for l in counts.index],
        autopct="%1.1f%%",
        colors=[PALETTE.get(l, "#888") for l in counts.index],
        startangle=140,
        wedgeprops=dict(edgecolor="white", linewidth=1.5),
        textprops=dict(color="white", fontsize=12)
    )
    for at in autotexts:
        at.set_fontsize(11)
        at.set_fontweight("bold")
    ax.set_title("Review Composition", fontsize=14, color="white", pad=12)
    fig.patch.set_facecolor("#1e1e2e")
    return fig_to_b64(fig)

# ── Bootstrap model on startup ────────────────────────────────────────────────
MODEL, DF, METRICS = train_model()

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    charts = {
        "label_dist":   chart_label_dist(DF),
        "rating_dist":  chart_rating_dist(DF),
        "confusion":    chart_confusion(METRICS["cm"]),
        "metrics_bar":  chart_metrics_bar(METRICS),
        "pie":          chart_pie(DF),
    }
    stats = {
        "total":    len(DF),
        "fake":     int((DF["label"] == "fake").sum()),
        "real":     int((DF["label"] == "real").sum()),
        "accuracy": METRICS["accuracy"],
        "f1":       METRICS["f1"],
    }
    return render_template("index.html", charts=charts, metrics=METRICS, stats=stats)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    review_text = data.get("review", "").strip()

    if not review_text:
        return jsonify({"error": "No review text provided."}), 400

    clean = preprocess(review_text)
    pred  = MODEL.predict([clean])[0]
    proba = MODEL.predict_proba([clean])[0]

    label      = "fake" if pred == 1 else "real"
    confidence = round(float(max(proba)) * 100, 1)
    fake_pct   = round(float(proba[1]) * 100, 1)
    real_pct   = round(float(proba[0]) * 100, 1)

    # Simple red-flag keywords
    flags = []
    lower = review_text.lower()
    if re.search(r"\b(paid|compensated|free|gift card|discount)\b.*review", lower):
        flags.append("Mentions compensation for review")
    if re.search(r"(!!!|!!!)", review_text):
        flags.append("Excessive exclamation marks")
    if re.search(r"\b(miracle|cure|life.?changing|best ever|greatest)\b", lower):
        flags.append("Hyperbolic language detected")
    if re.search(r"\b(buy now|must buy|everyone needs)\b", lower):
        flags.append("Promotional call-to-action language")
    if len(review_text.split()) < 5:
        flags.append("Very short review")

    return jsonify({
        "label":      label,
        "confidence": confidence,
        "fake_pct":   fake_pct,
        "real_pct":   real_pct,
        "flags":      flags,
        "review":     review_text,
    })


@app.route("/api/stats")
def api_stats():
    return jsonify({
        "total":     len(DF),
        "fake":      int((DF["label"] == "fake").sum()),
        "real":      int((DF["label"] == "real").sum()),
        "accuracy":  METRICS["accuracy"],
        "precision": METRICS["precision"],
        "recall":    METRICS["recall"],
        "f1":        METRICS["f1"],
    })


if __name__ == "__main__":
    app.run(debug=True)
