from flask_restplus import Namespace, Resource, fields
from sqlalchemy import false, null, true

api = Namespace('packageList', description='Get Package List')

package = api.model('Package', {
    'id': fields.String(required=True, description='Package Identifier'),
    'title': fields.String(required=True, description='Title of the package'),
    'price': fields.String(required=True, description='price of the package'),
    'period': fields.String(required=True, description='Period'),
    'description': fields.String(required=True, description='description'),
    'gateways': fields.String(required=True, description='gateway'),
    'extra_parameters': fields.String(required=True, description='extra parameters'),
    'is_recurring': fields.String(required=True, description='is recurring'),
    'is_upgradeable': fields.String(required=True, description='is upgradable'),
    'keyword': fields.String(required=True, description='Keyword'),
    'tag_line': fields.String(required=True, description='Tag Line'),
    'badge_text': fields.String(required=True, description='Badge Text'),
    'badge_color_from': fields.String(required=True, description='Badge Color From'),
    'badge_color_to': fields.String(required=True, description='Badge Color To'),
})

PACKAGE = [
    {
        "id": 16,
        "title": "১ দিন আনলিমিটেড Bongo",
        "price": {
            "price": 5.2199999999999998,
            "currency": "BDT",
            "symbol": "BDT"
        },
        "period": "1 Day(s)",
        "description": [
            "জনপ্রিয় নাটক, টিভি সিরিজ, সিনেমা এবং মিউজিক ভিডিও",
            " কোন অতিরিক্ত বিজ্ঞাপন অথবা বাধা নেই",
            " এক্সক্লুসিভ এবং অরিজিনাল সব ভিডিও"
        ],
        "gateways": [
            "GP"
        ],
        "extra_parameters": [
            {
                "name": "gp",
                "parameters": {
                    "serviceId": "PPU00021805382181128143",
                    "isAutoRenewable": "false"
                }
            }
        ],
        "is_recurring": "false",
        "is_upgradeable": "true",
        "keyword": "BONGO-DAILY",
        "tag_line": "null",
        "badge_text": "null",
        "badge_color_from": "#ed482f",
        "badge_color_to": "#ed4f2f"
    },
    {
        "id": 17,
        "title": "৩ দিন আনলিমিটেড Bongo",
        "price": {
            "price": 10.460000000000001,
            "currency": "BDT",
            "symbol": "BDT"
        },
        "period": "3 Day(s)",
        "description": [
            "জনপ্রিয় নাটক, টিভি সিরিজ, সিনেমা এবং মিউজিক ভিডিও",
            " কোন অতিরিক্ত বিজ্ঞাপন অথবা বাধা নেই",
            " এক্সক্লুসিভ এবং অরিজিনাল সব ভিডিও"
        ],
        "gateways": [
            "GP",
            "TELETALK"
        ],
        "extra_parameters": [
            {
                "name": "gp",
                "parameters": {
                    "serviceId": "PPU00021805382181128143",
                    "isAutoRenewable": "false"
                }
            },
            {
                "name": "teletalk",
                "parameters": {
                    "serviceId": "BD",
                    "chargingId": "",
                    "appChargingKey": "",
                    "ussd": "",
                    "isAutoRenewable": "true"
                }
            }
        ],
        "is_recurring": "false",
        "is_upgradeable": "true",
        "keyword": "BONGO-3DAY",
        "tag_line": "null",
        "badge_text": "null",
        "badge_color_from": "#ed482f",
        "badge_color_to": "#ed4f2f"
    },
    {
        "id": 18,
        "title": "৭ দিন আনলিমিটেড Bongo",
        "price": {
            "price": 10,
            "currency": "BDT",
            "symbol": "BDT"
        },
        "period": "7 Day(s)",
        "description": [
            "জনপ্রিয় নাটক, টিভি সিরিজ, সিনেমা এবং মিউজিক ভিডিও",
            " কোন অতিরিক্ত বিজ্ঞাপন অথবা বাধা নেই",
            " এক্সক্লুসিভ এবং অরিজিনাল সব ভিডিও"
        ],
        "gateways": [
            "GP",
            "TELETALK",
            "ROBI",
            "AIRTEL",
            "GHOORI"
        ],
        "extra_parameters": [
            {
                "name": "gp",
                "parameters": {
                    "serviceId": "PPU00021805382181128143",
                    "isAutoRenewable": "false"
                }
            },
            {
                "name": "teletalk",
                "parameters": {
                    "serviceId": "BW",
                    "chargingId": "",
                    "appChargingKey": "",
                    "ussd": "",
                    "isAutoRenewable": "true"
                }
            },
            {
                "name": "robi",
                "parameters": {
                    "serviceId": "BONGOW",
                    "chargingId": "0300415027",
                    "appChargingKey": "",
                    "ussd": "",
                    "isAutoRenewable": "true"
                }
            },
            {
                "name": "airtel",
                "parameters": {
                    "serviceId": "BONGOW",
                    "chargingId": "0300415027",
                    "appChargingKey": "",
                    "ussd": "",
                    "isAutoRenewable": "true"
                }
            },
            {
                "name": "ghoori",
                "parameters": {
                    "isAutoRenewable": "false",
                    "serviceId": "BBD_7"
                }
            }
        ],
        "is_recurring": "false",
        "is_upgradeable": "true",
        "keyword": "BONGO-7DAYS-SPECIAL",
        "tag_line": "null",
        "badge_text": "null",
        "badge_color_from": "#ed482f",
        "badge_color_to": "#ed4f2f"
    },
    {
        "id": 19,
        "title": "১৫ দিন আনলিমিটেড Bongo",
        "price": {
            "price": 20,
            "currency": "BDT",
            "symbol": "BDT"
        },
        "period": "15 Day(s)",
        "description": [
            "জনপ্রিয় নাটক, টিভি সিরিজ, সিনেমা এবং মিউজিক ভিডিও",
            " কোন অতিরিক্ত বিজ্ঞাপন অথবা বাধা নেই",
            " এক্সক্লুসিভ এবং অরিজিনাল সব ভিডিও"
        ],
        "gateways": [
            "GP",
            "TELETALK",
            "ROBI",
            "AIRTEL"
        ],
        "extra_parameters": [
            {
                "name": "gp",
                "parameters": {
                    "serviceId": "PPU00021805382181128143",
                    "isAutoRenewable": "false"
                }
            },
            {
                "name": "teletalk",
                "parameters": {
                    "serviceId": "BM",
                    "chargingId": "",
                    "appChargingKey": "",
                    "ussd": "",
                    "isAutoRenewable": "true"
                }
            },
            {
                "name": "robi",
                "parameters": {
                    "serviceId": "BONGO15",
                    "chargingId": "0300415029",
                    "appChargingKey": "",
                    "ussd": "",
                    "isAutoRenewable": "true"
                }
            },
            {
                "name": "airtel",
                "parameters": {
                    "serviceId": "BONGO15",
                    "chargingId": "0300415029",
                    "appChargingKey": "",
                    "ussd": "",
                    "isAutoRenewable": "true"
                }
            }
        ],
        "is_recurring": "false",
        "is_upgradeable": "true",
        "keyword": "BONGO-15DAYS",
        "tag_line": "null",
        "badge_text": "null",
        "badge_color_from": "#ed482f",
        "badge_color_to": "#ed4f2f"
    },
    {
        "id": 10,
        "title": "৩০ দিন আনলিমিটেড Bongo",
        "price": {
            "price": 30,
            "currency": "BDT",
            "symbol": "BDT"
        },
        "period": "1 Month(s)",
        "description": [
            "জনপ্রিয় নাটক, টিভি সিরিজ, সিনেমা এবং মিউজিক ভিডিও",
            " কোন অতিরিক্ত বিজ্ঞাপন অথবা বাধা নেই",
            " এক্সক্লুসিভ এবং অরিজিনাল সব ভিডিও"
        ],
        "gateways": [
            "GHOORI",
            "GP",
            "ROBI",
            "AIRTEL"
        ],
        "extra_parameters": [
            {
                "name": "ghoori",
                "parameters": {
                    "isAutoRenewable": "false",
                    "serviceId": "BBD_30"
                }
            },
            {
                "name": "gp",
                "parameters": {
                    "serviceId": "PPU00021805382181128143",
                    "isAutoRenewable": "false"
                }
            },
            {
                "name": "robi",
                "parameters": {
                    "serviceId": "BONGOM",
                    "chargingId": "0300415031",
                    "appChargingKey": "",
                    "ussd": "",
                    "isAutoRenewable": "true"
                }
            },
            {
                "name": "airtel",
                "parameters": {
                    "serviceId": "BONGOM",
                    "chargingId": "0300415031",
                    "appChargingKey": "",
                    "ussd": "",
                    "isAutoRenewable": "true"
                }
            }
        ],
        "is_recurring": "false",
        "is_upgradeable": "true",
        "keyword": "BIO-MONTHLY",
        "tag_line": "null",
        "badge_text": "null",
        "badge_color_from": "#ed482f",
        "badge_color_to": "#ed4f2f"
    },
    {
        "id": 12,
        "title": "365 দিন আনলিমিটেড Bongo",
        "price": {
            "price": 400,
            "currency": "BDT",
            "symbol": "BDT"
        },
        "period": "12 Month(s)",
        "description": [
            "জনপ্রিয় নাটক, টিভি সিরিজ, সিনেমা এবং মিউজিক ভিডিও",
            " কোন অতিরিক্ত বিজ্ঞাপন অথবা বাধা নেই",
            " এক্সক্লুসিভ এবং অরিজিনাল সব ভিডিও"
        ],
        "gateways": [
            "GHOORI"
        ],
        "extra_parameters": [
            {
                "name": "ghoori",
                "parameters": {
                    "isAutoRenewable": "false",
                    "serviceId": "BBD_365"
                }
            }
        ],
        "is_recurring": "false",
        "is_upgradeable": "false",
        "keyword": "BIO-YEARLY",
        "tag_line": "null",
        "badge_text": "null",
        "badge_color_from": "#ed482f",
        "badge_color_to": "#ed4f2f"
    }
]


@api.route('/')
@api.response(404, 'NULL')
class PackageList(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Request', 500: 'Mapping Key Error'})
    @api.marshal_with(package)
    def get(self):
        """List all packages"""
        try:
            return PACKAGE
        except Exception as e:
            api.abort(400, e.__doc__, status='Could not retrieve information', statusCode='400')

