from flask import Flask
from flask_cors import CORS
from .users.routes import user_route
from .calculations.routes import calculation_route

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

# Registering blueprint
app.register_blueprint(user_route)
app.register_blueprint(calculation_route, url_prefix='/calculate')