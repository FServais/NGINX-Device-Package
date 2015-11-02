__author__ = 'Fabrice Servais'


class NginxBackendServer:

    def __init__(self, address="", port="80", params=None):
        self.address = ""
        self.port = ""
        self.params = params

    def set_parameters(self, params):
        """ Set the parameters of the server.

        :param params: Type: NginxBackendServerParameters, set of parameters
        """
        self.params = params

    def __str__(self):
        return "{{ 'address': '{address}', 'port':'{port}', 'parameters': {params} }}".format(address=self.address, port=self.port, params=self.params)

    def __repr__(self):
        return str(self)