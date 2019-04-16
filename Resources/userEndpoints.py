import sqlite3
from flask_restful import Resource,reqparse

from Models.userModels import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type = str,
        required = True,
        help = "This field cannot be blank"
    )
    parser.add_argument(
        "password",
        type = str,
        required = True,
        help = "This field cannot be blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message":"A User with that username already exists"},400


        user = UserModel(**data)#(data["username"],data["password"])
        user.save_to_db()

        return {"message":"User created successfully"},201