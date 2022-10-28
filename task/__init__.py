from flask import Flask
from flask_cors import CORS
from .users.routes import user_route

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

# Registering blueprint
app.register_blueprint(user_route)