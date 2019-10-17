import requests
from sanic.response import json
from json import dumps
from jwt import encode
from datetime import datetime, timedelta

class GraphQLClient:
    
    def __init__(self,prisma):
        self.endpoint = prisma['endpoint']
        d_now = datetime.now()
        token = encode(
            {
            'data': {
                'service': prisma['service'],
                'roles': prisma['roles']
                },
            'iat': int(d_now.strftime("%s")),
            'exp': int((d_now + timedelta(0,(60 * 5))).strftime("%s"))
               }, prisma['secret'], algorithm='HS256')

        self.headers = {'Authorization': 'Bearer ' + token.decode('ascii'),'Content-Type': 'application/json'}
        
        
    def query(self,query,variables=None):
        
        body = dict()
        
        body['query'] = query
        
        if variables:
            body['variables'] = variables
            
        body = dumps(body)
        
        res = requests.post(self.endpoint, headers=self.headers, data=body)
        return res.json()
    
    
    
    def queryStorage(self,name,variables=None):
        
        body = dict()

        body['query'] = 'query($q:String!){queryStorage(where:{name: $q }){query}}'
        body['variables'] = {
            'q': name
        }
            
        remote_query = requests.post(self.endpoint, headers=self.headers, data=dumps(body))
        
        query = remote_query.json().get('data').get('queryStorage',None)
        
        if query:
            query = query.get('query')
        else:
            return {
                'response': f'The query with name: `{name}` does not exists'
            }
        
        
        return self.query(query=query,variables=variables)
        
        