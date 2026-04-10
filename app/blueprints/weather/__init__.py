from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from app.data_sources.weather import fetch_weather_data

weather_bp = Blueprint('weather_bp', __name__)

@weather_bp.route('/', defaults={'page': 'weather'})
@weather_bp.route('/<page>')
def show(page):
    print(fetch_weather_data(), flush=True)
    try:
        return render_template(f'weather/{page}.html', data=[])
    except TemplateNotFound:
        abort(404)
