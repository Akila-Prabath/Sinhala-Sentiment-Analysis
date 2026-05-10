# Sinhala Sentiment Analysis using TensorFlow & BiLSTM

A deep learning based Sinhala sentiment analysis project built using **TensorFlow**, **Keras**, and **Bidirectional LSTM (BiLSTM)** architecture for classifying Sinhala text sentiments.

This project focuses on Natural Language Processing (NLP) for the Sinhala language and provides a complete workflow including:

- Data preprocessing
- Tokenization & padding
- Deep learning model training
- Real-time sentiment prediction
- Streamlit web application deployment

---

## 🚀 Features

- ✅ Sinhala text sentiment classification
- ✅ TensorFlow + Keras implementation
- ✅ Bidirectional LSTM (BiLSTM) deep learning model
- ✅ Real-time sentiment prediction
- ✅ Streamlit web application
- ✅ Model saving and loading support
- ✅ Sinhala NLP preprocessing pipeline
- ✅ User-friendly interface

---

## 🧠 Model Architecture

The project uses a **Bidirectional Long Short-Term Memory (BiLSTM)** neural network for better contextual understanding of Sinhala sentences.

### Main Technologies

- TensorFlow
- Keras
- Python
- Streamlit
- NumPy
- Pandas
- Scikit-learn

### Deep Learning Pipeline

1. Text Cleaning
2. Tokenization
3. Sequence Padding
4. Embedding Layer
5. BiLSTM Layer
6. Dense Classification Layer
7. Softmax / Sigmoid Prediction

---

## 📂 Project Structure

```bash
Sinhala-Sentiment-Analysis/
│
├── app/
│   ├── app.py                          # Streamlit web application
│   └── predict.py                      # Real-time sentiment prediction functions
│
├── data/
│   ├── preprocessed/
│   │   ├── train_preprocessed.csv      # Preprocessed training dataset
│   │   └── test_preprocessed.csv       # Preprocessed testing dataset
│   │
│   └── raw/
│       ├── train.tsv                   # Original training dataset
│       └── test.tsv                    # Original testing dataset
│
├── models/
│   ├── bilstm_sentiment_model.keras    # Trained BiLSTM TensorFlow model
│   ├── tokenizer.pkl                   # Saved tokenizer
│   └── label_encoder.pkl               # Saved label encoder
│
├── notebooks/
│   ├── preprocessing.ipynb             # Data preprocessing notebook
│   └── training.ipynb                  # Model training notebook
│
├── .gitignore                          # Git ignored files
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```
---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Akila-Prabath/Sinhala-Sentiment-Analysis.git
cd Sinhala-Sentiment-Analysis
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

Then open:

```bash
http://localhost:8501
```

---

## 🏋️ Train the Model

Run the training script:

```bash
python train.py
```

After training, the model will be saved as:

```bash
bilstm_sentiment_model.keras
```

---

## 🔍 Real-Time Prediction

Example prediction:

```python
from predict import predict_sentiment

text = "මේක ගොඩක් හොඳයි"
result = predict_sentiment(text)

print(result)
```

---

## 📊 Example Sentiments

| Sinhala Text | Predicted Sentiment |
|---|---|
| මේක ගොඩක් හොඳයි | Positive |
| මේක හරිම නරකයි | Negative |
| අද සාමාන්‍ය දවසක් | Neutral |

---

## 🧪 Model Architecture Example

```python
model = Sequential([
    Embedding(MAX_WORDS, EMBEDDING_DIM, input_length=MAX_LENGTH),

    Bidirectional(LSTM(128, return_sequences=True)),
    Dropout(0.3),

    Bidirectional(LSTM(64)),
    Dropout(0.3),

    Dense(64, activation='relu'),
    Dropout(0.2),

    Dense(num_classes, activation='softmax')
])
```
---
## Screenshot 

<img width="1481" height="812" alt="Screenshot (495)" src="https://github.com/user-attachments/assets/f7b4712c-ac93-4a77-9e4e-2804aaf1cade" />

---

## 📈 Future Improvements

- Transformer-based Sinhala sentiment analysis
- Sinhala BERT integration
- Attention mechanisms
- Larger Sinhala datasets
- Multiclass sentiment classification
- API deployment
- Mobile application integration

---

## 🌍 Research & Inspiration

This project is inspired by Sinhala NLP and sentiment analysis research using deep learning and BiLSTM architectures. Recent Sinhala sentiment analysis studies show that BiLSTM-based models achieve strong performance for low-resource languages like Sinhala. :contentReference[oaicite:0]{index=0}

Useful research references:

- *Sentiment Analysis for Sinhala Language using Deep Learning Techniques* :contentReference[oaicite:1]{index=1}
- *Sentiment Analysis of Sinhala News Comments using Sentence-State LSTM Networks* :contentReference[oaicite:2]{index=2}

---

## 📦 Requirements

Example dependencies:

```txt
tensorflow
streamlit
numpy
pandas
scikit-learn
pickle-mixin
```

---

## 👨‍💻 Author

### Akila Prabath

- GitHub: [Akila-Prabath GitHub](https://github.com/Akila-Prabath?utm_source=chatgpt.com)

---

## ⭐ Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛠️ Contribute improvements
- 📢 Share with others

---

## 📜 License

This project is licensed under the MIT License.

---
