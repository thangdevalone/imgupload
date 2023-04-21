from main import app,db

from flask import jsonify, make_response, request
from main.model.ImgUpload import ImageUpload

@app.route('/')
def hello():
    return "Api is running"

@app.route('/upload/<id>',methods=['POST'])
def post_img(id):
    if(request.method=="POST"):
        try:
            data=request.json
            upload=""
            if("detail" in data ):
                upload=ImageUpload(idUser=id,link=data["link"],detail=data["detail"])
            else:
                upload=ImageUpload(idUser=id,link=data["link"])
            db.session.add(upload)
            db.session.commit()
            return {"status":200,"message":"Upload image successfully"}
        except:
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)
        
@app.route('/upload-muti/<id>',methods=['POST'])
def post_muti_img(id):
    if(request.method=="POST"):
        try:
            data=request.json
            upload=""
        
            for link in data["data"]:

                if("detail" in link):
                    upload=ImageUpload(idUser=id,link=link["link"],detail=link["detail"])
                else:
                    upload=ImageUpload(idUser=id,link=link["link"])
                db.session.add(upload)
            db.session.commit()
            return {"status":200,"message":"Upload muti image successfully"}
        except:
            return make_response(jsonify({'status': 400, 'message': 'Request fail. Please try again'}), 400)