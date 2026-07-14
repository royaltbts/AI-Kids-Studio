from fastapi import FastAPI
from backend.app.api.routes.system import router as system_router
from backend.app.api.routes.health import router as health_router
from backend.app.api.routes.story import router as story_router

app = FastAPI(
    title="TinyVerse Kids Studio",
    version="1.0.0",
    description="AI-powered platform for creating educational kids videos",
)

app.include_router(health_router)
app.include_router(story_router)
app.include_router(system_router)

@app.get("/")
def root():
    return {
        "project": "TinyVerse Kids Studio",
        "status": "Running 🚀",
        "version": "1.0.0",
    }