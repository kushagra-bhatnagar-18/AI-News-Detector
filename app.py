import streamlit as st
import torch
import time
import plotly.graph_objects as go
from utils import (
        get_related_news,
        get_fact_checks,
        extract_claim,
        extract_keywords,
        semantic_fact_check_match
    )

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
)


from Components import(
    show_prediction,
    show_dashboard,
    show_trust_score,
    show_fact_check,
    show_confidence_meter,
    show_probability_chart,
    show_related_news,
    show_overall_reliability,
    show_model_information,
    show_search_summary,
    show_ai_reasoning,
    show_authenticity_indicators,
    show_recommendation,
    show_reliability_breakdown,
    show_authenticity_progress,
    generate_pdf_report,
)

st.set_page_config(
    page_title="AI-Powered Fake News Detection",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

load_css()

@st.cache_resource
def load_model():

    MODEL_NAME = "KBhatnagar/AI-Fake-News-Detector"

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME
    )

    return tokenizer, model

tokenizer, model = load_model()

if "history" not in st.session_state:
    st.session_state.history = []

if "news_input" not in st.session_state:
    st.session_state.news_input = ""

with st.sidebar:

    st.title("🤖 AI Fake News Detector")

    st.markdown("---")

    st.subheader("📌 Model")
    st.write("Fine-tuned **DistilBERT**")

    st.subheader("📚 Dataset")
    st.write("""
**Training Articles**

31,428 Articles

• Fake News

• Real News
""")

    st.subheader("⚙️ Tech Stack")
    st.write("""
• 🤗 Hugging Face

• PyTorch

• Streamlit

• Google Fact Check API

• NewsAPI
""")

    st.subheader("👨‍💻 Developer")
    st.write("Kushagra Bhatnagar")

    st.markdown("---")

    st.success("🤖 DistilBERT Ready")

    if st.session_state.history:

        latest = st.session_state.history[-1]

        st.metric(
            "Latest Prediction",
            latest["Prediction"]
        )

        st.metric(
            "Confidence",
            f"{latest['Confidence']:.2%}"
        )

        st.markdown("### 🕘 Recent Predictions")

        for item in reversed(st.session_state.history[-5:]):

            emoji = (
                "✅"
                if item["Prediction"] == "Real"
                else "❌"
            )

            st.write(
                f"{emoji} {item['Prediction']} ({item['Confidence']:.2%})"
            )

    else:

        st.info("Analyze an article to start building prediction history.")

    st.markdown("---")

    st.caption(
        "DistilBERT v1.0\n\nInference Device: CPU"
    )
st.markdown(
"""
<h1 style="
text-align:center;
font-size:58px;
font-weight:700;
background:linear-gradient(90deg,#4F46E5,#06B6D4);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
">

Fake News Detector

</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div style="
text-align:center;
font-size:20px;
margin-top:-15px;
margin-bottom:30px;
color:#D1D5DB;
">

Detect whether a news article resembles
<b>Real</b> or <b>Fake</b> news using a
fine-tuned <b>DistilBERT Transformer</b>.

</div>
""",
unsafe_allow_html=True
)
st.warning(
"""
### ⚠ Disclaimer

This application combines AI-based text classification with real-time news and existing fact-checks from external sources.

The AI prediction is based on learned language patterns and does not independently verify factual accuracy. Always consult reliable news organizations and professional fact-checkers before relying on important information.
"""
)

st.subheader("📝 News Article")
st.write(
    "Paste a complete news article below and let the AI analyze it."
)

st.text_area(
    "",
    key="news_input",
    height=260,
    placeholder="""
Example:

Prime Minister Narendra Modi today inaugurated a new highway project
aimed at improving transportation infrastructure across northern India.
"""
)

news = st.session_state.news_input
word_count = len(news.split())
char_count = len(news)
sentence_count = len(
    [s for s in news.split(".") if s.strip()]
)

reading_time = max(
    1,
    word_count // 200
)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Words", word_count)
m2.metric("Characters", char_count)
m3.metric("Sentences", sentence_count)
m4.metric(
    "Reading Time",
    f"{reading_time} min"
)

st.divider()

b1, b2 = st.columns([5,1])
with b1:
    predict = st.button(
        "🚀 Analyze Article",
        use_container_width=True
    )
def clear_news():
    st.session_state.news_input = ""

with b2:
    st.button(
        "🗑️",
        use_container_width=True,
        on_click = clear_news
    ):
        
