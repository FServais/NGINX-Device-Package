from NGINXConfiguration.NginxBackendServerParameters import NginxBackendServerParameters

__author__ = 'Fabrice Servais'


class NginxBackendServer:
    __SERVER_DIRECTIVE_NAME = "server"

    def __init__(self, address="", port=80, params=None):
        self.address = address
        self.port = port
        self.params = params if params is not None else []

    def set_parameters(self, params):
        """ Set the parameters of the server.

        :param params: Type: NginxBackendServerParameters, set of parameters
        """
        self.params = params

    def __str__(self):
        return "{}".format({'address': self.address, 'port': self.port, 'parameters': self.params})

    def __repr__(self):
        return str(self)

    def export(self):
        from ExportConfiguration.Directive import Directive
        parameters = ["{}:{}".format(self.address, self.port)]
        parameters.extend(self.params.export())

        return Directive(self.__SERVER_DIRECTIVE_NAME, parameters)

if __name__ == "__main__":
    b_serv1 = NginxBackendServer(address="127.0.0.1", port=80, params=NginxBackendServerParameters(backup=True, max_fails=3))

    print(b_serv1)
    print(b_serv1.export())