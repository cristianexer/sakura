from sanic import Blueprint
from sanic.response import json
from json import dumps
import requests as req
from helpers.prisma_handler import GraphQLClient

#from middlewares.iam import iam
#from middlewares.auth import auth

ineed = Blueprint('ineed', url_prefix='/ineed')

@ineed.route('/',methods=['POST'])
async def need(request):
    
    client = GraphQLClient(
        endpoint=request.app.config['api_endpoint'],
        token=request.app.config['api_token']
        )
    
    body = request.json
    
    q = body.get('query',None)
    q_name = body.get('query_name',None)
    variables = body.get('variables',None)
    
    print(f'\nQuery: {q}\nQuery Name: {q_name} \nVars: {variables}\n')
    
    if q:
        res = client.query(query=q,variables=variables)
    
    elif q_name:
        res = client.queryStorage(name=q_name,variables=variables)
    
    else:
        return json({
            'response': False,
            'error': 'You have to specify the `query` or the `query_name`.'
        },status=300)
    
    
    return json(res,status=200)


