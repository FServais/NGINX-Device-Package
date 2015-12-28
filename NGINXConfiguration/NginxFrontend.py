from API.Configuration import Configuration
from NGINXConfiguration.NginxServerListen import NginxServerListen
from NGINXConfiguration.NginxServerLocation import NginxServerLocation

__author__ = 'Fabrice Servais'


class NginxFrontend:
    __SERVER_BLOCK__NAME = "server"

    def __init__(self, listen=None, locations=None):
        """
        Constructor.
        :param listen: Type: NginxServerListen, 'listen' directive of the server block.
        :param locations: Type: NginxServerLocation or List<NginxServerLocation>, list of 'location' directives.
        """
        if locations:
            if type(locations) is not list:
                self.locations = [locations]
            else:
                self.locations = locations
        else:
            self.locations = []

        if listen is None:
            self.listen = NginxServerListen(port=80)
        else:
            self.listen = listen

    @classmethod
    def from_configuration(self, configuration):
        """

        :param configuration: Type list<API.Configuration>
        :return:
        """
        locations = []
        listen = None

        for config in configuration:
            if config.get_key() == "listen":
                listen = NginxServerListen.from_configuration(config.get_value())
            elif config.get_key() == "location":
                locations.append(NginxServerLocation.from_configuration(config.get_value()))

        return NginxFrontend(listen, locations)

    def add_location(self, location):
        """
        Add a 'location' block to the (frontend) server block.

        :param location: Type: NginxServerLocation, 'location' block
        """
        self.locations.append(location)

    def __str__(self):
        return "{}".format({'locations': self.locations, 'listen': self.listen})

    def __repr__(self):
        return str(self)

    def accept(self, visitor):
        return visitor(self)


if __name__ == "__main__":
    frontend = NginxFrontend(locations=NginxServerLocation("backend", '/'))

    print(frontend)

    frontend2 = NginxFrontend([Configuration({(4, 'listen', 'listen'): {'state': 1, 'transaction': 0, 'ackedstate': 0, 'value': {(5, 'address', 'address'): {'state': 1, 'transaction': 0, 'ackedstate': 0, 'value': '127.0.0.1'}, (5, 'port', 'port'): {'state': 1, 'transaction': 0, 'ackedstate': 0, 'value': '80'}}}}
),
                               Configuration({(4, 'location', 'location'): {'state': 1, 'transaction': 0, 'ackedstate': 0, 'value': {(5, 'backend_name', 'backend_name'): {'state': 1, 'transaction': 0, 'ackedstate': 0, 'value': 'backend'}, (5, 'uri', 'uri'): {'state': 1, 'transaction': 0, 'ackedstate': 0, 'value': '/'}}}}
)])
    print(frontend2)