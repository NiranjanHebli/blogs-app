from typing import List
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str



class User(BaseModel):
    name: str
    email: str
    password: str

class ShowCreator(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    blogs :List[Blog]
    class Config:
        orm_mode = True

class ShowBlog(Blog):
    id: int
    creator: ShowCreator
    class Config:
        orm_mode = True

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str