from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ajax/post", methods=["POST"])
def form_submission():
    print(request.form)
    return render_template("ajax.html")

@app.route("/ajax")
def do_stuff():
    things = ["one", "two", "three"]
    return render_template("ajax.html", things=things)

if __name__ == "__main__":
    app.run(debug=True)