import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import time
import plotly.graph_objects as go

st.set_page_config(
    page_title="AI Fake News Detector",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

@st.cache_resource
def load_model():

    tokenizer = AutoTokenizer.from_pretrained(
        "models/final_model"
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        "models/final_model"
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
- 🤗 Hugging Face
- PyTorch
- Streamlit
""")

    st.subheader("👨‍💻 Developer")

    st.write("Kushagra Bhatnagar")

    st.markdown("---")

    st.success("🤖 DistilBERT Ready")

    if st.session_state.history:

        st.markdown("### 🕘 Recent Predictions")

        for item in st.session_state.history[-5:]:

            emoji = "✅" if item["Prediction"] == "Real" else "❌"

            st.write(
                f"{emoji} {item['Prediction']} ({item['Confidence']:.2%})"
            )

st.markdown(
"""
<h1 style="
text-align:center;
font-size:56px;
font-weight:700;
background:linear-gradient(90deg,#4F46E5,#06B6D4);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
">

📰 AI-Powered Fake News Detection

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

This application predicts whether a news article resembles
**Real** or **Fake** news based on language patterns learned
during training.

It **does not perform live fact checking**
and should not be considered a source of truth.
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
reading_time = max(1, word_count // 200)

m1, m2, m3, m4 = st.columns(4)

m1.metric("Words", word_count)
m2.metric("Characters", char_count)
m3.metric("Sentences", sentence_count)
m4.metric("Reading Time", f"{reading_time} min")

st.divider()

predict = st.button(
    "🚀 Analyze Article",
    use_container_width=True
)

if predict:

    if news.strip() == "":
        st.warning("Please enter a news article.")
        st.stop()

    start = time.time()

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

        probs = torch.softmax(outputs.logits, dim=1)

        fake_probability = probs[0][0].item()
        real_probability = probs[0][1].item()

        prediction = torch.argmax(probs, dim=1).item()

    inference_time = time.time() - start

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

    st.divider()

    st.header("🎯 AI Verdict")

    if prediction == 1:
        verdict = "REAL NEWS"
        emoji = "✅"
        css = "real"
    else:
        verdict = "FAKE NEWS"
        emoji = "❌"
        css = "fake"

    st.markdown(
        f"""
<div class="verdict-card">

<div class="verdict-title {css}">
{emoji} {verdict}
</div>

<div class="verdict-confidence">
{confidence:.2%}
</div>

<div class="verdict-small">
Model Confidence
</div>

</div>
""",
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:

        st.metric(
            "Inference Time",
            f"{inference_time:.2f} sec"
        )

        st.metric(
            "Prediction",
            prediction_text
        )

        if confidence > 0.95:
            st.success("🟢 Very High Confidence")

        elif confidence > 0.80:
            st.info("🔵 High Confidence")

        elif confidence > 0.60:
            st.warning("🟡 Moderate Confidence")

        else:
            st.error("🔴 Low Confidence")

    with right:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=confidence*100,
                number={"suffix":"%"},
                gauge={
                    "axis":{"range":[0,100]},
                    "bar":{"color":"#2563EB"},
                    "steps":[
                        {
                            "range":[0,50],
                            "color":"#EF4444"
                        },
                        {
                            "range":[50,75],
                            "color":"#FACC15"
                        },
                        {
                            "range":[75,100],
                            "color":"#22C55E"
                        }
                    ]
                }
            )
        )

        gauge.update_layout(
            height=280,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    st.divider()

    st.subheader("📊 Prediction Probabilities")

    p1, p2 = st.columns(2)

    with p1:

        st.write(
            f"🟥 **Fake Probability:** {fake_probability:.2%}"
        )

        st.progress(fake_probability)

        st.write(
            f"🟩 **Real Probability:** {real_probability:.2%}"
        )

        st.progress(real_probability)
        with p2:

            pie = go.Figure(
                data=[
                    go.Pie(
                        labels=["Fake", "Real"],
                        values=[
                        fake_probability,
                        real_probability
                    ],
                        hole=0.65,
                        marker=dict(
                        colors=[
                            "#EF4444",
                            "#22C55E"
                        ]
                    )
                )
            ]
        )

        pie.update_layout(
            showlegend=True,
            height=360,
            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    st.divider()

    st.subheader("🧠 AI Assessment")

    if prediction == 1:

        if confidence > 0.95:

            st.success("""
The writing style strongly resembles authentic news reporting.

The model is highly confident in this prediction.

This result is based on linguistic patterns learned during training.
""")

        elif confidence > 0.75:

            st.info("""
The article appears to resemble genuine news.

Confidence is reasonably high, but manual verification is still recommended for important information.
""")

        else:

            st.warning("""
The article resembles real news, but confidence is moderate.

Consider verifying this information using trusted news sources.
""")

    else:

        if confidence > 0.95:

            st.error("""
The writing style strongly resembles fake or misleading news.

The model is highly confident in this prediction.

Always verify suspicious news using reliable sources.
""")

        elif confidence > 0.75:

            st.warning("""
The article contains several characteristics commonly found in misleading news.

Manual verification is recommended.
""")

        else:

            st.info("""
The article contains mixed linguistic signals.

The prediction confidence is moderate.
Please verify the information before drawing conclusions.
""")

    st.divider()

    st.markdown("## 📊 Model Information")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Model",
        "DistilBERT"
    )

    c2.metric(
        "Accuracy",
        "99.8%"
    )

    c3.metric(
        "Dataset",
        "31K+"
    )

    c4.metric(
        "Framework",
        "PyTorch"
    )

    left_exp, right_exp = st.columns(2)

    with left_exp:

        with st.expander("📖 About the Model"):

            st.write("""
This application uses a fine-tuned DistilBERT Transformer trained on more than **31,000** news articles.

Instead of relying on keywords, DistilBERT understands the context and relationships between words before making a prediction.

The model classifies news articles based on writing patterns and **does not perform real-time internet fact checking**.
""")

    with right_exp:

        with st.expander("💡 Try Sample Articles"):

            st.markdown("### 📰 Real Example")

            st.code("""
Prime Minister Narendra Modi inaugurated a new expressway today aimed at improving transport connectivity.
""")

            st.markdown("### ❌ Fake Example")

            st.code("""
Scientists confirm that aliens have officially taken over the White House.
""")
            st.divider()

            st.caption(
    "© 2026 Kushagra Bhatnagar | DistilBERT • Hugging Face • PyTorch • Streamlit"
)