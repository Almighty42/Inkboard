from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

weather_bp = Blueprint('weather_bp', __name__)

@weather_bp.route('/', defaults={'page': 'weather'})
@weather_bp.route('/<page>')
def show(page):
    try:
        return render_template(f'weather/{page}.html')
    except TemplateNotFound:
        abort(404)
