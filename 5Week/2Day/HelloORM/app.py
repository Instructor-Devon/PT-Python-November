from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate			# this is new
app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello_orm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)

class User(db.Model):	
    __tablename__ = "users"    # optional		
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45)) #VARCHAR(45)
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

@app.route("/")
def index():
    # query for all users!
    all_users = User.query.all()
    return render_template("index.html", users=all_users)

@app.route("/create", methods=["POST"])
def create():
    # create a new User object
    new_user = User(
        first_name = request.form["first_name"],
        last_name = request.form["last_name"],
        email = request.form["email"]
    )

    # commit to the db
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")

@app.route("/user/<id>")
def show(id):
    # query for a single user with 'id'
    one = User.query.get(id)
    return render_template("show.html", user=one)

@app.route("/update/<id>", methods=["POST"])
def update(id):
    # query for a single user with 'id'
    one = User.query.get(id)
    one.first_name = request.form["first_name"]
    one.last_name = request.form["last_name"]
    one.email = request.form["email"]
    db.session.commit()
    return redirect(f"/user/{id}")

@app.route("/user/delete/<id>")
def delete(id):
    one = User.query.get(id)
    db.session.delete(one)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)