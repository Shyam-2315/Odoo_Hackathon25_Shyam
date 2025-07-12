from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

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

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve XML or landing HTML file
@app.get("/", response_class=FileResponse)
def root():
    return FileResponse(os.path.join("static", "src", "views", "templates.xml"))
    # If using HTML instead of XML:
    # return FileResponse(os.path.join("static", "src", "views", "index.html"))
