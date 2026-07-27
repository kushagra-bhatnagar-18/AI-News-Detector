import streamlit as st

def show_prediction(prediction, confidence):
    if prediction == 1:
        st.success(
            f"🟢 Looks like Real News\n\nConfidence: {confidence:.2%}"
        )
    else:
        st.error(
            f"🔴 Looks like Fake News\n\nConfidence: {confidence:.2%}"
        )

def show_ai_reasoning(
    prediction,
    confidence,
    fact_check_disputed,
    has_related_news
):

    st.subheader("🧠 AI Explanation")

    reasons = []

    if confidence >= 0.90:
        reasons.append(
            "✅ The model is highly confident about its prediction."
        )

    elif confidence >= 0.75:
        reasons.append(
            "🟡 The model has moderate confidence."
        )

    else:
        reasons.append(
            "⚠ The prediction confidence is relatively low."
        )

    if has_related_news:
        reasons.append(
            "📰 Similar news articles were found from online sources."
        )

    else:
        reasons.append(
            "📰 No closely related news articles were found."
        )

    if fact_check_disputed:

        reasons.append(
            "❌ Professional fact-checkers dispute a similar claim."
        )

    else:

        reasons.append(
            "✔ No professional dispute was found for this claim."
        )

    if prediction == 1:

        reasons.append(
            "🤖 The article's writing style resembles genuine news."
        )

    else:

        reasons.append(
            "🤖 The article contains patterns commonly seen in misleading news."
        )

    for item in reasons:

        st.write(item)

def show_recommendation(
    prediction,
    confidence,
    fact_check_disputed
):

    st.subheader("💡 AI Recommendation")

    if fact_check_disputed:

        st.error("""
Do not share this article until verified.

Professional fact-checkers have disputed a similar claim.
""")

    elif prediction == 1 and confidence > 0.9:

        st.success("""
This article appears reliable.

Still cross-check with trusted sources if the topic is important.
""")

    elif prediction == 0:

        st.warning("""
Treat this article cautiously.

Look for multiple independent sources before believing or sharing it.
""")

    else:

        st.info("""
Additional verification is recommended before relying on this article.
""")

