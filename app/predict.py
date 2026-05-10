# Sinhala Sentiment Prediction

import re
import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load Model

model = load_model(
    "../models/bilstm_sentiment_model.keras"
)

# Load Tokenizer

with open(
    "../models/tokenizer.pkl",
    "rb"
) as file:
    tokenizer = pickle.load(file)

# Load Label Encoder

with open(
    "../models/label_encoder.pkl",
    "rb"
) as file:
    label_encoder = pickle.load(file)

# Text Cleaning Function

def clean_text(text):

    text = str(text)

    text = re.sub(
        r'[^a-zA-Z\u0D80-\u0DFF\s]',
        '',
        text
    )

    text = text.lower()

    text = re.sub(
        r'\s+',
        ' ',
        text
    ).strip()

    return text


# Predict Sentiment

def predict_sentiment(text):

    MAX_LENGTH = 100

    # Clean text
    cleaned_text = clean_text(text)

    # Convert to sequence
    sequence = tokenizer.texts_to_sequences(
        [cleaned_text]
    )

    # Padding
    padded_sequence = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post"
    )

    # Prediction
    prediction = model.predict(
        padded_sequence
    )

    predicted_class = np.argmax(
        prediction,
        axis=1
    )[0]

    confidence = np.max(prediction)

    sentiment = label_encoder.inverse_transform(
        [predicted_class]
    )[0]

    return sentiment, confidence