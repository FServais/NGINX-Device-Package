from NGINXConfiguration.NginxBackend import NginxBackend
from NGINXConfiguration.NginxBackendServer import NginxBackendServer
from NGINXConfiguration.NginxBackendServerParameters import NginxBackendServerParameters
from NGINXConfiguration.NginxConfiguration import NginxConfiguration
from NGINXConfiguration.NginxFrontend import NginxFrontend
from NGINXConfiguration.NginxServerListen import NginxServerListen
from NGINXConfiguration.NginxServerLocation import NginxServerLocation
from NginxExportConfiguration.Block import Block
from NginxExportConfiguration.Directive import Directive

__author__ = 'Fabrice Servais'


def file_exporter():

    def export(node):
        __SERVER_BLOCK__NAME = "server"
        __LISTEN_DIRECTIVE__NAME = "listen"
        __LOCATION_BLOCK_NAME = "location"
        __SERVER_DIRECTIVE_NAME = "server"
        __UPSTREAM_BLOCK_NAME = "upstream"
        __DEFAULT_LB_ALGORITHM = "round-robin"

        if isinstance(node, NginxConfiguration):
            front = [str(node.frontend.visit(file_exporter()))] if node.frontend is not None else []
            back = [str(backend.visit(file_exporter())) for backend in node.backends]

            content = front + back

            return '\n'.join(content)

        elif isinstance(node, NginxFrontend):
            block = Block(__SERVER_BLOCK__NAME)

            block.add_lines(node.listen.visit(file_exporter()))
            for location in node.locations:
                block.add_lines(location.visit(file_exporter()))

            return block

        elif isinstance(node, NginxServerListen):
            param = ""

            if node.address:
                param = "{}:".format(node.address)

            param = "{}{}".format(param, node.port)

            return Directive(__LISTEN_DIRECTIVE__NAME, param)

        elif isinstance(node, NginxServerLocation):
            block_parameters = []

            if node.modifier:
                block_parameters.append(node.modifier)

            block_parameters.append(node.uri)

            return Block(__LOCATION_BLOCK_NAME, block_parameters, Directive(node.pass_method, "{}://{}".format(
                "https" if node.https else "http", node.backend_name)))

        elif isinstance(node, NginxBackend):
            lines = []
            if node.method != __DEFAULT_LB_ALGORITHM:
                lines.append(Directive(node.method))

            lines.extend([server.visit(file_exporter()) for server in node.server_pool])
            return Block(__UPSTREAM_BLOCK_NAME, node.name, lines)

        elif isinstance(node, NginxBackendServer):
            parameters = ["{}:{}".format(node.address, node.port)]

            if node.params is not None:
                parameters.extend(node.params.visit(file_exporter()))

            return Directive(__SERVER_DIRECTIVE_NAME, parameters)

        elif isinstance(node, NginxBackendServerParameters):
            to_return = []

            if node.backup:
                to_return.append("backup")

            if node.down:
                to_return.append("down")

            if node.fail_timeout != -1:
                to_return.append("fail_timeout={}".format(node.fail_timeout))

            if node.max_fails != -1:
                to_return.append("max_fails={}".format(node.max_fails))

            if node.weight != -1:
                to_return.append("weight={}".format(node.weight))

            return to_return

        else:
            return ""

    return export