from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(
        status="up",
        maintainer="Sayantan"
    )

@app.route("/")
def home():
    return "<b> Welcome to my project!! </b> <br/>"
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
