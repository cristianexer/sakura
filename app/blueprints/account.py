from sanic import Blueprint
from sanic.response import json

account = Blueprint('account', url_prefix='/account')


@account.route('/login')
def login(request):
    return 'login';
    
    
@account.route('/register')
def register(request):
    return 'register';
    
    
    

