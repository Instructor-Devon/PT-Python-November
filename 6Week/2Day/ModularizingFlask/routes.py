from config import app
from controller_functions import index, create

app.add_url_rule("/", view_func=index)
app.add_url_rule("/create", methods=["POST"], view_func=create)