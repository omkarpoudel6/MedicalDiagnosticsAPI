from app.core.logic import get_treatment

def test_fever_and_cough():
    symptoms = ["cough", "fever"]
    result = get_treatment(symptoms)
    assert "Flu" in result["Conditions"]
    
def test_unknown_symptom():
    symptoms = ["backpain"]
    result = get_treatment(symptoms)
    assert result["conditions"] == "Unknown"