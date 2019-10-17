from sanic import Blueprint
from sanic.response import json
from jwt import encode, decode
from helpers.prisma_handler import GraphQLClient
from helpers.help import generate_user_token
account = Blueprint('account', url_prefix='/account')
from helpers.encryption import encrypt

@account.route('/login',methods=['POST'])
async def login(request):
    body = request.json
    email = body.get('email',None)
    password = body.get('password',None)
    
    
    if email and password:
        client = GraphQLClient(prisma=request.app.config.get('prisma'))
        
        q = """
        query($user_email:String!, $user_password:String!){
            users(where:{
                email: $user_email,
                password: $user_password
            }){
            id
            }
        }
        """
        
        v = {
            'user_email': email,
            'user_password': encrypt(request.app.config.get('sakura').get('secret'),password)
        }
        
        res =  client.query(query=q,variables=v)
        
        res_data = res.get('data').get('users')
       
        if len(res_data) > 0:
            return json({
                'token': generate_user_token(
                user_id=res_data[0].get('id'),
                service=request.app.config.get('sakura').get('service'),
                duration = request.app.config.get('sakura').get('token_lifetime_minutes'),
                secret=request.app.config.get('sakura').get('secret')
            )
            },status=200)
        else:
            return json({
            'response': res.get('errors')
        },status=300)
        
    else:
        return json({
            'response': 'Something went wrong'
        },status=300)
    
    
    
@account.route('/register',methods=['POST'])
async def register(request):
    body = request.json
    username = body.get('username',None)
    email = body.get('email',None)
    password = body.get('password',None)
    
    
    if username and email and password:
        client = GraphQLClient(prisma=request.app.config.get('prisma'))
        
        q = """
        mutation($user_name:String!, $user_password:String!, $role:Roles!, $user_email:String!){
          createUser(data:{
            username:$user_name
            password:$user_password
            email:$user_email
            role:$role
          }){
            id
          }
        }
        """
        
        v = {
            'user_email': email,
            'user_password': encrypt(request.app.config.get('sakura').get('secret'),password),
            'user_name': username,
            'role': 'USER'
        }
        
        res =  client.query(query=q,variables=v)
        

        if res.get('data',None):
            user_id = res.get('data').get('createUser').get('id')
            return json({
                'token': generate_user_token(
                user_id=user_id,
                service=request.app.config.get('sakura').get('service'),
                duration = request.app.config.get('sakura').get('token_lifetime_minutes'),
                secret=request.app.config.get('sakura').get('secret')
            )
            },status=200)
        else:
            return json({
            'response': res.get('errors')
        },status=300)
        
    else:
        return json({
            'response': 'Something went wrong'
        },status=300)
    
    
    







    

