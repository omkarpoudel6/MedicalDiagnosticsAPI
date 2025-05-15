from fastapi import APIRouter
from pydantic import BaseModel
from app.core.logic import get_treatment

router = APIRouter()

class SymptomRequest(BaseModel):
    symptoms: list[str]
    
@router.post("/diagnose")
def diagnose(request: SymptomRequest):
    result = get_treatment(request.symptoms)
    return {"imput_symptoms":request.symptoms, **result}