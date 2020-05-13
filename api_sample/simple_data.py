import requests


def call_api(base_url, endpoint, method, latitude=None, longitude=None):
    flag = latitude and longitude
    payload = {
            'lat': latitude,
            'lon': longitude
        }
    if method:
        if method.value == 'GET':
            if flag:
                data = requests.get(base_url + endpoint, params=payload)
            else:
                data = requests.get(base_url+endpoint)
        elif method.value == 'POST':
            if flag:
                data = requests.post(base_url+endpoint, params=payload)
            else:
                data = requests.post(base_url+endpoint)
        elif method.value == 'PUT':
            if flag:
                data = requests.put(base_url + endpoint, params=payload)
            else:
                data = requests.put(base_url + endpoint)
        else:
            raise ValueError("Invalid method given")
        return data
    raise ValueError("Doesn't given method")

