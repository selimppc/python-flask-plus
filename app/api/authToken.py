import json
import requests
from flask_restplus import Resource, Namespace, fields, reqparse
from flask import jsonify, request
import datetime
from logging.config import dictConfig
from app.helper.encode_auth_token import encode_auth_token
from app.helper.api_doc_response import api_doc_response

api = Namespace('auth', description='Auth Token')

# Model
token = api.model('Token', {'token': fields.String()})
_tokenModel = api.model('TokenModel', {
    'grant_type': fields.String(required=True, description='This Grant Type is Required'),
    'client_id': fields.String(required=True, description='This ClientID is Required'),
    'client_secret': fields.String(required=True, description='This ClientSecret is Required')
})


@api.route('/')
class TokenProvider(Resource):
    # POST METHOD
    @api.doc(api_doc_response())
    @api.marshal_with(token)
    def get(self):
        """response token"""
        try:
            return {
                'token': encode_auth_token()
            }
        except Exception as e:
            api.abort(400, e.__doc__, status='Could not retrieve information', statusCode='400')

    # POST METHOD
    @api.expect(_tokenModel, validate=True)
    @api.doc(api_doc_response())
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
    # POST METHOD to CALL AUTH SERVICE
    @api.doc(api_doc_response())
    @api.expect(_tokenModel, validate=True)
    # @jwt_token_validate
    def post(self):
        # headers = {'Authorization': 'Bearer Token'}
        # Static Body
        body = dict(authentication_type="phone", phone_no="8801678114307", phone_no_country_code="BD",
                    client_type="web", client_id="123456789", channel="bioscope_web_phone_desktop")

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
