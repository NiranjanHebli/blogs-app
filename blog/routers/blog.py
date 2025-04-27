from blog import oauth2
from fastapi import APIRouter, Depends, status
from typing import List
from .. import schemas
from ..database import get_db
from ..repository import blog
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = "/blog",
    tags=["blogs"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(db, request)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete(db, id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(
    id: int, request: schemas.Blog, db: Session = Depends(get_db)
):
    return blog.update(db, id, request)


@router.get("", response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    return blog.get_by_id(db, id)
