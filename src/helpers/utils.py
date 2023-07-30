# Help you to read the json files and provides json data
import json


def get_payload_auth():
    # Read from the auth.json and return json

    file_data = open("src/resources/auth.son")
    data=json.loads(file_data)
    file_data.close()
    return data

def common_headers():
    headers = {

        "Content-Type": "application/json"

    }
    return headers
