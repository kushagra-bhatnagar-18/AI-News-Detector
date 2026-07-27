import streamlit as st

def show_dashboard(
    prediction_text,
    confidence,
    trust_score,
    inference_time
):

    st.subheader("📊 AI Analysis Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(
            "Prediction",
            prediction_text
        )

    with c2:
        st.metric(
            "Confidence",
            f"{confidence:.2%}"
        )

    with c3:
        st.metric(
            "Trust Score",
            f"{trust_score}/100"
        )

    with c4:
        st.metric(
            "Inference Time",
            f"{inference_time:.2f}s"
        )

def show_search_summary(
    related_news,
    fact_checks
):

    st.subheader("🔎 Search Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Related Articles",
            len(related_news)
        )

    with c2:
        st.metric(
            "Fact Checks",
            len(fact_checks)
        )

    with c3:

        if len(fact_checks) > 0:
            status = "High"

        elif len(related_news) >= 3:
            status = "Medium"

        else:
            status = "Low"

        st.metric(
            "Evidence Strength",
            status
        )
