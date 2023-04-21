from main.controller.upload import *
from main import app
from sqlalchemy import text

@app.route('/get-img/<id>',methods=['GET'])
def getImg(id):
    
    imgs = db.session.execute(text("select * from imageuploads where idUser={}".format(id)))
    data=[]
    for img in imgs:
        
        img_parse = {}
        img_parse["link"]=img.link
        img_parse["upload_at"]=str(img.createAt)
        img_parse["detail"]=img.detail
        data.append(img_parse)
    return {"data":data}
