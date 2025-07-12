from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

import os

from app.database import Base, engine
from app.routes import auth, items, swaps
from app.models import user, item, swap

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(
    title="ReWear Backend API",
    version="1.0.0",
    description="Backend service for the ReWear platform"
)

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000/"],  # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include route modules
app.include_router(auth.router)
app.include_router(items.router)
app.include_router(swaps.router)

# ✅ Serve static assets (CSS, JS, images, etc.)
app.mount("/static", StaticFiles(directory="app/static/src"), name="static")

# ✅ Jinja2 Template Setup for HTML files
templates = Jinja2Templates(directory="app/static/views")

# ✅ Route: Home Page (index.html)
@app.get("/", response_class=FileResponse)
def get_home():
    return FileResponse("app/static/index.html")

# ✅ Route: Login Page
@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("templates/auth/login.html", {"request": request})

# ✅ Route: Register Page
@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("templates/auth/register.html", {"request": request})
