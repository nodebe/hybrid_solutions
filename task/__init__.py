from flask import Flask
from .users.routes import user_route

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Registering blueprint
app.register_blueprint(user_route)