from flask import request
from six import wraps
from werkzeug.exceptions import Unauthorized
import jwt


def require_jwt_auth(handler_function):
    """Authenticates JWT against User DB"""

    @wraps(handler_function)
    def _require_auth(*args, **kwargs):
        token = request.headers.get('Authorization')
        default_error_msg = {"message": "Invalid header authorization"}

        if not token:
            raise Unauthorized(description=default_error_msg)

        parts = token.split()
        if parts[0].lower() != 'bearer' or len(parts) != 2:
            raise Unauthorized(description=default_error_msg)
        auth_token = parts[1]

        try:
            return handler_function(*args, **kwargs)

        except jwt.exceptions.DecodeError as error:
            error_msg = {"message": f'Invalid header authorization: {error}'}
            raise Unauthorized(description=error_msg)
        except jwt.ExpiredSignatureError as error:
            error_msg = {"message": f'Signature expired. Please log in again. {error}'}
            raise Unauthorized(description=error_msg)
        except jwt.InvalidTokenError as error:
            error_msg = {"message": f'Invalid token. Please log in again. {error}'}
            raise Unauthorized(description=error_msg)

    return _require_auth
