from flask import render_template, redirect, request, flash, session, get_flashed_messages, jsonify
import json
from models import Dog, DogSchema
from config import db

def index():
    return render_template("index.html")

def create():
    print(request.form)
    if len(request.form["name"]) < 1:
        flash("Name fields are required", category="name")
        flash("Dont be a dingus", category="name")
    errors = get_flashed_messages(with_categories=True)
    if errors:
        print(json.dumps(errors))
        return jsonify(errors=errors)

    else:
        new_dog = Dog.create(request.form)
        db.session.add(new_dog)
        db.session.commit()
    return redirect("/")

def fetch_dogs():
    return render_template("dogs_partial.html", dogs=Dog.query.all())

def fetch_dogs_json():
    dogs = Dog.query.all()
    dog_schema_many = DogSchema(many=True)
    # dog_schema_one = DogSchema()
    many_dogs = dog_schema_many.dump(dogs)
    # dog = Dog.query.first()
    # one_dog = dog_schema_one.dump(dog)
    # one_dog = dog_schema_one.dump(dog).data
    payload = {
        "dogs": many_dogs
    }
    return jsonify(payload)