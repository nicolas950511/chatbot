from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)  # Esto permitirá todas las solicitudes CORS

@app.route('/')
def index_get():
    return render_template('index.html')

@app.post('/predict')
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"Respuesta": response}
    return jsonify(message), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True)
