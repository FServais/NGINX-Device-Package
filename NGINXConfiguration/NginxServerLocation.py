from API.Configuration import Configuration

__author__ = 'Fabrice Servais'


class NginxServerLocation:
    __LOCATION_BLOCK_NAME = "location"
    __DEFAULT_PASS_METHOD = "proxy_pass"

    def __init__(self, backend_name, uri, pass_method=__DEFAULT_PASS_METHOD, https=False, modifier=None):
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

    @classmethod
    def from_configuration(cls, configuration):
        backend_name = ""
        uri = ""
        pass_method = cls.__DEFAULT_PASS_METHOD
        https = False
        modifier = None

        for config in configuration:
            if config.get_key() == "backend_name":
                backend_name = config.get_value()
            elif config.get_key() == "uri":
                uri = config.get_value()
            elif config.get_key() == "pass_method":
                pass_method = config.get_value()
            elif config.get_key() == "https":
                https = config.get_value().lower() == 'true'
            elif config.get_key() == "modifier":
                modifier = config.get_value()

        return NginxServerLocation(backend_name, uri, pass_method, https, modifier)

    def __str__(self):
        return "{}".format(
            {'backend_name': self.backend_name, 'uri': self.uri, 'pass_method': self.pass_method, 'https': self.https,
             'modifier': self.modifier})

    def __repr__(self):
        return str(self)

    def accept(self, visitor):
        return visitor(self)

if __name__ == "__main__":
    location = NginxServerLocation("backend", "/", pass_method="method", modifier="~*")
    print(location)
