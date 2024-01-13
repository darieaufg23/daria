from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return f"Method POST, value{user}"
    else:
        user = request.args.get("name")
        return f"Method GET, value {user}"
def main():
    app.run()
if __name__=="__main__":
    main()