from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Intelligence API",
    description="Backend API for AI-powered resume analysis",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ai-resume-intelligence",
    }