from flask import Flask, render_template, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from validations.validators import validate
import re
# from app import User
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_dash.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "LOL"

bcrypt = Bcrypt(app)

# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)

# some_user.posts => [Post, Post]
class User(db.Model):	
    __tablename__ = "users"    # optional		
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    #posts

    def __repr__(self):
        return f"<User: {self.email}>"

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = db.relationship('User', foreign_keys=[author_id], backref="posts", cascade="all")
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Post: \"{self.content[:5]}...\">"

@app.route("/")
def index():
    return render_template("index.html", users=User.query.all())

@app.route("/users/create", methods=["POST"])
def register():
    errors = []

    if len(request.form['first_name']) < 2:
        errors.append("First name must be at least 2 characters")
        valid = False

    if len(request.form['last_name']) < 2:
        errors.append("Last name must be at least 2 characters")
        valid = False

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append("Email must be valid")
        valid = False

    if len(request.form['password']) < 8:
        errors.append("Password must be at least 8 characters")
        valid = False

    #TODO: Validate email is unique
    user_check = User.query.filter_by(email=request.form["email"]).first()
    if user_check is not None:
        errors.append("Email is in use")
    
    if request.form['password'] != request.form['confirm']:
        errors.append("Passwords must match")
        valid = False

    if errors:
        for e in errors:
            flash(e)
    else:
        hashed = bcrypt.generate_password_hash(request.form["password"])
        new_user = None
        #TODO: Create New User
        new_user = User(
            first_name = request.form["first_name"],
            last_name = request.form["last_name"],
            email = request.form["email"],
            password = hashed
        )
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
        return redirect("/dashboard")

    return redirect("/")

@app.route("/users/login", methods=["POST"])
def login():
    errors = []

    user_attempt = User.query.filter_by(email=request.form["email"]).first()
    #TODO: Query for user wiith provided email
    
    if not user_attempt:
        flash("Email/Password Incorrect")
        return redirect("/")

    if not bcrypt.check_password_hash(user_attempt.password, request.form["password"]):
        flash("Email/Password Incorrect")
        return redirect("/")

    session["user_id"] = user_attempt.id
    return redirect('/dashboard')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    # get user from session
    if not "user_id" in session:
        return redirect("/")
    
    logged_in = User.query.get(session["user_id"])
    #TODO: Query for user with session id

    all_posts = Post.query.all()
    #TODO: Query for all posts, ordered by the most recent


    return render_template("dashboard.html", user=logged_in, posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)