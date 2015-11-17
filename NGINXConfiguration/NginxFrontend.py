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

    def export(self):
        from NginxExportConfiguration.Block import Block
        block = Block(self.__SERVER_BLOCK__NAME)

        from NginxExportConfiguration.Directive import Directive
        block.add_lines(self.listen.export())
        for location in self.locations:
            block.add_lines(location.export())

        return block


if __name__ == "__main__":
    frontend = NginxFrontend(locations=NginxServerLocation("backend", '/'))

    print(frontend)
    print(frontend.export())