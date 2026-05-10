# Sinhala Sentiment Analysis App

import streamlit as st

from predict import predict_sentiment


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Sinhala Sentiment Analysis",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #111827
    );
    color: white;
}

/* Main Container */
.main-container {
    padding: 2rem;
    border-radius: 24px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    margin-top: 30px;
}

/* Main Title */
.main-title {
    font-size: 3.2rem;
    font-weight: 800;
    text-align: center;
    margin-bottom: 0.5rem;
    color: white;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

/* Text Area */
textarea {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 15px !important;
    border: 1px solid #334155 !important;
    font-size: 16px !important;
}

/* Input Label */
label {
    color: white !important;
    font-weight: 600 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color: white;
    border: none;
    padding: 0.9rem;
    border-radius: 14px;
    font-size: 1rem;
    font-weight: 700;
    transition: 0.3s;
}

/* Button Hover */
.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(124,58,237,0.5);
}

/* Result Box */
.result-box {
    padding: 1rem;
    border-radius: 16px;
    margin-top: 1.5rem;
    font-size: 1.2rem;
    font-weight: bold;
    text-align: center;
}

/* Positive */
.positive {
    background: rgba(34,197,94,0.15);
    border: 1px solid #22c55e;
    color: #4ade80;
}

/* Negative */
.negative {
    background: rgba(239,68,68,0.15);
    border: 1px solid #ef4444;
    color: #f87171;
}

/* Neutral */
.neutral {
    background: rgba(234,179,8,0.15);
    border: 1px solid #eab308;
    color: #fde047;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# Main Container

st.markdown(
    '<div class="main-container">',
    unsafe_allow_html=True
)

# Title

st.markdown(
    """
    <div class="main-title">
        🧠 Sinhala Sentiment Analysis
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Deep learning based Sinhala sentiment analysis using TensorFlow and BiLSTM.
    </div>
    """,
    unsafe_allow_html=True
)


# Text Input

user_input = st.text_area(
    "Enter Sinhala Text",
    height=180,
    placeholder="මෙහි සිංහල වාක්‍යයක් ඇතුළත් කරන්න..."
)


# Predict Button

predict_btn = st.button(
    "🚀 Predict Sentiment"
)


# Prediction Logic

if predict_btn:

    if user_input.strip() == "":

        st.warning(
            "⚠️ Please enter Sinhala text."
        )

    else:

        with st.spinner(
            "Analyzing sentiment..."
        ):

            sentiment, confidence = predict_sentiment(
                user_input
            )

        confidence_percent = round(
            confidence * 100,
            2
        )


        # Positive
        if sentiment == "POSITIVE":

            st.markdown(
                f"""
                <div class="result-box positive">
                    😊 Positive Sentiment
                </div>
                """,
                unsafe_allow_html=True
            )


        # Negative
        elif sentiment == "NEGATIVE":

            st.markdown(
                f"""
                <div class="result-box negative">
                    😡 Negative Sentiment
                </div>
                """,
                unsafe_allow_html=True
            )


        # Neutral
        else:

            st.markdown(
                f"""
                <div class="result-box neutral">
                    😐 Neutral Sentiment
                </div>
                """,
                unsafe_allow_html=True
            )


# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Built with using Streamlit + BiLSTM
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)