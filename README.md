# 🤖 AI Support Ticket Classifier

An AI-powered web application that automatically classifies customer support tickets using Machine Learning and Natural Language Processing (NLP).

## 📌 Project Overview

This application analyzes support tickets, predicts their category, and provides an appropriate response.

### Example Tickets

| User Ticket | Predicted Category |
|-------------|--------------------|
| I forgot my password | Password & Login Support |
| I can't log in because my password is incorrect | Password & Login Support |
| How can I see my leave balance? | HR Leave Management |

The AI groups tickets based on their **intent**, not just keywords.

---

## 🚀 Features

- AI-powered ticket classification
- Machine Learning using Scikit-learn
- Natural Language Processing (TF-IDF)
- Automatic response generation
- Flask web application
- Responsive user interface

---

## 🧠 AI Workflow

User Ticket
↓
Text Preprocessing
↓
TF-IDF Vectorization
↓
Machine Learning Classification
↓
Predicted Category
↓
Suggested Response

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

AI-Ticket-Classifier/

├── app.py

├── train_model.py

├── intents.json

├── model.pkl

├── vectorizer.pkl

├── responses.pkl

├── requirements.txt

├── templates/

│ └── index.html

└── static/

├── style.css

└── script.js

---

## ▶️ Installation

```bash
pip install -r requirements.txt

python train_model.py

python app.py
```

Open:

http://127.0.0.1:5000

---

## 🎯 Sample Prediction

### Input

```
I forgot my password
```

### Output

```
Category:
Password & Login Support

Confidence:
97%

Suggested Response:
Click "Forgot Password" and follow the password reset instructions.
```

---

## 👨‍💻 Author

**Goutham Boini**

GitHub:
https://github.com/gouthamboini09