__author__ = 'Fabrice Servais'


class NginxServerLocation:
    __LOCATION_BLOCK_NAME = "location"

    def __init__(self, backend_name, uri, pass_method="proxy_pass", https=False):
        self.uri = uri
        self.pass_method = pass_method
        self.https = https
        self.backend_name = backend_name

    def __str__(self):
        return "{}".format({'backend_name': self.backend_name, 'uri': self.uri, 'pass_method': self.pass_method, 'https': self.https})

    def __repr__(self):
        return str(self)

    def export(self):
        from ExportConfiguration.Block import Block
        from ExportConfiguration.Directive import Directive
        return Block(self.__LOCATION_BLOCK_NAME, self.uri, Directive(self.pass_method, "{}://{}".format("https" if self.https else "http", self.backend_name)))


if __name__ == "__main__":
    location = NginxServerLocation("backend", "/")
    print(location)
    print(location.export())