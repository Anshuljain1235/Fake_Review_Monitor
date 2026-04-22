# 📖 Usage Guide

## Running the Application

### Step 1: Start the Server
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 2: Open in Browser
Navigate to: `http://127.0.0.1:5000`

## Using the Dashboard

### 1️⃣ View Statistics
The top section shows:
- Total reviews in dataset
- Number of fake reviews detected
- Number of real reviews
- Model accuracy and F1 score

### 2️⃣ Classify a Review

**Option A: Type Your Own**
1. Scroll to "Classify a Review" section
2. Type or paste a product review
3. Click "🔍 Analyze Review"
4. View results with confidence scores

**Option B: Use Sample Reviews**
1. Scroll to "Try Sample Reviews"
2. Click any sample card
3. Automatically analyzes and shows results

### 3️⃣ Understanding Results

**Fake Review Indicators:**
- 🚨 Red background
- High fake probability (>50%)
- Red flags detected:
  - Mentions compensation
  - Excessive exclamation marks
  - Hyperbolic language
  - Promotional calls-to-action

**Real Review Indicators:**
- ✅ Green background
- High real probability (>50%)
- Balanced, authentic language
- Specific details without hype

### 4️⃣ Explore Visualizations
Scroll down to see:
- **Fake vs Real Distribution** - Bar chart
- **Review Composition** - Pie chart
- **Rating Distribution** - Grouped bar chart
- **Confusion Matrix** - Model performance
- **Metrics Comparison** - Accuracy, Precision, Recall, F1

## API Endpoints

### Predict Review
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"review": "This product is amazing!!!"}'
```

**Response:**
```json
{
  "label": "fake",
  "confidence": 85.3,
  "fake_pct": 85.3,
  "real_pct": 14.7,
  "flags": ["Excessive exclamation marks"],
  "review": "This product is amazing!!!"
}
```

### Get Statistics
```bash
curl http://127.0.0.1:5000/api/stats
```

**Response:**
```json
{
  "total": 95,
  "fake": 50,
  "real": 45,
  "accuracy": 88.0,
  "precision": 87.5,
  "recall": 87.0,
  "f1": 87.0
}
```

## Keyboard Shortcuts

- **Ctrl + Enter** in textarea → Analyze review
- **Click sample card** → Auto-fill and analyze

## Tips for Best Results

✅ **DO:**
- Use complete sentences
- Include product-specific details
- Test various review styles
- Compare fake vs real samples

❌ **DON'T:**
- Submit empty reviews
- Use only emojis
- Submit extremely short text (<5 words)

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or use different port
flask run --port 5001
```

### Module Not Found
```bash
pip install -r requirements.txt
```

### Charts Not Loading
- Check matplotlib backend
- Ensure seaborn is installed
- Clear browser cache

## Performance Notes

- **Model loads on startup** (~2-3 seconds)
- **Prediction time** <100ms per review
- **Chart generation** cached on page load
- **Dataset size** 95 reviews (expandable)

## Customization

### Add More Reviews
Edit `fake_reviews.csv`:
```csv
review_text,label,rating
"Your review here",fake,5
```

Then restart the app to retrain.

### Adjust Model Parameters
In `app.py`, modify:
```python
KNeighborsClassifier(n_neighbors=5, metric='cosine')
# Try: n_neighbors=3, 7, 10
```

### Change Theme Colors
Edit `static/style.css`:
```css
:root {
  --accent: #7c3aed;  /* Change primary color */
  --bg: #0f0f1a;      /* Change background */
}
```

## Next Steps

1. ⭐ Star the repository
2. 🐛 Report issues on GitHub
3. 🚀 Deploy to cloud (Heroku, Render, Vercel)
4. 🔧 Customize for your use case
5. 📊 Add more training data

---

**Need help?** Open an issue: https://github.com/Anshuljain1235/Fake_Review_Monitor/issues
