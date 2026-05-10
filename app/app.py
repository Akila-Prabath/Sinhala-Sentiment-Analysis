# Sinhala Sentiment Analysis App

import streamlit as st

from predict import predict_sentiment

# Page Configuration

st.set_page_config(
    page_title="Sinhala Sentiment Analysis",
    page_icon="🇱🇰",
    layout="centered"
)

# Title

st.title(
    "Sinhala Sentiment Analysis"
)

st.markdown(
    """
    Deep learning based Sinhala sentiment analysis
    using TensorFlow and BiLSTM.
    """
)

# Text Input

user_input = st.text_area(
    "Enter Sinhala Text",
    height=150
)

# Prediction

if st.button("Predict Sentiment"):

    if user_input.strip() == "":

        st.warning(
            "Please enter Sinhala text."
        )

    else:

        sentiment, confidence = predict_sentiment(
            user_input
        )

        confidence_percent = round(
            confidence * 100,
            2
        )


        # Positive
        if sentiment == "POSITIVE":

            st.success(
                f"😊 Positive Sentiment"
            )

        # Negative
        elif sentiment == "NEGATIVE":

            st.error(
                f"😡 Negative Sentiment"
            )

        # Neutral
        else:

            st.info(
                f"😐 Neutral Sentiment"
            )