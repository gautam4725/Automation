# HTTP status code



def verify_http_code(response_data,expected_data):
    assert response_data.status_code==expected_data, "Expected HTTP status :" + expected_data


def verify_key(response_data,key):
    assert key != 0, "Key is non empty:" + key
