🧠 Spam Detection ML Pipeline



\---



📌 Project Overview



This project demonstrates an end-to-end Machine Learning pipeline where a spam detection model is:



* Trained using NLP techniques
* Exposed via a REST API
* Containerized using Docker
* Deployed to the cloud
* Tracked using MLflow



\---



🚀 Live Demo



👉 https://spam-detection-ml-pipeline.onrender.com/



\---



🏗️ Architecture

User → API (Flask) → ML Model → Prediction → Response

&#x20;            ↓

&#x20;        Docker Container

&#x20;            ↓

&#x20;        Cloud Deployment



\---



⚙️ Tech Stack



* Python
* scikit-learn
* Flask
* Docker
* MLflow
* Render (Deployment)



\---



📂 Project Structure



spam-detection-ml-pipeline/

│

├── app/

│   ├── app.py

│   └── model.pkl

│

├── model/

│   └── train.py

│

├── requirements.txt

├── Dockerfile

└── README.md



\---



🐳 Run with Docker

docker build -t spam-detection-app .

docker run -p 5000:5000 spam-detection-app

📊 MLflow Tracking



\---



This project uses MLflow to:



Track experiments

Log parameters

Store model artifacts



\---



!\[CI](https://github.com/Tanvi-s26/spam-detection-ml-pipeline/actions/workflows/ci-cd.yml/badge.svg)

