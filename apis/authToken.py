from flask_restplus import Resource, Namespace, fields
from flask import Flask, jsonify, request
import datetime
import jwt

# from ..config import key

api = Namespace('auth', description='Auth Token')

token = api.model('Token', {
    'token': fields.String()
})

TOKEN = {
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE1NzgwNzQ4MDUsImV4cCI6MTU3ODE2MTIwNSwicm9sZXMiOlsiUk9MRV9VU0VSX0JJT1NDT1BFIiwiUExFWFVTX1VTRVIiLCJST0xFX1VTRVIiXSwidXNlcm5hbWUiOiJQTEVYVVNfVVNFUiIsImNsaWVudF9sb2dpbl9pZCI6ImQ5YWU4OWI5MzNjM2Q1NGNjMzJmIn0.p8lDAblbRU941D2TvRee2IdkP2_bD-ZXTsYOmwnTbn9Nt7ZQuzRN3LRPk_IweHY0zdJd45DYOjExcNc6b37TKXDYThefWg6XLNJ613W6XM8wFwrUQzZkfSK7W6nOOOF_3JCF-CrOBcaiTdgwtwOQVKdA832_U1eBd9WBBGC3BKgLV9qrnMQc7ayMaMna1tWrS4bn5Ko3XTKQ7mgrHKA4UQmDPy7Jyt_ITjEMan6dtZv7XEVMLn4GanPuR4d2c-qKQMx7-75QwhWV0Y7wjk2AruJivsE5Z2mzjUPHEkEKxTOSmHNxG8w1nuIMDRcO0iASKerbbgduROecQQVpY4jiL3wQ_hphxUId3t2zPwbawMXTvYYWQWD3Cxt8BL5jdDdwp6TqcqIJ9Nt2EvhfPRey6kQ24vHn6EJQfaC6kz7xCoyrYuyHG9wNqm8_3lJev3it7oEA0sTC2X9Omca7s13X5qu-Y_exgBDNiLAWY7nq6KqHsjgCGnR5naMDiGa0k3SYoDeP5xJdFubmCHCX_YiaxM2nuD5Bh_pG4sYtT58-LKpl8azZHpflcX9B6wlwHJC4gRrhDITPOGJtFlpFijHC64GzmubGmCPG4Cr_3S5cmtH9vyKJHP9C-km1y8Vho4VmV1Sh7AJD_xr_MnlN-Pscrm9jj99s4p52v-ieNn6PmHI'
}


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
        return jwt.encode(
            payload,
            # key,
            algorithm='HS256'
        )
    except Exception as e:
        return e


@api.route('/')
class TokenProvider(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Request', 500: 'Mapping Key Error'})
    @api.marshal_with(token)
    def get(self):
        """response token"""
        try:
            return TOKEN
        except Exception as e:
            api.abort(400, e.__doc__, status='Could not retrieve information', statusCode='400')

