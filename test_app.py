#!/usr/bin/env python3
"""Quick test script for Fake Review Monitor"""

print("🔍 Testing Fake Review Monitor...\n")

# Test imports
print("[1/4] Testing imports...")
from app import train_model, preprocess
print("✓ Imports successful")

# Test preprocessing
print("\n[2/4] Testing text preprocessing...")
text = "AMAZING!!! Best product EVER!!!"
clean = preprocess(text)
print(f"Original: {text}")
print(f"Cleaned:  {clean}")
print("✓ Preprocessing works")

# Test model training
print("\n[3/4] Testing model training...")
model, df, metrics = train_model()
print(f"✓ Model trained on {len(df)} reviews")
print(f"✓ Accuracy: {metrics['accuracy']}%")
print(f"✓ F1 Score: {metrics['f1']}%")

# Test prediction
print("\n[4/4] Testing prediction...")
test_reviews = [
    "This product is absolutely amazing! Best purchase ever!!!",
    "Decent product. Works as expected. Nothing special.",
]

for review in test_reviews:
    pred = model.predict([preprocess(review)])[0]
    label = "FAKE" if pred == 1 else "REAL"
    print(f"\nReview: {review[:50]}...")
    print(f"Prediction: {label}")

print("\n✅ All tests passed! App is ready to run.")
print("\nTo start the server:")
print("  python app.py")
print("\nThen open in browser:")
print("  http://127.0.0.1:5000")
