from flask import Blueprint, request, jsonify, session

account = Blueprint('account', __name__, url_prefix='/account')


@account.route('/login')
def login():
    return 'login';
    
    
@account.route('/register')
def register():
    return 'register';
    
    
    

