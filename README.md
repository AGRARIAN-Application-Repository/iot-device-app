# iot-device-app

Agrarian iot-device-app Application

## Description

This is a simple FastAPI application for the Agrarian ecosystem.

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python src/app.py
```

## Docker

```bash
# Build the image
docker build -t iot-device-app .

# Run the container
docker run -p 80:80 iot-device-app
```

## CI/CD

This repository uses a simple CI/CD pipeline that:
- Tests application compilation
- Checks for hardcoded secrets
- Builds Docker image
- Pushes to GitHub Container Registry
- Tests the Docker image

## Endpoints

- `GET /` - Main endpoint
- `GET /health` - Health check
