from fastapi import FastAPI
from app.routes import auth, items, swaps, admin
from app.database import engine, Base
from app.models import user, item, swap  # Ensure models are imported

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(swaps.router, prefix="/swaps", tags=["Swaps"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def read_root():
    return {"message": "Welcome to ReWear API"}
