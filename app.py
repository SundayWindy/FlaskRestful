from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)


class Test(Resource):
    def get(self,user_id):
        return {"key": 200}, 200


api = Api(app)
api.add_resource(Test, "/<string:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
