from flask_restful import Resource,reqparse
from flask_jwt_extended import (
                                create_access_token,
                                create_refresh_token,
                                jwt_refresh_token_required,
                                get_jwt_identity,
                                get_raw_jwt,
                                jwt_required
                                )
from Models.userModels import UserModel
from blacklist import BLACKLIST

#private variable and shouldnt be imported from somewhere else
_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
        "username",
        type = str,
        required = True,
        help = "This field cannot be blank"
    )
_user_parser.add_argument(
        "password",
        type = str,
        required = True,
        help = "This field cannot be blank"
    )


class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message":"A User with that username already exists"},400


        user = UserModel(**data)#(data["username"],data["password"])
        user.save_to_db()

        return {"message":"User created successfully"},201


class User(Resource):

    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return{"message":"User not found"}
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return{"message":"User not found"}
        user.delete_from_db()
        return {"message":"user deleted"}


class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data["username"])

        if user and (user.password,data["password"]):
            access_token = create_access_token(identity = user.id, fresh = True)
            refresh_token = create_refresh_token(user.id)

            return {
                    "access_token":access_token,
                    "refresh_token":refresh_token
                }
        return{"message":"Invalid Credentials"},401

class UserLogout(Resource):
    @jwt_required
    def post(self):
        # unique identifier for jwt
        jti = get_raw_jwt()["jti"]
        BLACKLIST.add(jti)
        return {"message":"Successfully logged out."},200

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token":new_token}