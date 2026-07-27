import requests
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import spacy
import streamlit as st
import os
from dotenv import load_dotenv()

nlp = spacy.load("en_core_web_sm")
semantic_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

try:
    GNEWS_API_KEY = st.secrets["GNEWS_API_KEY"]
    GOOGLE_FACTCHECK_API_KEY = st.secrets["GOOGLE_FACTCHECK_API_KEY"]
except Exception:
    load_dotenv()
    GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
    GOOGLE_FACTCHECK_API_KEY = os.getenv("GOOGLE_FACTCHECK_API_KEY")

def extract_claim(article):

    doc = nlp(article)

    if len(list(doc.sents)):
        sentence = list(doc.sents)[0].text.strip()

    else:

        sentence = article

    entities = []

    for ent in doc.ents:
        if ent.label_ in [

            "PERSON",
            "ORG",
            "GPE",
            "EVENT",
            "PRODUCT"

        ]:

            entities.append(ent.text)

    query = sentence

    if entities:

        query += " " + " ".join(entities)

    return query
def extract_keywords(text):

    doc = nlp(text)
    keywords=[]

    for token in doc:
        if token.pos_ in [
            "NOUN",
            "PROPN"
        ]:

            keywords.append(token.text)

    return " ".join(keywords[:10])


def get_related_news(query):

    url=(
        "https://gnews.io/api/v4/search"
        f"?q={query}"
        "&lang=en"
        "&max=5"
        f"&apikey={GNEWS_API_KEY}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return data.get("articles",[])

    except Exception as e:
        print(e)
        return []

def get_fact_checks(query):

    url = (
        "https://factchecktools.googleapis.com/v1alpha1/claims:search"
        f"?query={query}"
        f"&key={GOOGLE_FACTCHECK_API_KEY}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return data.get("claims",[])

    except Exception:
        return []

def semantic_fact_check_match(
    query,
    fact_checks,
    threshold=0.55
):

    if not fact_checks:
        return [], 0

    query_embedding = semantic_model.encode(
        query,
        convert_to_tensor=True
    )

    best_score = 0
    best_fact = None

    for fact in fact_checks:

        claim = fact.get("text", "")

        if isinstance(claim, list):
            claim = " ".join(claim)

        if not claim:
            continue

        claim_embedding = semantic_model.encode(
            claim,
            convert_to_tensor=True
        )

        score = cos_sim(
            query_embedding,
            claim_embedding
        ).max().item()

        if score > best_score:
            best_score = score
            best_fact = fact
        
    if best_score >= threshold:

        return [best_fact], best_score

    return [], best_score

