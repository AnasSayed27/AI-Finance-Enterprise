# 🏦 Enterprise AI Credit Intelligence & Macro-Risk Engine

---

## 📄 Executive Summary (The White Paper)

### **The Problem: The "Black Box" & Credit Contagion**
In the Indian banking sector, rising **Non-Performing Assets (NPAs)** and the lack of transparency in traditional credit scoring models present a dual risk. Traditional models often fail to capture non-linear relationships in borrower behavior, while complex "Black Box" AI models face rejection from regulators (RBI) due to a lack of interpretability.

### **The Solution: Integrated Decision Intelligence**
This project presents a **Unified AI Finance Engine** that bridges the gap between raw economic data and actionable credit decisions. By utilizing a **Parsimonious 5-Feature Architecture**, we prioritize model stability and regulatory compliance without sacrificing predictive power.

### **Key Achievements**
- **Explainable AI (XAI):** Integrated **SHAP (Shapley Additive Explanations)** to provide a mathematical "Why" for every loan decision, meeting RBI's transparency mandates.
- **Production-Grade Architecture:** Deployed as a containerized **Microservice** using FastAPI and Docker, ensuring sub-second inference latency.
- **Risk-First Engineering:** Optimized the XGBoost pipeline for **High Recall**, prioritizing the detection of potential defaulters to protect bank capital.

---

## 🛠️ Technical Architecture

### **1. The Data Engine (Phase 1)**
- **Macro-Financial Data Lake:** A robust ETL pipeline fetching daily NIFTY 50 prices and global economic indicators (Repo Rates, GDP, Inflation) via `yfinance` and `fredapi`.
- **Statistical Validation:** Implemented **Augmented Dickey-Fuller (ADF)** tests to ensure stationarity in time-series data before feature engineering.

### **2. The Intelligence Layer (Phase 2)**
- **Credit Risk Classifier:** An XGBoost-driven model trained on real-world lending logic.
- **Imbalance Handling:** Utilized `scale_pos_weight` and cost-based thresholding to balance the trade-off between "Lost Opportunity" (False Positives) and "Total Capital Loss" (False Negatives).
- **Portfolio Optimization:** Integration of **Modern Portfolio Theory (MPT)** to allocate capital across assets based on AI-generated signals.

### **3. The Production Stack (Phase 3)**
- **FastAPI:** An asynchronous REST API designed for high-throughput financial queries.
- **Streamlit UI:** A professional dashboard for stakeholders to interact with the models in real-time.
- **Docker-Compose:** Orchestrated multi-container environment ensuring "Environment Parity" from development to production.

---

## 📊 System Performance & KPIs

| Metric | Value | Financial Significance |
| :--- | :--- | :--- |
| **Model Recall (Class 1)** | ~88% | High sensitivity to potential defaulters (NPA Prevention). |
| **Decision Threshold** | 0.20 | Conservative stance to prioritize capital preservation. |
| **Inference Latency** | < 100ms | Real-time decisioning for mobile/web integrations. |
| **Architecture** | Microservice | Independent scaling of Risk and UI components. |

---

## 📸 Visualizing the Intelligence

> **[INSERT_SCREENSHOT_OF_DASHBOARD_HERE]**
> *Figure 1: Unified Stakeholder Dashboard showing Real-time Risk Metrics.*

> **[INSERT_SCREENSHOT_OF_SHAP_PLOT_HERE]**
> *Figure 2: SHAP Waterfall Plot explaining a specific Loan Rejection (RegTech Compliance).*

---

## 🚀 How to Run (Standard Production Build)

This system is containerized for instant deployment. Ensure you have **Docker Desktop** installed.

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/[YOUR_USERNAME]/AI-Finance-Credit-Risk.git
   cd AI-Finance-Credit-Risk

2. **Deploy the Microservices:**
   ```bash
   docker-compose up --build

3. **Access the Interface:**
   - Frontend UI: http://localhost:8501
   - API Documentation (Swagger): http://localhost:8000/docs
  
---

## 👨‍💻 Author & Vision

### Mohammed Anas Sayed  
- AI Engineering Student @ Mumbai University  

Focused on the intersection of Quantitative Finance and Scalable AI Infrastructure.
This project represents a commitment to building transparent, robust, and economically sound financial technology.  

**Connect with me:** [LinkedIn Link] | [Twitter/Portfolio Link]  
