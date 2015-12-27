from API.Configuration import Configuration

__author__ = 'Fabrice Servais'

class NginxServerListen:
    __LISTEN_DIRECTIVE__NAME = "listen"

    def __init__(self, address=None, port=80):
        self.address = address
        self.port = port

    @classmethod
    def from_configuration(cls, configuration):
        """

        :param configuration: Type list<API.Configuration>
        :return:
        """
        address = None
        port = None
        for config in configuration:
            if config.get_key() == 'address':
                address = config.get_value()
            elif config.get_key() == 'port':
                port = config.get_value()

        return NginxServerListen(address, port)

    def __str__(self):
        return "{}".format({'address': self.address, 'port': self.port})

    def __repr__(self):
        return str(self)

    def visit(self, visitor):
        return visitor(self)

if __name__ == "__main__":
    listen = NginxServerListen(address="127.0.0.1", port=8001)

    listen2 = NginxServerListen(port=8001)

    listen3 = NginxServerListen("*", 8001)

    listen4 = NginxServerListen.from_configuration(
        [Configuration({(5, 'address', 'address'): {'ackedstate': 0,
                                                                 'state': 1,
                                                                 'transaction': 0,
                                                                 'value': '127.0.0.1'}}),
        Configuration({(5, 'port', 'port'): {'ackedstate': 0,
                                                           'state': 1,
                                                           'transaction': 0,
                                                           'value': '8003'}})])
