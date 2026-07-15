import json
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

texts = []
labels = []

responses = {}

for intent in data["intents"]:
    responses[intent["tag"]] = intent["response"]

    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

# Vectorize
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

# Train Model
model = LogisticRegression()

model.fit(X, labels)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(responses, open("responses.pkl", "wb"))

print("Model Trained Successfully!")