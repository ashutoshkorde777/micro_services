# README.md
# Subscription Service Microservice

## Features
- JWT-based Authentication
- Subscription Plan Management
- User Subscription Management
- RESTful APIs

## Setup Instructions
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file with DB credentials and secret key.
4. Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```
