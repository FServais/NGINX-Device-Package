import requests
from utils import logger

__author__ = 'Fabrice Servais'


class RequestHandler:

    def __init__(self, address, port, username=None, password=None, https=True):
        self.address = address
        self.port = port

        self.username = username
        self.password = password

        self.response = None
        self.https = https


    def send(self, method="GET", location="/", url_params=None, payload=None):
        logger.log("[Request] Try to connect at {}".format(self.url(location)))

        try:
            if method == "GET":
                self.response = requests.get(self.url(location), params=url_params, auth=(self.username, self.password), verify=False)

            elif method == "PUT":
                self.response = requests.put(self.url(location), params=url_params, json=payload, auth=(self.username, self.password), verify=False)

            elif method == "POST":
                self.response = requests.post(self.url(location), params=url_params, json=payload, auth=(self.username, self.password), verify=False)

            elif method == "DELETE":
                self.response = requests.delete(self.url(location), auth=(self.username, self.password), verify=False)

            else:
                self.response = requests.get(self.url(location), auth=(self.username, self.password), verify=False)

            json = self.response.json()

        except Exception as e:
            logger.log("[Request] Send to {} failed : {}".format(self.url(location), e))
            return 504, e.message

        return self.response.status_code, json

    def url(self, location):
        return ("https" if self.https else "http") + "://{}:{}{}".format(self.address, self.port, location)
