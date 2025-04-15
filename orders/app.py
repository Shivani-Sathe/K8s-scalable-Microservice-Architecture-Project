from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/orders", methods=["GET"])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
