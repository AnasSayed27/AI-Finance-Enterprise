from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "credit_risk_pipeline.joblib")

try:
    model_pipeline = joblib.load(MODEL_PATH)
except Exception as e:
    model_pipeline = None
    print(f"FAILED TO LOAD MODEL AT {MODEL_PATH}: {e}")

app = FastAPI(title="Bank of Mumbai: AI Credit Engine (Parsimonious V3)")

class LoanApplicant(BaseModel):
    person_income: float = Field(..., gt=0, description="Your annual gross income in INR", example=500000)
    loan_amnt: float = Field(..., gt=0, description="The total amount you wish to borrow", example=50000)
    loan_percent_income: float = Field(..., ge=0, le=1, description="Loan amount divided by annual income (e.g., 0.15 for 15%)", example=0.10)
    person_home_ownership: str = Field(..., description="Your housing status: 'RENT', 'OWN', or 'MORTGAGE'", example="OWN")
    cb_person_default_on_file: str = Field(..., description="Have you ever defaulted before? 'Y' or 'N'", example="N")

@app.get("/health")
def health_check():
    return {"status": "Server is Live", "model_loaded": model_pipeline is not None}

@app.post("/predict-credit-risk")
async def predict(applicant: LoanApplicant):
    if not model_pipeline:
        raise HTTPException(status_code=503, detail="Model pipeline not loaded.")

    input_df = pd.DataFrame([applicant.dict()])

    try:
        prob_default = float(model_pipeline.predict_proba(input_df)[0][1])
        decision = "Reject" if prob_default > 0.20 else "Approve"
        
        return {
            "probability_of_default": round(prob_default, 4),
            "decision": decision,
            "policy_reference": "RBI FREE-AI Framework 2025: Understandable by Design",
            "next_steps": "Please proceed to document verification if Approved."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))