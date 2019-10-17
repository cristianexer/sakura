from jwt import encode
from datetime import datetime, timedelta

def generate_user_token(user_id, service, duration, secret, alg='HS256'):
    iat = datetime.now()
    exp = iat + timedelta(0, (60 * duration))
    return encode({'data':{
                'identity': user_id,
                'service': service
                },
            'iat': int(iat.strftime("%s")),
            'exp': int(exp.strftime("%s"))
                }, secret, algorithm=alg).decode('ascii')
