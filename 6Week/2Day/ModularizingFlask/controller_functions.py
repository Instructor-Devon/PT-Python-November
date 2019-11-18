from flask import render_template, redirect, request, flash, session
from models import Dog
from config import db

def index():
    return render_template("index.html", dogs=Dog.query.all())

def create():
    
    errors = Dog.validate(request.form)

    if errors:
        for e in errors:
            flash(e)
    else:
        new_dog = Dog.create(request.form)
        print(new_dog.name)
        return redirect("/")

    return redirect("/")