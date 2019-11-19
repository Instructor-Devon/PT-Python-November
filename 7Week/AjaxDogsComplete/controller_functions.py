from flask import render_template, redirect, request, flash, session
from models import Dog
from config import db

def index():
    return render_template("index.html")

def create():
    print(request.form)
    new_dog = Dog.create(request.form)
    db.session.add(new_dog)
    db.session.commit()
    return redirect("/")

def fetch_dogs():
    return render_template("dogs_partial.html", dogs=Dog.query.all())