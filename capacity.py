from datetime import datetime, timedelta
# from database import get_capacity_data
from math import ceil
import pytz


# This list defines the capacity and pricing for different countries.
now = datetime.now(pytz.utc)

capacity_collections = [
    {
        "country": "BD",
        "price": 0.30,
        "country_code": "+880",
        "capacity": 100,
        "unlock_time": 3600000,
        "country_imogi": "🇧🇩"
    },
    {
        "country": "USA",
        "country_code": "+1",
        "price": 0.18,
        "capacity": 1,
        "unlock_time": 3600000,
        "country_imogi": "🇺🇸"
    },
    {
        "country": "Algeria",
        "country_code": "+213",
        "price": 0.45,
        "capacity": 100,
        "unlock_time": 3600000,
        "country_imogi": "🇩🇿"
    },
    {
        "country": "India",
        "country_code": "+91",
        "price": 0.38,
        "capacity": 100,
        "unlock_time": 3600000,
        "country_imogi": "🇮🇳"
    },
    {
        "country": "UK",
        "country_code": "+44",
        "price": 1,
        "capacity": 100,
        "unlock_time": 3600000,
        "country_imogi": "🇬🇧"
    },
    {
        "country": "Colombia",
        "country_code": "+57",
        "price": 0.28,
        "capacity": 100,
        "unlock_time": 3600000,
        "country_imogi": "🇨🇴"
    }
]


# ==========================================================>
#                     Break nimu all error bujtase na
# <==========================================================>


# math problem solve just i can use my won project

# print("tested line 1")
# data = get_capacity_data()
# print(data)


# done get capacity data


# def miliSecondToTime():

#     for `tested in capacity_collections:
#         if tested["unlock_time"] <= 60000:
#             leftMinit = ceil(tested["unlock_time"]/1000/60)
#             return leftMinit
#         elif tested["unlock_time"] <= 3600000:
#             leftMinit = ceil(tested["unlock_time"]/1000 / 60 / 60)
#             return leftMinit
#             print(f"{leftMinit} minite")
#         elif tested["unlock_time"] <= 216000000:
#             print(ceil(tested["unlock_time"]/1000/60/60/24))
#         else:
#             print(tested["unlock_time"])
# `
