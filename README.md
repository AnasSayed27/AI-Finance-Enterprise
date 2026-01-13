# 🏦 Enterprise AI for Credit Risk & Decision Intelligence

### **Project Pitch**
A Production-Grade Credit Risk Intelligence System built for the Indian FinTech landscape. I implemented an explainable XGBoost pipeline with SHAP to meet RegTech transparency standards, achieving high recall for default detection to prioritize capital protection. The entire engine is architected as a containerized Microservice using FastAPI and Docker for scalable, high-speed financial decision-making.

## 🛠️ Tech Stack
- **Model:** XGBoost Classifier (Scikit-Learn Pipeline)
- **Interpretability:** SHAP (Shapley Additive Explanations)
- **API:** FastAPI (Asynchronous Python)
- **Frontend:** Streamlit
- **DevOps:** Docker & Docker-Compose

## 🚀 How to Run (Production Mode)
Ensure you have Docker installed, then run:
`docker-compose up --build`

## 📈 Financial Impact
- **Risk Mitigation:** Optimized for High Recall to reduce Non-Performing Assets (NPAs).
- **Compliance:** Includes a SHAP-based waterfall plot logic to explain "Loan Rejections" to regulators.
