# from flask import Blueprint, render_template, abort
# from jinja2 import TemplateNotFound
#
# weather_bp = Blueprint('weather_bp', __name__, template_folder='templates')
#
# @weather_bp.route('/', defaults={'page': 'index'})
# @weather_bp.route('/<page>')
# def show(page):
#     try:
#         return render_template(f'pages/{page}.html')
#     except TemplateNotFound:
#         abort(404)
#
# return weather_bp
