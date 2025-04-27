from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    # This is the root endpoint (can be named anything apart from index)
    return {"data": "blog-list"}

@app.get("/blog/{id}")
def get_blog():
    return {"data": f"blog with id {id}"}

