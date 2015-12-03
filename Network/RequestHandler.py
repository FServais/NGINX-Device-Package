import requests
from pip._vendor.requests import RequestException

__author__ = 'Fabrice Servais'


class RequestHandler:

    def __init__(self, address, port, username=None, password=None):
        self.address = address
        self.port = port

        self.username = username
        self.password = password

        self.response = None

    def send(self, method="GET", location="/", url_params=None, payload=None):
        print("[Request] Try to connect at {}".format(self.url(location)))

        try:
            if method == "GET":
                self.response = requests.get(self.url(location), params=url_params, auth=(self.username, self.password))

            elif method == "PUT":
                self.response = requests.put(self.url(location), params=url_params, json=payload, auth=(self.username, self.password))

            elif method == "POST":
                self.response = requests.post(self.url(location), params=url_params, json=payload, auth=(self.username, self.password))

            elif method == "DELETE":
                self.response = requests.delete(self.url(location), auth=(self.username, self.password))

            else:
                self.response = requests.get(self.url(location), auth=(self.username, self.password))

            json = self.response.json()
        except Exception as e:
            from utils import logger
            logger.log("[Request] Send to {} failed : {}".format(self.url(location), e))
            return 500, e.message

        return self.response.status_code, json

    def url(self, location):
        return "http://{}:{}{}".format(self.address, self.port, location)

if __name__ == "__main__":
    rh = RequestHandler("127.0.0.1", 5000)
    status, response = rh.send("GET")