if predict:
    if news.strip() == "":
        st.warning("Please enter a news article.")
        st.stop()

    start_time = time.time()

    with st.spinner("🧠 Running DistilBERT inference..."):
        inputs = tokenizer(
            news,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = model(**inputs)

        probabilities = torch.softmax(
            outputs.logits,
            dim=1
        )

        fake_probability = probabilities[0][0].item()
        real_probability = probabilities[0][1].item()

        prediction = torch.argmax(
            probabilities,
            dim=1
        ).item()

    inference_time = time.time() - start_time

    confidence = (
        real_probability
        if prediction == 1
        else fake_probability
    )

    prediction_text = (
        "Real"
        if prediction == 1
        else "Fake"
    )
   
    query = extract_claim(news)
    keywords = extract_keywords(news)
    
    queries = [

    query,
    keywords,

    " ".join(query.split()[:8]),
    " ".join(query.split()[:5])

    ]
    queries = list(set([q.strip() for q in queries if q.strip()]))

    fact_checks = []
    related_news = []
    for q in queries:

        if not q.strip():
            continue

        fc = get_fact_checks(q)
        rn = get_related_news(q)

        if fc:
            fact_checks.extend(fc)
        if rn:
            related_news.extend(rn)

    seen_claims = set()
    unique_fact_checks = []
    for fc in fact_checks:
        text = fc.get("text", "")

        if text not in seen_claims:
            seen_claims.add(text)
            unique_fact_checks.append(fc)

    fact_checks = unique_fact_checks

    seen = set()
    unique_news = []

    for article in related_news:
        url = article.get("url")

        if url not in seen:
            seen.add(url)
            unique_news.append(article)

    related_news = unique_news
    fact_checks, similarity_score = semantic_fact_check_match(
        query,
        fact_checks
    )
    if not fact_checks:
        similarity_score = 0

    has_fact_check = len(fact_checks) > 0
    has_related_news = len(related_news) > 0

    rating = ""

    if has_fact_check:

        review_data = fact_checks[0].get("claimReview")

        if review_data:

            rating = review_data[0].get(
                "textualRating",
                ""
            ).lower()

    fact_check_disputed = any(
        word in rating
        for word in [
            "false",
            "fake",
            "incorrect",
            "misleading",
            "wrong",
            "falso",
            "falsch",
            "errado"
        ]
    )

    trust_score = 0

    trust_score += int(confidence * 50)

    if has_related_news:
        trust_score += 20

    if has_fact_check:

        if fact_check_disputed:
            trust_score -= 30
        else:
            trust_score += 30

    trust_score = max(
        0,
        min(100, trust_score)
    )

    st.session_state.history.append(
            {
                "Prediction": prediction_text,
                "Confidence": confidence
            }
        )

    if len(st.session_state.history) > 5:
            st.session_state.history = (
                st.session_state.history[-5:]
            )
    st.header("🛡️ News Credibility Assessment")

    show_prediction(
        prediction,
        confidence
    )

    st.divider()
    show_dashboard(
        prediction_text,
        confidence,
        trust_score,
        inference_time
    )

    st.divider()
    show_trust_score(
        trust_score
    )

    st.divider()
    show_reliability_breakdown(
        confidence,
        has_fact_check,
        has_related_news,
        fact_check_disputed,
        trust_score
    )

    st.divider()
    show_authenticity_progress(
        trust_score
    )

    st.divider()
    show_confidence_meter(confidence)

    st.divider()
    show_probability_chart(
        fake_probability,
        real_probability
    )
    st.divider()

    if fact_checks:

        review = fact_checks[0]["claimReview"][0]

        show_fact_check(
            review,
            fact_checks[0].get(
                "text",
                "No claim text available"
            ),
            similarity_score   
        )

    else:

        st.subheader("🔍 Fact Check Status")

        st.warning(
            "⚠ No matching professional fact-check found."
        )

    st.divider()
    show_search_summary(
        related_news,
        fact_checks,
    )

    st.divider()
    show_related_news(
        related_news
    )

    st.divider()
    show_authenticity_indicators(
        confidence,
        related_news,
        fact_check_disputed
    )

    st.divider()
    show_overall_reliability(
        prediction,
        confidence,
        has_fact_check,
        has_related_news,
        fact_check_disputed
    )

    st.divider()
    show_recommendation(
        prediction,
        confidence,
        fact_check_disputed
    )

    st.divider()
    show_ai_reasoning(
        prediction,
        confidence,
        fact_check_disputed,
        has_related_news
    )

    st.divider()
    show_model_information()

    st.divider()

    pdf_file = generate_pdf_report(
        prediction_text,
        confidence,
        trust_score,
        has_fact_check,
        has_related_news,
        fact_check_disputed,
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            "📄 Download AI Report",
            file,
            file_name="AI_Fake_News_Report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

    st.divider()

    st.caption(
"""
© 2026 Kushagra Bhatnagar

AI-Powered Fake News Detection using DistilBERT,
Google Fact Check API,
NewsAPI,
PyTorch,
and Streamlit.
"""
)