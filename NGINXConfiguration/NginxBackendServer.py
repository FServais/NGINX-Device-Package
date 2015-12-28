# from NGINXConfiguration.NginxBackendServerParameters import NginxBackendServerParameters

__author__ = 'Fabrice Servais'


class NginxBackendServer:
    __SERVER_DIRECTIVE_NAME = "server"

    def __init__(self, address, port=80, backup=False, down=False, fail_timeout=-1, max_fails=-1, weight=-1):
        """
        Constructor.
        :param address: IP address of the server.
        :param port: Port on the server. 80 by default.
        :param params: Type: NginxBackendServerParameters, set of backend parameters.
        """
        self.address = address
        self.port = port

        # Parameters
        self.backup = backup
        self.down = down
        self.fail_timeout = fail_timeout
        self.max_fails = max_fails
        self.weight = weight

    @classmethod
    def from_configuration(cls, configuration):
        address = None
        port = 80

        backup = False
        down = False
        fail_timeout = -1
        max_fails = -1
        weight = -1

        for config in configuration:
            if config.get_key() == "ip":
                address = config.get_value()
            elif config.get_key() == "port":
                port = config.get_value()
            elif config.get_key() == "backup":
                backup = (config.get_value().lower() == 'true')
            elif config.get_key() == "down":
                down = (config.get_value().lower() == 'true')
            elif config.get_key() == "fail_timeout":
                fail_timeout = int(config.get_value())
            elif config.get_key() == "max_fails":
                max_fails = int(config.get_value())
            elif config.get_key() == "weight":
                weight = int(config.get_value())

        return NginxBackendServer(address=address, port=port, backup=backup, down=down, fail_timeout=fail_timeout,
                                  max_fails=max_fails, weight=weight)

    def __str__(self):
        to_return = {'address': self.address, 'port': self.port, 'backup': self.backup, 'down': self.down,
                     'fail_timeout': self.fail_timeout, 'max_fails': self.max_fails, 'weight': self.weight}

        return "{}".format(to_return)

    def __repr__(self):
        return str(self)

    def accept(self, visitor):
        return visitor(self)


if __name__ == "__main__":
    backend_server = NginxBackendServer(address="127.0.0.1", port=80)
    print(backend_server)
