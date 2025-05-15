# Configuration and Setup Notes

## Environment Variables

The application uses environment variables to configure settings, loaded from a `.env` file.

### Example `.env` file:

APP_Name = Medical Diagnostics
ENV = development
PORT = 8000

## How Configuration Works

- These variables are accessed via Pydantic's `BaseSettings` in `app/core/config.py`.
- You can modify `.env` to adjust configurations for different environments (development, staging, production).

## Running Tests

Tests use `pytest`. Run them with:

```bash
pytest
