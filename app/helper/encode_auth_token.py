import datetime
import jwt


def encode_auth_token():
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': 2222
        }
        token = jwt.encode(
            payload,
            'this-is-enc',
            algorithm='HS256'
        )
        return token.decode()
    except Exception as e:
        return e
