import streamlit as st

def show_model_information():

    import streamlit as st

    st.subheader("📊 Model Information")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Model",
        "DistilBERT"
    )

    c2.metric(
        "Dataset",
        "31K+"
    )

    c3.metric(
        "Task",
        "Binary Classification"
    )

    c4.metric(
        "Framework",
        "PyTorch"
    )

    left_exp, right_exp = st.columns(2)

    with left_exp:

        with st.expander("📖 About the Model"):

            st.write("""
This application uses a fine-tuned DistilBERT Transformer trained on over **31,000** news articles.

Unlike traditional keyword-based systems, DistilBERT understands contextual relationships between words before making predictions.

The model classifies articles using learned language patterns.

It is complemented with live news retrieval and professional fact-check services to assist credibility assessment.

The final decision should always be verified through trusted sources.
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
