import streamlit as st
import plotly.graph_objects as go

def show_confidence_meter(confidence):

    import streamlit as st

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=confidence * 100,
            number={"suffix": "%"},
            gauge={
                "axis": {"range": [0, 100]},
                "steps": [
                    {"range": [0, 50], "color": "#EF4444"},
                    {"range": [50, 75], "color": "#FACC15"},
                    {"range": [75, 100], "color": "#22C55E"},
                ],
            },
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

    st.subheader("📈 Confidence Meter")

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

def show_probability_chart(
    fake_probability,
    real_probability
):

    import streamlit as st
    import plotly.graph_objects as go

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
                    labels=[
                        "Fake",
                        "Real"
                    ],
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

def show_authenticity_progress(trust_score):

    st.subheader("📈 Authenticity Score")

    st.progress(trust_score / 100)

    if trust_score >= 80:

        st.success(f"🟢 {trust_score}% Authentic")

    elif trust_score >= 60:

        st.warning(f"🟡 {trust_score}% Needs Verification")

    else:

        st.error(f"🔴 {trust_score}% Low Authenticity")


