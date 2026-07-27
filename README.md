# 🧠 AI-Powered Fake News Detection System

An intelligent fake news detection platform that combines **Deep Learning (DistilBERT)** with **real-time external verification** to assess the credibility of news articles.

Instead of relying only on AI predictions, the system integrates multiple evidence sources including:

- 🤖 Fine-tuned DistilBERT Transformer
- 📰 GNews API
- ✅ Google Fact Check API
- 🧠 Semantic Similarity Matching
- 📊 Trust Score Calculation
- 📄 PDF Report Generation
- 🎨 Interactive Glassmorphism Dashboard

The application analyzes a news article, predicts whether it resembles **Real** or **Fake** news, searches for supporting news coverage, checks professional fact-check databases, computes a credibility score, and generates a detailed AI report.

---

## 🚀 Features

### 🤖 AI-Based News Classification
- Fine-tuned DistilBERT Transformer
- Binary Fake vs Real News Classification
- Confidence Score Prediction
- Probability Distribution Visualization

### 🌐 Real-Time Verification
- Google Fact Check API Integration
- GNews API Integration
- Semantic Fact-Check Matching using Sentence Transformers
- Related News Discovery

### 📊 Credibility Analysis
- Trust Score Calculation
- Reliability Breakdown Dashboard
- Authenticity Indicators
- AI Reasoning Summary
- Overall Reliability Recommendation

### 📈 Interactive Analytics
- Confidence Meter
- Probability Charts
- Reading Time Estimation
- Word, Character & Sentence Statistics
- Prediction History

### 📄 Reporting
- PDF Report Generation
- Downloadable Analysis Report

### 🎨 User Interface
- Modern Glassmorphism Design
- Responsive Streamlit Dashboard
- Animated Cards
- Hover Effects
- Dark Theme

## ⭐ Key Highlights

- 🧠 Fine-tuned **DistilBERT Transformer** for binary fake news classification
- 📊 AI confidence scoring with interactive probability visualization
- 📰 Real-time related news retrieval using **GNews API**
- ✅ Professional claim verification using **Google Fact Check API**
- 🔍 Semantic similarity matching using **Sentence Transformers**
- 📈 Dynamic trust score based on AI prediction and external evidence
- 📄 One-click PDF report generation
- 🎨 Modern glassmorphism-inspired responsive UI built with Streamlit
- ⚡ Optimized inference using PyTorch and Hugging Face Transformers

## 🏗️ System Architecture

```text
                     User
                       │
                       ▼
          Paste News Article
                       │
                       ▼
              Streamlit Frontend
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
DistilBERT        GNews API      Google Fact Check API
Prediction      Related News       Claim Verification
      │                │                │
      └────────────────┼────────────────┘
                       ▼
          Semantic Similarity Matching
                       │
                       ▼
          Trust Score Calculation Engine
                       │
                       ▼
     Interactive Dashboard & PDF Report
```

## 🧠 Model Workflow

```text
News Article
      │
      ▼
Text Preprocessing
      │
      ▼
DistilBERT Tokenizer
      │
      ▼
Fine-tuned DistilBERT Model
      │
      ▼
Real / Fake Prediction
      │
      ├──────────────► Confidence Score
      │
      ├──────────────► Related News (GNews API)
      │
      ├──────────────► Google Fact Check API
      │
      ▼
Semantic Similarity Matching
      │
      ▼
Trust Score Calculation
      │
      ▼
Interactive Dashboard
      │
      ▼
Downloadable PDF Report
```

The application combines **AI-based text classification** with **external evidence retrieval** to provide a comprehensive credibility assessment.

Instead of relying solely on the prediction produced by the DistilBERT model, it also incorporates:

- Semantic matching against professional fact-checks
- Related news retrieval
- Confidence estimation
- Trust score calculation
- Visual analytics and PDF reporting

## 📈 Model Performance

The fine-tuned DistilBERT model was evaluated on a held-out test set containing **6,735 news articles**.

| Metric | Score |
|---------|-------|
| Accuracy | ~100%* |
| Precision | ~100% |
| Recall | ~100% |
| F1-Score | ~100% |

**Test Set Distribution**

- 📰 Real News: **3,523**
- 🚨 Fake News: **3,212**

> *Values are rounded to two decimal places in the evaluation output.

## 🔐 Environment Variables

Create a `.env` file in the project root and add your API keys:

```env
GNEWS_API_KEY=your_gnews_api_key

GOOGLE_FACTCHECK_API_KEY=your_google_factcheck_api_key
```

The application automatically loads these environment variables using **python-dotenv**.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/AI_News_Detector.git
```

### 2. Navigate into the project

```bash
cd AI_News_Detector
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Programming Language** | Python |
| **Deep Learning** | PyTorch |
| **Transformer Model** | DistilBERT |
| **NLP Framework** | Hugging Face Transformers |
| **Semantic Search** | Sentence Transformers |
| **Web Framework** | Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly |
| **APIs** | Google Fact Check API, GNews API |
| **PDF Generation** | ReportLab |
| **Frontend** | HTML, CSS |
| **Version Control** | Git & GitHub |

## 📂 Project Structure

AI_News_Detector/

├── app.py                     # Main Streamlit application

├── components.py              # UI Components

├── utils.py                   # APIs & helper functions

├── style.css                  # Custom styling

├── requirements.txt

├── README.md

├── .gitignore

│

├── models/

│   └── final_model/           # Fine-tuned DistilBERT

│

├── notebooks/

│   ├── EDA.ipynb

│   ├── baseline_model.ipynb

│   └── Model_Train.ipynb

│

├── reports/

│   └── AI_Fake_News_Report.pdf


## 🚀 Future Roadmap

The project will continue to evolve with additional AI-powered capabilities:

- 🌍 Multi-language Fake News Detection
- 🖼️ Image-based Misinformation Detection
- 🎥 Video & Deepfake Detection
- 🧠 Explainable AI (SHAP / LIME)
- 📡 Real-time News Monitoring
- 🤖 LLM-assisted Claim Verification
- ☁️ Docker & Cloud Deployment
- 🔐 User Authentication
- 📱 Mobile Responsive Version
- 📊 Admin Analytics Dashboard

## 👨‍💻 Author

**Kushagra Bhatnagar**

