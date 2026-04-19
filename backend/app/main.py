from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import interview

app = FastAPI(title="AI Tutor Screener")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend requests
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interview.router)

@app.get("/")
def home():
    return {"message": "AI Tutor Screener API running"}