from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")
    try:
        # Evaluate expression safely
        result = str(eval(expression, {"__builtins__": None}, {}))
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": "Error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
