from config import app
from controller_functions import index, create, fetch_dogs

app.add_url_rule("/", view_func=index)
app.add_url_rule("/create", methods=["POST"], view_func=create)
app.add_url_rule("/dogs", view_func=fetch_dogs)