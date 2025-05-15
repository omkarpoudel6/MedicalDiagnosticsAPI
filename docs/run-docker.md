# Running the Project Using Docker

## Prerequisites

- Docker installed and running
- (Optional) Docker Compose installed

## Steps

### Build the Docker image:
- docker build -t disease-checker .

### Run the Docker COntainer:
- docker run -d -p 8000:8000 --env-file .env disease-checker

### Access the API
- Open your browser and go to: http://localhost:8000/docs
    
### Test the API via curl
- curl -X POST http://localhost:8000/api/v1/diagnose \ -H "Content-Type: application/json" \ -d '{"symptoms": ["fever", "cough"]}'

## Stopping the Container

### Find the container ID
- docker ps

### Stop the container:
- docker stop <container_id>

