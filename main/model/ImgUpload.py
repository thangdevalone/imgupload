from main import db
from sqlalchemy import Column,Integer,DateTime,Text

from sqlalchemy.sql import func
class ImageUpload(db.Model):
    __tablename__ = 'imageuploads'
    id=Column(Integer,primary_key=True,autoincrement=True)
    link=Column(Text,nullable=False)
    idUser=Column(Integer,)
    detail=Column(Text,nullable=True)
    createAt=Column(DateTime(timezone=True),default=func.now())
    
   