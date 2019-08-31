from flask import Blueprint, render_template, redirect, url_for
from jinja2 import TemplateNotFound
from myApp import db

play_blueprint = Blueprint(name='play',
                           import_name=__name__,
                           template_folder='templates/arena')

@play_blueprint.route('/play')
def play():
    return render_template('arena.html')