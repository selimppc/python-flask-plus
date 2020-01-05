from flask_restplus import Namespace, Resource, fields
from sqlalchemy import null, true, false

api = Namespace('activePackage', description='Active Package for a use/msisdn')

activate = api.model('Active', {
    'code': fields.String(required=True, description='code SUCCESS or FAIL'),
    'message': fields.String(required=True, description='message'),
    'data': fields.String(required=True, description='Object'),
})

ACTIVATE = {
    "code": "SUCCESS",
    "message": "User is subscribed",
    "data": {
        "user": {
            "id": 42
        },
        "stripe": {
            "customerId": null
        },
        "subscription": {
            "subscriptionId": 436,
            "userId": 42,
            "phoneNo": "8801831803255",
            "gatewayName": null,
            "subscribedFrom": "BD",
            "isCouponApplicableOnPack": true,
            "usedCoupon": null,
            "packageId": 23,
            "packageName": "Banglalink Daily Plan",
            "keyword": "BANGLALINK-DAILY",
            "duration": "1 Day(s)",
            "price": 2.5499999999999998,
            "currency": "BDT",
            "symbol": "BDT",
            "isAutoRecurring": true,
            "isUpgradeable": false,
            "expiryDate": {
                "date": "2020-01-06 23:35:56.797978",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "currentDate": {
                "date": "2020-01-04 04:53:27.811295",
                "timezone_type": 3,
                "timezone": "UTC"
            },
            "isThisPackageAutoRenewable": false,
            "hasUserEverSubscribed": true
        }
    }
}


@api.route('/')
class ActivatePackage(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Request', 500: 'Mapping Key Error'})
    @api.marshal_with(activate)
    def get(self):
        """Response"""
        try:
            return ACTIVATE
        except Exception as e:
            api.abort(400, e.__doc__, status='Could not retrieve information', statusCode='400')

