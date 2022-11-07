from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "Hello World"}
		return jsonify(data)


if __name__ == '__main__':
	from waitress import serve
	serve(app, host="0.0.0.0", port=8080)
	app.run(debug=True)