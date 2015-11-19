from NginxExportConfiguration.Directive import Directive

__author__ = 'Fabrice Servais'


class Block:
    """
    Class that represents a block in a NGINX configuration file.
    Example:
        upstream backend {
            server backend1.example.com       weight=5;
            server backup2.example.com:8080   backup;
        }

        Here, there is one block (upstream).

    A Block is composed of a 'name', an optional set of 'parameters' (or single parameter), and a content (= 'lines')
    either of type 'Directive' or 'Block'.

    Examples of usage:
        - Block("upstream", "backend") corresponds to:
            upstream backend {

            }
        - Block(name="block1", lines=[Directive("command", "argument"), Block("block2", "inside")]) corresponds to:
            block1 {
                command argument;
                block2 inside {

                }
            }
    """

    def __init__(self, name, parameters=None, lines=None):
        self.name = name

        if parameters is not None:
            if type(parameters) is not list:
                self.parameters = [parameters]
            else:
                self.parameters = parameters
        else:
            self.parameters = []

        if lines is not None:
            if type(lines) is not list:
                self.lines = [lines]
            else:
                self.lines = lines
        else:
            self.lines = []

    def add_parameters(self, *parameters):
        self.parameters.extend(list(parameters))

    def add_lines(self, *lines):
        self.lines.extend(list(lines))

    def __str__(self):
        # First line
        header = ' '.join([self.name] + map(str, self.parameters) + ['{'])

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
    upstream = Block("upstream", ["backend", "option"])
    server1 = Directive("server", ["10.9.217.1:80", 'backup'])
    server2 = Directive("server", "10.9.217.2:80")
    upstream.add_lines(server1, server2)

    serverBlock = Block("server")
    locationBlock = Block("location", "/")
    locationBlock.add_lines(Directive("proxy_pass", "http://backend"), Directive("health_check"))

    serverBlock.add_lines(locationBlock)

    print(upstream)
    print(serverBlock)
