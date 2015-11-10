__author__ = 'Fabrice Servais'


class Directive:
    """
    Class that represents a directive (i.e. a line) in a NGINX configuration file.
    Example:
        upstream backend {
            server backend1.example.com       weight=5;
            server backup2.example.com:8080   backup;
        }

        Here, there are 2 directives :
        - server backend1.example.com weight=5;
        - server backup2.example.com:8080 backup;

    A Directive is composed of a 'name' (e.g. "server") and an optional set of 'parameters'
    (e.g. ["backend1.example.com", "weight=5"]) that will be separated by a space. A Directive also ends by a ';'.

    Examples of usage:
        - Directive("server", "server1.example.com") corresponds to "server server1.example.com;"
        - Directive("server", ["server1.example.com", "backup"]) corresponds to "server server1.example.com backup;"
    """
    def __init__(self, name, parameters=None):
        self.name = name

        if parameters is not None:
            if type(parameters) is not list:
                self.parameters = [parameters]
            else:
                self.parameters = parameters
        else:
            self.parameters = []

    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    def add_parameters(self, parameters):
        self.parameters.extend(parameters)

    def __str__(self):
        to_return = [self.name] + map(str, self.parameters)
        return ' '.join(to_return) + ';'

    def __repr__(self):
        return str(self)
