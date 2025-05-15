import json
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent.parent / "data/symptoms_db.json"

with open(DB_PATH, "r") as file:
    symptom_data = json.load(file)
    
def get_treatment(symptoms: list[str]) -> dict:
    key = ",".join(sorted(symptoms))
    match = symptom_data.get(key)
    if match:
        return match
    else:
        return {"conditions":["Unknown"],
                "treatments":["Consult a doctor"],
                "medicines":[]}