\# Spam Detection ML Pipeline



\## 📌 Problem Statement

Build a machine learning model to classify messages as Spam or Not Spam.



\## ⚙️ Day 1 Progress

\- Created structured ML project

\- Implemented text preprocessing using CountVectorizer

\- Trained Naive Bayes model

\- Saved model as pickle file for future deployment



\## 🧠 Tech Stack

\- Python

\- scikit-learn

\- pandas



\## 📂 Project Structure

\- model/ → training logic

\- app/ → (API will be added later)



\## 🚀 Next Step

Expose model via Flask API



\## Day 2 Progress

\- Built Flask API

\- Created /predict endpoint

\- Integrated ML model into API



\## API Usage



POST /predict



Request:

{

&#x20; "text": "Win money"

}



Response:

{

&#x20; "prediction": "Spam"

}



\## Day 3 Progress

\- Dockerized the Flask API

\- Created Dockerfile

\- Ran containerized application



\## Run with Docker



docker build -t spam-detection-app .

docker run -p 5000:5000 spam-detection-app





\## Day 4 Progress

\- Deployed ML API to cloud

\- Live endpoint available

