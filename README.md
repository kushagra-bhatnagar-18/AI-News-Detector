# 📰 AI-Powered Fake News Detection System

An NLP-based Fake News Detection system that classifies news articles as **Real** or **Fake** using Machine Learning and Transformer-based Deep Learning models.

This project explores traditional Natural Language Processing approaches and modern Transformer architectures by comparing a baseline Machine Learning model with a fine-tuned DistilBERT model.

---

# 🚀 Features

- Exploratory Data Analysis of news datasets
- Text preprocessing and cleaning
- Baseline Fake News Classification using:
  - TF-IDF Vectorization
  - Logistic Regression
- Transformer-based Fake News Classification using:
  - DistilBERT
  - Hugging Face Transformers
  - PyTorch
- Model evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix
- Interactive prediction interface using Streamlit

---

# 🏗️ Project Workflow

```
News Dataset
        |
        ↓
Exploratory Data Analysis
        |
        ↓
Text Preprocessing
        |
        ↓
Baseline Machine Learning Model
(TF-IDF + Logistic Regression)
        |
        ↓
Transformer Model
(Fine-tuned DistilBERT)
        |
        ↓
Streamlit Web Application
```

---

# 📂 Project Structure

```
AI_News_Detector/

│
├── notebooks/
│   ├── EDA.ipynb
│   ├── baseline_model.ipynb
│   └── Model_Train.ipynb
│
├── models/
│
├── results/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# 🧠 Models Used

## 1. Baseline Model

### TF-IDF + Logistic Regression

The baseline model converts news text into numerical representations using TF-IDF and performs binary classification using Logistic Regression.

### Purpose:
- Establish a traditional Machine Learning benchmark
- Compare performance with Transformer-based models

---

## 2. Transformer Model

### DistilBERT

A fine-tuned DistilBERT model from Hugging Face is used for Fake News Classification.

### Advantages:
- Understands contextual meaning of words
- Captures complex language patterns
- Provides better text representation compared to traditional NLP techniques

---

# 📊 Model Evaluation

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-learn

## Deep Learning / NLP

- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets

## Deployment

- Streamlit

---

# ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd AI_News_Detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Enter a news article and get the prediction:

```
Real News / Fake News
```

---

# 📌 Future Improvements

- Real-time fact verification using external APIs
- News source credibility analysis
- Explainable AI using SHAP/LIME
- Multilingual fake news detection
- Improved deployment pipeline
- Evidence-based claim verification

---

# 👨‍💻 Author

**Kushagra Bhatnagar**
