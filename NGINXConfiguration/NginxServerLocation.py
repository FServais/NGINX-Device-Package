__author__ = 'Fabrice Servais'


class NginxServerLocation:
    __LOCATION_BLOCK_NAME = "location"

    def __init__(self, backend_name, uri, pass_method="proxy_pass", https=False, modifier=None):
        """
        Constructor.
        :param backend_name: Name of the backend.
        :param uri: URI, location of the request.
        :param pass_method: Pass directive.
        :param https: True of using HTTPS.
        """
        self.uri = uri
        self.pass_method = pass_method
        self.https = https
        self.backend_name = backend_name
        self.modifier = modifier

    def __str__(self):
        return "{}".format(
            {'backend_name': self.backend_name, 'uri': self.uri, 'pass_method': self.pass_method, 'https': self.https,
             'modifier': self.modifier})

    def __repr__(self):
        return str(self)

    def export(self):
        from NginxExportConfiguration.Block import Block
        from NginxExportConfiguration.Directive import Directive

        block_parameters = []
        if self.modifier:
            block_parameters.append(self.modifier)

        block_parameters.append(self.uri)

        return Block(self.__LOCATION_BLOCK_NAME, block_parameters, Directive(self.pass_method, "{}://{}".format(
            "https" if self.https else "http", self.backend_name)))


if __name__ == "__main__":
    location = NginxServerLocation("backend", "/", pass_method="method", modifier="~*")
    print(location)
    print(location.export())
