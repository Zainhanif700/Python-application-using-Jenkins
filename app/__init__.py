from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return "Hello, Jenkins CI/CD with Flask!"

    return app
