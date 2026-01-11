import requests

class APIUtility:

    def get(self, endpoint=None, params=None, headers=None, data=None):
        response = requests.get(url=endpoint)
        return response

    def post(self, endpoint=None, data=None, params=None):
        response = requests.post(url=endpoint, json=data)
        return response