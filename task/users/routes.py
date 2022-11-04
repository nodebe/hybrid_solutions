from flask import Blueprint

user_route = Blueprint('users', __name__)

@user_route.get('/')
def index():
    my_info = {
        "slackUsername": "KayKay",
        "backend": True,
        "age": 24,
        "bio": "I'm a software engineer who writes clean, testable, scalable, and maintainable code. A good teammate and lover of learning new things to develop daily."
    }

    return my_info
