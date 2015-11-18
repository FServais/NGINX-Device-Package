from NGINXConfiguration.NginxBackendServer import NginxBackendServer
from NGINXConfiguration.NginxBackendServerParameters import NginxBackendServerParameters

__author__ = 'Fabrice Servais'


class NginxBackend:
    __UPSTREAM_BLOCK_NAME = "upstream"
    __DEFAULT_LB_ALGORITHM = "round-robin"

    def __init__(self, method=__DEFAULT_LB_ALGORITHM, name="backend", server_pool=None):
        """
        Constructor.
        :param method: Load balancing algorithm
        :param name: Name of the backend
        :param server_pool: Type: NginxBackendServer or List<NginxBackendServer>, list of servers in the backend.
        """

        self.method = method
        self.name = name

        if server_pool is not None:
            if type(server_pool) is not list:
                self.server_pool = [server_pool]
            else:
                self.server_pool = server_pool
        else:
            self.server_pool = []

    @classmethod
    def from_configuration(cls, configuration):
        method = cls.__DEFAULT_LB_ALGORITHM
        name = "backend"
        server_pool = []

        for config in configuration:
            if config.get_key() == "upstreamName":
                name = config.get_value()
            elif config.get_key() == "lbalgo":
                method = config.get_value()
            elif config.get_key() == "server":
                server_pool.append(NginxBackendServer.from_configuration(config.get_value()))

        return NginxBackend(method, name, server_pool)

    def add_backend_server(self, backend_server):
        """
        Add a backend server
        :param backend_server: Type: NginxBackendServer
        """
        self.server_pool.append(backend_server)

    def add_backend_servers(self, backend_servers):
        """
        Add a list of backend servers
        :param backend_servers: Type: List<NginxBackendServer>
        """
        self.server_pool.extend(backend_servers)

    def __str__(self):
        return "{}".format({'method': self.method, 'name': self.name, 'server_pool': self.server_pool})

    def __repr__(self):
        return str(self)

    def export(self):
        from NginxExportConfiguration.Block import Block
        from NginxExportConfiguration.Directive import Directive
        lines = []
        if self.method != self.__DEFAULT_LB_ALGORITHM:
            lines.append(Directive(self.method))

        lines.extend([server.export() for server in self.server_pool])
        return Block(self.__UPSTREAM_BLOCK_NAME, self.name, lines)


if __name__ == "__main__":
    backend = NginxBackend(method="ip-hash")
    backend_server1 = NginxBackendServer(address="127.0.0.1", port=80,
                                         params=NginxBackendServerParameters(backup=True, max_fails=3))
    backend_server2 = NginxBackendServer(address="0.0.0.0", port=2354)
    backend_server3 = NginxBackendServer(address="10.10.10.10")

    backend.add_backend_servers([backend_server1, backend_server2])
    backend.add_backend_server(backend_server3)

    print(backend)
    print(backend.export())
