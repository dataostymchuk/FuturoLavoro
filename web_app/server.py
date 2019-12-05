import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello():
	data = request.get_json(force=True)
	data = json.loads(data)
	return data['text']

if __name__ == "__main__":
    app.run(debug=True)