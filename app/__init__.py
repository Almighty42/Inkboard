from flask import Flask
# from app.blueprints.weather import weather_bp
# from app.blueprints.agenda import agenda_bp

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # app.register_blueprint(weather_bp)
    # app.register_blueprint(agenda_bp)

    return app
