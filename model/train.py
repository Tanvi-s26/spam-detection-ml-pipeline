import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os
import mlflow
import mlflow.sklearn

# Ensure correct path for saving model
os.makedirs("app", exist_ok=True)

# Step 1: Dataset
data = {
    "text": [
        "Free money now",
        "Win cash prize",
        "Claim your reward",
        "Hi how are you",
        "Let's meet tomorrow",
        "Are you coming today"
    ],
    "label": [1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

# Step 2: Text → Numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

# Step 3: 

with mlflow.start_run():

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["text"])

    model = MultinomialNB()
    model.fit(X, df["label"])

    # Log model
    mlflow.sklearn.log_model(model, "model")

    # Log parameter
    mlflow.log_param("model_type", "MultinomialNB")

    # Save model locally also
    with open("app/model.pkl", "wb") as f:
        pickle.dump((model, vectorizer), f)

    print("Model trained & logged with MLflow")
# Step 4: Save Model
with open("app/model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("✅ Model trained & saved at app/model.pkl")