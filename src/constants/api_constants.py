# Add your constants here

# Adding url constants


def base_url():

    # Changebased on the env.json -STG,Prod,Pre-prod
    # In future I will write a logic to change the base url based on the env
    return "https://restful-booker.herokuapp.com"

# BASE_URL="https://restful-booker.herokuapp.com"

def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"

# return"BASE_URL/booking"

def url_create_token():
    return "https://restful-booker.herokuapp.com/booking/auth"
# return"BASE_URL/booking/auth"

def url_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + booking_id

# return"BASE_URL/booking/" +booking_id