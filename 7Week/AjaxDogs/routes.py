from config import app
from controller_functions import index, create, fetch_dogs, dog_json, dogs_json

app.add_url_rule("/", view_func=index)
app.add_url_rule("/dogs", view_func=fetch_dogs)
app.add_url_rule("/api/dog/<id>", view_func=dog_json)
app.add_url_rule("/api/dog", view_func=dogs_json)
app.add_url_rule("/create", methods=["POST"], view_func=create)