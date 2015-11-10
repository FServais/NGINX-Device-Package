from NGINXConfiguration.NginxServerLocation import NginxServerLocation

__author__ = 'Fabrice Servais'


class NginxFrontend:
    __LISTEN_DIRECTIVE__NAME = "listen"
    __SERVER_BLOCK__NAME = "server"

    def __init__(self, listen_port=80, locations=None):
        """
        Constructor.
        :param listen_port: Listening port of the server (frontend).
        :param locations: Type: NginxServerLocation or List<NginxServerLocation>, list of 'location' directives.
        """
        if locations is not None:
            if type(locations) is not list:
                self.locations = [locations]
            else:
                self.locations = locations
        else:
            self.locations = []

        self.listen_port = listen_port

    def add_location(self, location):
        """
        Add a 'location' block to the (frontend) server block.

        :param location: Type: NginxServerLocation, 'location' block
        """
        self.locations.append(location)

    def __str__(self):
        return "{}".format({'locations': self.locations, 'listen_port': self.listen_port})

    def __repr__(self):
        return str(self)

    def export(self):
        from NginxExportConfiguration.Block import Block
        block = Block(self.__SERVER_BLOCK__NAME)

        from NginxExportConfiguration.Directive import Directive
        block.add_lines(Directive(self.__LISTEN_DIRECTIVE__NAME, self.listen_port))
        for location in self.locations:
            block.add_lines(location.export())

        return block


if __name__ == "__main__":
    frontend = NginxFrontend(locations=NginxServerLocation("backend", '/'))

    print(frontend)
    print(frontend.export())