from sqlalchemy.sql import func
from config import db, ma



class Dog(db.Model):	

    __tablename__ = "dogs"    # optional		
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    breed = db.Column(db.String(45))
    weight = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    @classmethod
    def validate(cls, form):
        '''
            Returns: [list, of, errors]
        '''
        errors = []

        if len(form['name']) < 2:
            errors.append("Name must be at least 2 characters")
            valid = False

        if len(form['breed']) < 2:
            errors.append("Breed must be at least 2 characters")
            valid = False

        try:
            if int(form["weight"]) < 1:
                errors.append("Invalid weight")
                valid = False
        except ValueError:
            errors.append("Invalid weight")

        return errors

    @classmethod
    def create(cls, form):
        new_dog = Dog(
            name = form["name"],
            breed = form["breed"],
            weight = form["weight"]
        )
        db.session.add(new_dog)
        db.session.commit()
        return new_dog
    
    def __repr__(self):
        return f"<Dog: {self.name}>"

class DogSchema(ma.ModelSchema):
    class Meta:
        model = Dog