
from flask.blueprints import Blueprint
from flask import redirect,flash
from flask.globals import request

blueprint = Blueprint('errors', __name__)

@blueprint.app_errorhandler(FileNotFoundError)
def file_notfound_error(e):
    flash('The file specfied could not be found, please ensure the path entered is absolute and the file exists')
    return redirect(request.url)
