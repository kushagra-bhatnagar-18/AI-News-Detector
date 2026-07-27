import streamlit as st
SOURCE_RATINGS = {

    "Reuters": ("🟢","High"),
    "Reuters.com": ("🟢","High"),

    "Associated Press": ("🟢","High"),
    "AP News": ("🟢","High"),

    "BBC": ("🟢","High"),
    "BBC News": ("🟢","High"),

    "The Guardian": ("🟢","High"),
    "The Hindu": ("🟢","High"),

    "CNN": ("🟡","Medium"),
    "Fox News": ("🟡","Medium"),
    "NBC News": ("🟡","Medium"),
    "ABC News": ("🟡","Medium"),

    "NDTV": ("🟡","Medium"),
    "India Today": ("🟡","Medium"),
    "Times of India": ("🟡","Medium"),
    "Hindustan Times": ("🟡","Medium"),
}

def show_related_news(related_news):

    import streamlit as st

    st.subheader("📰 Related News")

    if related_news:

        for article in related_news[:5]:

            with st.container():

                col1, col2 = st.columns([1,3])

                with col1:

                    if article.get("image"):

                        st.image(
                            article["image"],
                            use_container_width=True
                        )

                with col2:

                    source = article.get("source", {}).get(
                        "name",
                        "Unknown"
                    )

                    icon, credibility = SOURCE_RATINGS.get(
                        source,
                        ("⚪", "Unknown")
                    )

                    st.markdown(
                        f"### [{article['title']}]({article['url']})"
                    )

                    st.caption(
                        f"{icon} {source} • {credibility} Credibility • 📅 {article['publishedAt'][:10]}"
                    )

                    if credibility == "High":
                        st.success("Reliable News Source")
                    elif credibility == "Medium":
                        st.info("Generally Reliable Source")
                    else:
                        st.warning("Source Credibility Unknown")

                    st.write(
                        article.get(
                            "description",
                            "No description available."
                        )
                    )

                    st.link_button(
                        "🔗 Read Full Article",
                        article["url"]
                    )

    else:

        st.info(
            "No related news articles found."
        )

def show_fact_check(review, claim, similarity_score):
    st.subheader("🔍 Fact Check Status")
    st.error("❌ Existing professional fact-check found")
    st.write(
        f"**Rating:** {review.get('textualRating','Unknown')}"
    )
    st.write(
        f"**Publisher:** {review['publisher']['name']}"
    
    )
    st.metric(
        "Semantic Match",
        f"{similarity_score:.1%}"
    )
    st.info(claim)
    st.link_button(
        "Read Full Fact Check",
        review["url"]
    )

def semantic_fact_check_match(

    query,

    fact_checks,

    threshold=0.45

):

    if not fact_checks:

        return [],0

    query_embedding = semantic_model.encode(

        query,

        convert_to_tensor=True

    )

    scored=[]

    for fact in fact_checks:

        claim = fact.get("text","")

        if not claim:

            continue

        claim_embedding = semantic_model.encode(

            claim,

            convert_to_tensor=True

        )

        score = cos_sim(

            query_embedding,

            claim_embedding

        ).item()

        scored.append((score,fact))

    scored.sort(

        key=lambda x:x[0],

        reverse=True

    )

    if scored and scored[0][0]>=threshold:

        return [scored[0][1]],scored[0][0]

    return [],0
