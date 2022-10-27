from flask import Flask
from .users.routes import user_route

app = Flask(__name__)

# Registering blueprint
app.register_blueprint(user_route)