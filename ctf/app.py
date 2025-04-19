from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

CORRECT_KEY1 = "CTF{Forget CTF, How about a Cup Of Coffee?}"
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/page2.html')
def page2():
    return render_template("page2.html")


@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    user_key = data.get("key", "").strip()

    if user_key == CORRECT_KEY1:
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False})

if __name__ == '__main__':
    app.run(debug=True)
