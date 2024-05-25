from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models import Base, Joke, User
from database import engine, get_db
from auth import get_current_user
import random

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": "blob", "token_type": "bearer"}

async def authenticate_user(db: Session, username: str, password: str):
    user = await db.execute(select(User).where(User.username == username))
    user = user.scalar()
    if not user or not user.verify_password(password):
        return False
    return user

@app.get("/jokes/random", response_model=None, dependencies=[Depends(oauth2_scheme)])
async def get_random_joke(db: Session = Depends(get_db)):
    result = await db.execute(select(Joke))
    jokes = result.scalars().all()
    if not jokes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No jokes found")
    return random.choice(jokes)

@app.post("/jokes", response_model=None, dependencies=[Depends(oauth2_scheme)])
async def create_joke(joke: Joke, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    db.add(joke)
    await db.commit()
    await db.refresh(joke)
    return joke

# Lifespan event handler for startup and shutdown tasks
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield
    
    # Shutdown actions
    await engine.dispose()

app.router.lifespan_context = lifespan

