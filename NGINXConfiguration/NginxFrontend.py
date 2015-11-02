__author__ = 'Fabrice Servais'


class NginxFrontend:

    def __init__(self):
        self.locations = []

    def add_location(self, location):
        """Add a 'location' block to the (frontend) server block.

        :param location: Type: NginxServerLocation, 'location' block
        """
        self.locations.append(location)

    def __str__(self):
        return "{{ 'locations': {} }}".format(self.locations)

    def __repr__(self):
        return str(self)