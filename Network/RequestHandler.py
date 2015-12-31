import requests
from utils import logger

__author__ = 'Fabrice Servais'


class RequestHandler:

    def __init__(self, address, port, username=None, password=None, https=False):
        self.address = address
        self.port = port

        self.username = username
        self.password = password

        self.https = https


    def send(self, method="GET", location="/", url_params=None, payload=None):
        """
        Send a request at 'self.address':'self.port', at the URI 'location', with the credentials <'self.username' ; 'self.password'> via HTTPS or HTTP.
        The request is sent with the HTTP method 'method' and has the payload 'payload', and the URL can have the parameters 'url_params'.

        Args:
            method: (String) HTTP method (GET, POST,...)
            location: (String) Location in the URI (e.g. /, /a, /a/b/c/d,...)
            url_params: (Dictionary, {'name': value}) Parameters to pass via the URL.
            payload: (Dictionary, {'name': value}) Payload of the request

        Returns: (int, String) or (int, Dictionary)
            int: HTTP status of the response
            String or Dictionary: Content of the response

        """

        logger.log("[Request] Try to connect at {}".format(self.url(location)))
        response = None

        try:
            if method == "GET":
                response = requests.get(self.url(location), params=url_params, auth=(self.username, self.password), verify=False)

            elif method == "PUT":
                response = requests.put(self.url(location), params=url_params, json=payload, auth=(self.username, self.password), verify=False)

            elif method == "POST":
                response = requests.post(self.url(location), params=url_params, json=payload, auth=(self.username, self.password), verify=False)

            elif method == "DELETE":
                response = requests.delete(self.url(location), auth=(self.username, self.password), verify=False)

            else:
                response = requests.get(self.url(location), auth=(self.username, self.password), verify=False)

        except Exception as e:
            logger.log("[Request] Send to {} failed : {}".format(self.url(location), e))
            return 504, e.message

        # If not authenticated
        if response.status_code == 401:
            return response.status_code, 'Not authorized'

        try:
            json = response.json()

        except Exception as e:
            logger.log("[Request] Message extraction from {} failure : {}".format(self.url(location), e))
            return response.status_code, e.message

        return response.status_code, json

    def url(self, location):
        """
        Returns the URI where the request can be sent, depending on the address, the port, the 'location' and HTTP(S).

        Args:
            location: String of the location of the request (e.g. '/', '/config',...)

        Returns: String
            String: URI

        """
        return ("https" if self.https else "http") + "://{}:{}{}".format(self.address, self.port, location)
