import requests
from sanic.response import json
from json import dumps

class GraphQLClient:
    
    def __init__(self,endpoint, token):
        self.endpoint = endpoint
        self.headers = {'Authorization': 'Bearer ' + token,'Content-Type': 'application/json'}
        
        
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

        body['query'] = 'query{queryStorage(where:{name: "' + name + '"}){query}}'
            
        remote_query = requests.post(self.endpoint, headers=self.headers, data=dumps(body))
        
        query = remote_query.json().get('data').get('queryStorage',None)
        
        if query:
            query = query.get('query')
        else:
            return {
                'response': f'The query with name: `{name}` does not exists'
            }
        
        
        return self.query(query=query,variables=variables)
        
        