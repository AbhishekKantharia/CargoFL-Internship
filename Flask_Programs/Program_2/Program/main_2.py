from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
	def get(self):
		data={"data":"Hello World"}
		return data

api.add_resource(HelloWorld,'/hello')


if __name__=='__main__':
	from waitress import serve
	serve(app, host="0.0.0.0", port=8080)
	app.run(debug=True)