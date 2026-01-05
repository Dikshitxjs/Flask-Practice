from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
api = Api(app)

app.config["JWT_SECRET_KEY"] = "my-key"
jwt = JWTManager(app)


class Login(Resource):
    def post(self):
        data = request.get_json()

        if data["username"] == "admin" and data["password"] == "2468":
            token = create_access_token(identity=data["username"])
            return {"access_token": token}, 200

        return {"msg": "invalid credentials"}, 401


api.add_resource(Login, "/login")


if __name__ == "__main__":
    app.run(debug=True)
