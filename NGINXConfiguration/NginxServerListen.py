__author__ = 'Fabrice Servais'

class NginxServerListen:
    __LISTEN_DIRECTIVE__NAME = "listen"

    def __init__(self, address=None, port=80):
        self.address = address
        self.port = port

    def __str__(self):
        return "{}".format({'address': self.address, 'port': self.port})

    def __repr__(self):
        return str(self)

    def export(self):
        from NginxExportConfiguration.Directive import Directive
        param = ""

        if self.address:
            param = "{}:".format(self.address)

        param = "{}{}".format(param, self.port)

        return Directive(self.__LISTEN_DIRECTIVE__NAME, param)

if __name__ == "__main__":
    listen = NginxServerListen("127.0.0.1", 8001)
    print(listen.export())

    listen2 = NginxServerListen(port=8001)
    print(listen2.export())

    listen3 = NginxServerListen("*", 8001)
    print(listen3.export())