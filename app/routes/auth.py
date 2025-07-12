from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.schemas import user as user_schema, token as token_schema
from app.crud import user as user_crud
from app.dependencies import get_db
from app.utlis import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# ✅ JSON-based register endpoint (used by APIs)
@router.post("/register", response_model=user_schema.UserOut)
def register(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return user_crud.create_user(db=db, user=user)

# ✅ JSON-based login (for APIs or future React apps)
@router.post("/login", response_model=token_schema.Token)
def login(user: user_schema.UserLogin, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_username(db, user.username)
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

# ✅ HTML form-based login (for your login.html form)
@router.post("/login-form")
def login_form(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    db_user = user_crud.get_user_by_username(db, username)
    if not db_user or not verify_password(password, db_user.password_hash):
        return HTMLResponse(
            content="<h3>Invalid credentials</h3><a href='/login'>Try again</a>",
            status_code=401
        )

    # Login success — you could set session/cookie here
    token = create_access_token(data={"sub": db_user.username})
    # You can store token in session or show message
    return RedirectResponse(url="/", status_code=302)
