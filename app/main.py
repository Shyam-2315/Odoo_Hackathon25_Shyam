from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, items, swaps
from app.models import user, item, swap  # Ensure models are loaded so tables are created

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ReWear Backend API",
    version="1.0.0",
    description="Backend service for the ReWear platform"
)

# Include route modules
app.include_router(auth.router)
app.include_router(items.router)
app.include_router(swaps.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "ReWear Backend API is running."}
