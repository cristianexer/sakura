rom functools import wraps
from app import *


def authenticate_by_email_and_password(email, password):
    query = """
    query($input: UserWhereUniqueInput!) {
        user(where: $input) {
            id
          }
      }
    """
    res = gql.query(query=query,variables={
        'input':{
            'email': email,
            'password': password
        }
    })
    
    return res.json()
    
    
def authenticate_by_email_and_password(username, password):
    query = """
    query($input: UserWhereUniqueInput!) {
        user(where: $input) {
            id
          }
      }
    """
    res = gql.query(query=query,variables={
        'input':{
            'username': username,
            'password': password
        }
    })
    
    return res.json()

def identity(payload):
    user_id = payload['identity']
    
    query = """
    query($input: UserWhereUniqueInput!) {
        user(where: $input) {
            id
          }
      }
    """
    res = gql.query(query=query,variables={
        'input':{
            'id': user_id,
        }
    })
    
    return res.json()


