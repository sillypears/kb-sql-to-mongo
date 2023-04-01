

from flask import (Blueprint, Flask, jsonify, make_response, redirect,
                   render_template, request, send_file, url_for,)

from ..extentions import db


utils = Blueprint('utils', __name__, url_prefix="/utils")
                 
@utils.route("/", methods=["GET"])
def util_home():
  return {'msg': 'some utility functions'}