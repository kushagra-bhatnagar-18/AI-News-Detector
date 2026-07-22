import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)

st.title("📰 Fake News Detector")
st.write("Enter a news article below and our AI model will classify it as "
    "**Real News** or **Fake News**.")
st.info(
    "⚠️ Note: This model detects fake/real news based on linguistic patterns "
    "learned from training data. It is not a real-time fact checker and does "
    "not verify claims from the internet."
)

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("models/final_model")
    model = AutoModelForSequenceClassification.from_pretrained("models/final_model")
    return tokenizer, model

tokenizer, model = load_model()

news = st.text_area(
    "Paste your news article here:",
    height=250,
    placeholder="Enter news text..."
)

if st.button("🔍 Predict"):

    if news.strip() == "":
        st.warning("Please enter some news text.")
    else:
        with st.spinner("Analyzing news..."):
            inputs = tokenizer(
                news,
                return_tensors="pt",
                truncation=True,
                padding=True,
                max_length=512
            )
        
            with torch.no_grad():
                outputs = model(**inputs)
        
            probabilities = torch.softmax(outputs.logits, dim=1)
            fake_probability = probabilities[0][0].item()
            real_probability = probabilities[0][1].item()

            prediction = torch.argmax(probabilities,dim=1).item()

            st.subheader("Prediction Results")
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Fake Probability",
                    f"{fake_probability:.2%}"
                )
            
            with col2:
                st.metric(
                    "Real Probability",
                    f"{real_probability:.2%}"
                )

            if prediction == 1:
                st.success(f"✅ Real News\n\nConfidence:{real_probability:.2%}")
            else:
                st.error(f"❌ Fake News\n\nConfidence:{fake_probability:.2%}")

st.divider()
st.subheader("About the Model")
st.write(
      """
    This application uses a fine-tuned **DistilBERT transformer model**
    trained on a fake news dataset.

    **Technology Stack:**
    - Python
    - Hugging Face Transformers
    - PyTorch
    - Streamlit

    The model classifies news based on patterns learned from historical
    news articles.
    """
)