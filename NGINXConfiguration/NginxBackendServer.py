from NGINXConfiguration.NginxBackendServerParameters import NginxBackendServerParameters

__author__ = 'Fabrice Servais'


class NginxBackendServer:
    __SERVER_DIRECTIVE_NAME = "server"

    def __init__(self, address, port=80, params=None):
        """
        Constructor.
        :param address: IP address of the server.
        :param port: Port on the server. 80 by default.
        :param params: Type: NginxBackendServerParameters, set of backend parameters.
        """
        self.address = address
        self.port = port
        self.params = params

    @classmethod
    def from_configuration(cls, configuration):
        address = None
        port = 80
        params = NginxBackendServerParameters()

        for config in configuration:
            if config.get_key() == "ip":
                address = config.get_value()
            elif config.get_key() == "port":
                port = config.get_value()
            elif config.get_key() == "backup":
                params.backup = (config.get_value().lower() == 'true')
            elif config.get_key() == "down":
                params.down = (config.get_value().lower() == 'true')
            elif config.get_key() == "fail_timeout":
                params.fail_timeout = int(config.get_value())
            elif config.get_key() == "max_fails":
                params.max_fails = int(config.get_value())
            elif config.get_key() == "weight":
                params.weight = int(config.get_value())

        return NginxBackendServer(address, port, params)

    def set_parameters(self, params):
        """
        Set the parameters of the server.
        :param params: Type: NginxBackendServerParameters, set of backend parameters.
        """
        self.params = params

    def __str__(self):
        to_return = {'address': self.address, 'port': self.port}
        if self.params is not None:
            to_return['parameters'] = self.params

        return "{}".format(to_return)

    def __repr__(self):
        return str(self)

    def export(self):
        from NginxExportConfiguration.Directive import Directive
        parameters = ["{}:{}".format(self.address, self.port)]

        if self.params is not None:
            parameters.extend(self.params.export())

        return Directive(self.__SERVER_DIRECTIVE_NAME, parameters)


if __name__ == "__main__":
    backend_server = NginxBackendServer(address="127.0.0.1", port=80)
    backend_server.set_parameters(NginxBackendServerParameters(backup=True, max_fails=3))

    print(backend_server)
    print(backend_server.export())
