# 🔍 Fake Review Monitor

An intelligent web application that detects fake product reviews using Machine Learning (KNN + TF-IDF). Built with Flask, scikit-learn, and modern web technologies.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Problem Statement

In today's e-commerce platforms, fake reviews mislead customers and affect product credibility. Many sellers post manipulated or spam reviews to increase ratings. This system automatically detects such fake reviews using Machine Learning.

## ✨ Features

- 🤖 **ML-Powered Classification** - KNN algorithm with TF-IDF vectorization
- 📊 **Interactive Dashboard** - Real-time visualizations and metrics
- 🎨 **Modern UI** - Dark theme with smooth animations
- 📈 **Performance Metrics** - Accuracy, Precision, Recall, F1 Score
- 🚨 **Red Flag Detection** - Identifies suspicious patterns in reviews
- 💡 **Sample Reviews** - Pre-loaded examples to test the system
- 📉 **Data Visualizations** - Charts showing distribution and model performance

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Anshuljain1235/Fake_Review_Monitor.git
cd Fake_Review_Monitor
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open your browser**
```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
Fake_Review_Monitor/
├── app.py                 # Flask backend with ML pipeline
├── fake_reviews.csv       # Training dataset (95 reviews)
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css         # Modern dark theme styling
├── templates/
│   └── index.html        # Main dashboard interface
└── README.md             # Project documentation
```

## 🧠 How It Works

### 1. Data Preprocessing
- Text cleaning (lowercase, remove special characters)
- Tokenization and normalization
- TF-IDF vectorization with bigrams

### 2. Model Training
- **Algorithm**: K-Nearest Neighbors (KNN)
- **Distance Metric**: Cosine similarity
- **Features**: TF-IDF vectors (max 5000 features)
- **Train/Test Split**: 75/25 with stratification

### 3. Classification
- Predicts review as **Real** or **Fake**
- Provides confidence scores
- Detects red flags:
  - Compensation mentions
  - Excessive exclamation marks
  - Hyperbolic language
  - Promotional calls-to-action

### 4. Evaluation Metrics
- **Accuracy**: ~88%
- **Precision**: ~87%
- **Recall**: ~87%
- **F1 Score**: ~87%

## 📊 Features Breakdown

### Dashboard Components

1. **Dataset Overview**
   - Total reviews count
   - Fake vs Real distribution
   - Model accuracy and F1 score

2. **Review Classifier**
   - Text input for custom reviews
   - Real-time prediction with confidence
   - Probability bars for both classes
   - Red flag detection

3. **Sample Reviews**
   - Pre-loaded examples (fake and real)
   - One-click testing

4. **Data Visualizations**
   - Fake vs Real distribution (bar chart)
   - Review composition (pie chart)
   - Rating distribution by label
   - Confusion matrix
   - Performance metrics comparison

5. **Model Performance**
   - Accuracy, Precision, Recall, F1 Score
   - Visual metrics comparison

## 🎨 UI Features

- **Dark Theme** - Easy on the eyes
- **Responsive Design** - Works on all devices
- **Smooth Animations** - Polished user experience
- **Interactive Charts** - Matplotlib/Seaborn visualizations
- **Loading States** - Visual feedback during processing

## 🔧 Technologies Used

| Category | Technology |
|----------|-----------|
| **Backend** | Flask 3.0+ |
| **ML Framework** | scikit-learn 1.5+ |
| **Data Processing** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Fonts** | Google Fonts (Inter) |

## 📈 Model Performance

The KNN classifier achieves:
- ✅ **88% Accuracy** on test set
- ✅ **87% Precision** (low false positives)
- ✅ **87% Recall** (catches most fake reviews)
- ✅ **87% F1 Score** (balanced performance)

## 🚀 Future Enhancements

- [ ] Real-time review scraping from e-commerce sites
- [ ] Upload custom dataset feature
- [ ] Advanced NLP models (LSTM, BERT, Transformers)
- [ ] User authentication system
- [ ] Review history and analytics
- [ ] API endpoints for integration
- [ ] Cloud deployment (AWS, Heroku, Vercel)
- [ ] Multi-language support
- [ ] Batch review analysis
- [ ] Export reports (PDF, CSV)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Anshul Jain**

- GitHub: [@Anshuljain1235](https://github.com/Anshuljain1235)
- Repository: [Fake_Review_Monitor](https://github.com/Anshuljain1235/Fake_Review_Monitor)

## 🙏 Acknowledgments

- Dataset inspired by common e-commerce review patterns
- Built with Flask and scikit-learn
- UI design inspired by modern dark themes

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

⭐ **Star this repository if you find it helpful!**
