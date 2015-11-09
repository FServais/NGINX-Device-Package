from ExportConfiguration.Directive import Directive

__author__ = 'Fabrice Servais'


class Block:

    def __init__(self, name, parameters=None, lines=None):
        self.name = name

        if parameters is not None:
            if type(parameters) is not list:
                self.parameters = [parameters]
            else:
                self.parameters = parameters
        else:
            self.parameters = []

        self.lines = lines if lines is not None else []

    def add_parameters(self, *parameters):
        self.parameters.extend(list(parameters))

    def add_lines(self, *lines):
        self.lines.extend(list(lines))

    def __str__(self):
        # First line
        header = ' '.join([self.name] + self.parameters + ['{'])

        # Content
        content = '\n'.join([str(l) for l in self.lines])
        # Add tabulation
        content = '\t' + content.replace('\n', '\n\t')

        # Last line
        footer = '}'

        return "{}\n{}\n{}".format(header, content, footer)

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    upstr = Block("upstream", ["backend", "option"])
    server1 = Directive("server", ["10.9.217.1:80", 'backup'])
    server2 = Directive("server", "10.9.217.2:80")
    upstr.add_lines(server1, server2)

    serverBlock = Block("server")
    locationBlock = Block("location", "/")
    locationBlock.add_lines(Directive("proxy_pass", "http://backend"), Directive("health_check"))

    serverBlock.add_lines(locationBlock)

    print(upstr)
    print(serverBlock)
