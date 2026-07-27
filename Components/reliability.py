import streamlit as st
def show_trust_score(score):
    st.subheader("⭐ Overall Trust Score")
    if score >= 80:
        st.success(
            f"🟢 {score}/100 - High Reliability"
        )

    elif score >= 60:
        st.warning(
            f"🟡 {score}/100 - Needs Verification"
        )

    else:
        st.error(
            f"🔴 {score}/100 - Low Reliability"
        )

    st.caption(
        "Calculated using AI confidence, professional fact-check evidence, and related news availability."
    )

def show_reliability_breakdown(
    confidence,
    has_fact_check,
    has_related_news,
    fact_check_disputed,
    trust_score
):

    st.subheader("📊 Reliability Breakdown")

    ai_score = int(confidence * 50)

    fact_score = 0

    if has_fact_check:

        if fact_check_disputed:
            fact_score = -30
        else:
            fact_score = 30

    news_score = 20 if has_related_news else 0

    st.markdown(f"""
| Evidence | Contribution |
|-----------|-------------:|
| 🤖 AI Confidence | +{ai_score} |
| 📰 Related News | +{news_score} |
| 🔍 Professional Fact Check | {fact_score:+d} |
| **Final Trust Score** | **{trust_score}/100** |
""")

def show_overall_reliability(
    prediction,
    confidence,
    has_fact_check,
    has_related_news,
    fact_check_disputed
):

    import streamlit as st

    st.subheader("🛡️ Overall Reliability")

    if prediction == 1 and fact_check_disputed:

        st.error(f"""
### ❌ Claim disputed by professional fact-checkers

Although the AI classified this article as **Real** with **{confidence:.2%} confidence**,

professional fact-check organizations have already marked a similar claim as **False or Misleading**.

External evidence should be trusted over AI prediction.
""")

    elif prediction == 0 and fact_check_disputed:

        st.success(f"""
### ✅ AI prediction agrees with fact-check evidence

The AI classified this article as **Fake** with **{confidence:.2%} confidence**.

Professional fact-check organizations have also disputed a similar claim.
""")

    elif prediction == 1 and (has_fact_check or has_related_news):

        st.warning(f"""
### 🟡 Appears Reliable

• AI Confidence: **{confidence:.2%}**

• Supporting news evidence exists.

• No conflicting professional fact-check was found.

Manual verification is still recommended.
""")

    elif prediction == 0 and not has_fact_check and not has_related_news:

        st.warning(f"""
### 🔴 Potentially Misleading

• AI Confidence: **{confidence:.2%}**

No professional fact-checks or supporting news articles were found.

This prediction is based solely on language patterns.
""")

    else:

        st.info(f"""
### ⚪ Insufficient External Evidence

AI Confidence: **{confidence:.2%}**

The prediction was generated successfully.

However, external verification was limited.

Treat this as AI-assisted analysis rather than confirmed fact.
""")

def show_authenticity_indicators(
    confidence,
    related_news,
    fact_check_disputed
):

    st.subheader("🧩 Authenticity Indicators")

    c1, c2 = st.columns(2)

    with c1:

        if confidence >= 0.90:
            st.success(f"🟢 AI Confidence: {confidence:.2%}")

        elif confidence >= 0.75:
            st.warning(f"🟡 AI Confidence: {confidence:.2%}")

        else:
            st.error(f"🔴 AI Confidence: {confidence:.2%}")

        if len(related_news) > 0:
            st.success(
                f"📰 Related Articles: {len(related_news)} found"
            )

        else:
            st.error("📰 No related articles found")

    with c2:

        if fact_check_disputed:
            st.error(
                "❌ Professional fact-check dispute found"
            )

        else:
            st.success(
                "✅ No professional dispute found"
            )

        sources = {
            article["source"]["name"]
            for article in related_news
        }

        if sources:

            st.info(
                "Reliable Sources:\n\n"
                + "\n".join(
                    list(sources)[:5]
                )
            )

        else:

            st.warning("Unknown sources")
