from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    print("Rendering home template")
    return render_template("homework1.html")

if __name__ == "__main__":
    app.run(debug=True)
