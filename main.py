from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    id: int
    title: str
    body: str
    published : Optional[bool] 


blogs = []

@app.get("/")
def index():
    # This is the root endpoint (can be named anything apart from index)
    return {"data": "blog-list"}
@app.post('/blog')
def create_blog(blog: Blog):
    # This is the endpoint to create a blog
    blogs.append(blog)
    return {"data": f"blog created with title {blog.title}"}

@app.get('/blog')
def get_blogs(limit:int=10, published:bool=True):
    my_blogs = [x for x in blogs if x.published == published]
    if published:
        return {"data": f"list of {limit} published blogs",
                "blogs": my_blogs[:limit]}
    else:
        return {"data": f"list of {limit} blogs"}

@app.get('/blog/unpublished')
def get_unpublished_blogs():
    return {"data": "unpublished blogs"}
@app.get('/blog/{id}')
def get_blog(id:int):
    return {"data": f"blog with id {id}"}

@app.get('/blog/{id}/comments')
def get_blog_comments(id:int):
    return {"data": f"comments for blog with id {id}"}