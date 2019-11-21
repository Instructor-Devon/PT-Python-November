from flask import render_template, redirect, request, flash, session, jsonify, get_flashed_messages
import json
from models import Dog, DogSchema
from config import db

def index():
    return render_template("index.html")

def fetch_dogs():
    return render_template("dogs.html", dogs=Dog.query.all())

def test_api():
    my_data = {
        "first_name": "Devon",
        "last_name": "Newsom"
    }
    return jsonify(my_data)
def create():

    if len(request.form['name']) < 1:
        flash("Name field is required", category="name")
    
    if len(request.form['breed']) < 1:
        flash("Breed field is required", category="breed")

    if len(request.form['weight']) < 1:
        flash("Weight field is required", category="weight")

    errors = get_flashed_messages(with_categories=True)
    print(errors)

    if errors:
        # return errors as json
        return jsonify({
            "errors": errors
        })
    
    new_dog = Dog.create(request.form)
    # db.session.add(new_dog)
    # db.session.commit()
    return redirect("/dogs")

# get one
def dog_json(id):
    my_dog = Dog.query.get(id)
    dog_schema = DogSchema()
    data = dog_schema.dump(my_dog)
    return jsonify(data)

# get many
def dogs_json():
    dogs = Dog.query.all()
    dog_schema = DogSchema(many=True)
    data = dog_schema.dump(dogs)
    return jsonify(data)