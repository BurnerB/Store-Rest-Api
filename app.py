from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from Resources.userEndpoints import UserRegister
from Resources.ItemEndpoints import Item,ItemList
from Resources.storeEndpoints import Store,StoreList


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #Turn ff flask sqalchemy modification tracker
api = Api(app)
app.secret_key = "BABA"

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app,authenticate,identity) # /auth


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister,"/register")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    #Prevent circular imports
    app.run(port=5000, debug =True)
