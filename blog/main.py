from fastapi import FastAPI,Depends,status,Response
from . import schemas
from . import models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,response:Response,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"Blog with id {id} not found"}
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id {id} deleted"}

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int,request: schemas.Blog, response:Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"Blog with id {id} not found"}
    blog.update(request.dict())
    db.commit()
    return {"detail": f"Blog with id {id} updated"}

@app.get('/blog')
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def get_blog(id:int,response:Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"Blog with id {id} not found"}
    return blog