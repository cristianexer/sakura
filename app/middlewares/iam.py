from functools import wraps

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
