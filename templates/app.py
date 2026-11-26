
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json(silent=True) or {}

    if not all(key in data for key in ("latitude", "longitude", "accuracy")):
        return jsonify({"status": "error"}), 400

    print("\n👑 BLACK CROWN ASSISTANT", flush=True)
    print("Visitor shared location with permission", flush=True)
    print("Latitude:", data["latitude"], flush=True)
    print("Longitude:", data["longitude"], flush=True)
    print("Accuracy:", data["accuracy"], "meters", flush=True)

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
