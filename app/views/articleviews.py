from fastapi import APIRouter, Depends,Request
from sqlalchemy import select
from sqlalchemy import Session

from app.core.database import get_db
from app.models.article import Article

article_views = APIRouter()

@article_views.get("/article/create",include_in_schema=False)
async def article_create(request:Request, db:Session = Depends(get_db)):
    article = Article(title="Test Title", content="Content Here")
    db.add(article)
    db.commit()
    db.resfresh(article)
