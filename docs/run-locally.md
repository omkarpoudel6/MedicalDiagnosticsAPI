# Running the Project Locally

## Prerequisites

- Python 3.11+
- Pip
- Virtualenv (recommended)

## Steps

### Clone the repository:

- git clone https://github.com/omkarpoudel6/MedicalDiagnosticsAPI
- cd MedicalDiagnosticsAPI

### Create and activate virtual environment

- python -m venv myenv
- source venv/bin/activate # Linux/macOS
- venv\Scripts\activate # Windows

### Install dependencies

- pip install -r requirements.txt

### Run the FastAPI server:

- uvicorn.app.main:app --reload

### Open your browser 

- Navigate to http://localhost:8000/docs to access Swagger UI and test the API

### Test the API with curl

- curl -X POST http://localhost:8000/api/v1/diagnose \ -H "Content-Type: application/json" \ -d '{"symptoms": ["fever", "cough"]}'
