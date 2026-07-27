import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import datetime
import os

def generate_pdf_report(
    prediction_text,
    confidence,
    trust_score,
    has_fact_check,
    has_related_news,
    fact_check_disputed,
):

    filename = "AI_Fake_News_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI Fake News Detection Report</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"Generated on: {datetime.datetime.now().strftime('%d %B %Y %H:%M')}",
            styles["Normal"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            f"<b>Prediction:</b> {prediction_text}",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"<b>AI Confidence:</b> {confidence:.2%}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Trust Score:</b> {trust_score}/100",
            styles["Normal"]
        )
    )

    if fact_check_disputed:

        reliability = "Low Reliability"

    elif trust_score >= 80:

        reliability = "High Reliability"

    elif trust_score >= 60:

        reliability = "Needs Verification"

    else:

        reliability = "Low Reliability"

    story.append(
        Paragraph(
            f"<b>Overall Reliability:</b> {reliability}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Professional Fact Check:</b> {'Found' if has_fact_check else 'Not Found'}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Related News Articles:</b> {'Available' if has_related_news else 'Not Available'}",
            styles["Normal"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            "<b>Disclaimer</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "This report is generated using an AI model (DistilBERT) together with professional fact-check information and related news sources. The prediction should not be considered a substitute for independent verification.",
            styles["Normal"]
        )
    )

    doc.build(story)

    return filename