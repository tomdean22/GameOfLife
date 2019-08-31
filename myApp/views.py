""" file for views that don't require a module """

from flask import render_template, Blueprint
from myApp import app

about_blueprint = Blueprint(name='about',
                            import_name=__name__,
                            static_folder='/static',
                            template_folder='/templates')

@about_blueprint.route('/about')
def about():
    return render_template('about.html')