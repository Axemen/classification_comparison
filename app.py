from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route("/test")
def test(model):
    return jsonify({
        "test":'test'
    })

if __name__ == "__main__":
    app.run(debug=True)

