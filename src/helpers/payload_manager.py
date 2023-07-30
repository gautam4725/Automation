

def create_booking_payload():
    payload = {
        "firstname": "Gautam",
        "lastname": "Kogale",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast,Dinner"
    }
    return payload