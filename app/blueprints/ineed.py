from flask import Blueprint, request, jsonify, session
from middlewares.iam import iam
from middlewares.auth import auth

ineed = Blueprint('ineed', __name__, url_prefix='/ineed')


@ineed.route('/')
@auth()
@iam()
def need():
    return 'need';
    

    
    

