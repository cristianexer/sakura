from functools import wraps

# TODOS

# Create a wrapper to check the role of the JWT
# The decorators receives a list of roles
# Return permission denied if the current use role is not the list of roles
# continue if everything is ok

def iam():
    def _iam(f):
        @wraps(f)
        def __iam(*args, **kwargs):
            # just do here everything what you need
            print('before req')
            result = f(*args, **kwargs)
            print('result: %s' % result)
            print('after req')
            return result
        return __iam
    return _iam




def get_role_by(user_id):
    query = """
    query($input: UserWhereUniqueInput!) {
        user(where: $input) {
            role
          }
      }
    """
    res = gql.query(query=query,variables={
        'input':{
            'id': user_id
        }
    })
    
    return res.json()