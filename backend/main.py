from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.tasks import router as tasks_router
import uvicorn
import os

app = FastAPI(
    title="Todo API",
    description="A REST API for managing todo tasks",
    version="1.0.0"
)

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(tasks_router, prefix="/api", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Todo API is running on Hugging Face Spaces"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "Todo API is operational"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)