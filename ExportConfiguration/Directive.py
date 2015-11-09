__author__ = 'Fabrice Servais'


class Directive:

    def __init__(self, name, parameters=None):
        self.name = name

        if parameters is not None:
            if type(parameters) is not list:
                self.parameters = [parameters]
            else:
                self.parameters = parameters
        else:
            self.parameters = []

    def __str__(self):
        to_return = [self.name] + self.parameters
        return ' '.join(to_return) + ';'

    def __repr__(self):
        return str(self)
