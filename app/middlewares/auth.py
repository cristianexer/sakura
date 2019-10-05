from functools import wraps

def auth():
    def _auth(f):
        @wraps(f)
        def __auth(*args, **kwargs):
            # just do here everything what you need
            print('before req')
            result = f(*args, **kwargs)
            print('result: %s' % result)
            print('after req')
            return result
        return __auth
    return _auth
