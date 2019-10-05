from functools import wraps

def prisma():
    def _prisma(f):
        @wraps(f)
        def __prisma(*args, **kwargs):
            # just do here everything what you need
            print('before req')
            result = f(*args, **kwargs)
            print('result: %s' % result)
            print('after req')
            return result
        return __prisma
    return _prisma
