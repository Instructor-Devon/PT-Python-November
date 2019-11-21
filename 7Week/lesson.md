# Week 7 Session 2: APIs and json
### Summary: 
By returning json from our Flask AKA Server applications, we can build a standalone Server Application that can be used by ANY Client (web,mobile,desktop,etc)

Step 1) Return jsonified data from our Flask app.  Flash messages, for example.

Step 2) Allow our Model classes to be serialized into the correct json format
- new pip packages:
```bash
pip install flask-marshmallow
pip install marshmallow-sqlalchemy
```
- Set up new Schema classes for each of our Models
- Serialize our queries to json, return as server response