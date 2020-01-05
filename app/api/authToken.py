import json

import requests
from flask_restplus import Resource, Namespace, fields, reqparse
from flask import Flask, jsonify, request
import datetime
import jwt
from logging.config import dictConfig

from config import key

api = Namespace('auth', description='Auth Token')

token = api.model('Token', {
    'token': fields.String()
})


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


_tokenModel = api.model('TokenModel', {
    'grant_type': fields.String(required=True, description='This Grant Type is Required'),
    'client_id': fields.String(required=True, description='This ClientID is Required'),
    'client_secret': fields.String(required=True, description='This ClientSecret is Required')
})


@api.route('/')
class TokenProvider(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Request', 500: 'Mapping Key Error'})
    @api.marshal_with(token)
    def get(self):
        """response token"""
        try:
            return {
                'token': encode_auth_token()
            }
        except Exception as e:
            api.abort(400, e.__doc__, status='Could not retrieve information', statusCode='400')

    @api.expect(_tokenModel, validate=True)
    def post(self):
        requestData = request.json

        data = {
            'access_token': encode_auth_token(),
            'token_type': 'Bearer',
            'expires_in': str(datetime.timedelta(days=1))
        }
        return jsonify(data)


@api.route('/call_to_auth_ms')
class CallToAuthMs(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Request', 500: 'Mapping Key Error'})
    @api.expect(_tokenModel, validate=True)

    #@jwt_token_validate
    def post(self):
        # headers = {'Authorization': 'Bearer Token'}
        body = {
            "authentication_type": "phone",
            "phone_no": "8801678114307",
            "phone_no_country_code": "BD",
            "client_type": "web",
            "client_id": "123456789",
            "channel": "bioscope_web_phone_desktop"

        }

        try:
            r = requests.post('http://stageapi.bongobd.com/app_dev.php/api/login_check',
                              data=body
                              )
            response = json.loads(r.content.decode('utf-8'))
            return {
                'token': response['token']
            }
        except Exception as e:
            api.abort(400, e.__doc__, status='Could not retrieve information', statusCode='400')
