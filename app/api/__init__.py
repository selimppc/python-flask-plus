from flask import Blueprint
from flask_restplus import Api

from .authToken import api as ns1
from .getPackageList import api as ns2
from .activePackageCall import api as ns3

#blueprint_api = Blueprint('api', __name__, url_prefix="/api")
api = Api(
    title='Digital Agency APP',
    version='1.0',
    description='Digital Agency is gonna sell/active Bongo Packages for a user !'
    # ALl API Metadata
)

api.add_namespace(ns1, path='/api/v1/auth/token')
api.add_namespace(ns2, path='/api/v1/getPackageList')
api.add_namespace(ns3, path='/api/v1/activePackage')
