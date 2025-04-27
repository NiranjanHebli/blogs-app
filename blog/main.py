from typing import List
from blog.routers import blog,user,authentication
from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas, models
from .hashing import Hash
from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)