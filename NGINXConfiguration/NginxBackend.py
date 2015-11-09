from NGINXConfiguration.NginxBackendServer import NginxBackendServer
from NGINXConfiguration.NginxBackendServerParameters import NginxBackendServerParameters

__author__ = 'Fabrice Servais'


class NginxBackend:
    __UPSTREAM_BLOCK_NAME = "upstream"

    def __init__(self, method="round-robin", name="backend", server_pool=[]):
        self.method = method
        self.name = name
        self.server_pool = server_pool

    def add_backend_server(self, backend_server):
        """Add a backend server
        :param backend_server: Type: NginxBackendServer
        """
        self.server_pool.append(backend_server)

    def __str__(self):
        return "{}".format({'method': self.method, 'name': self.name, 'server_pool': self.server_pool})

    def __repr__(self):
        return str(self)

    def export(self):
        from ExportConfiguration.Block import Block
        return Block(self.__UPSTREAM_BLOCK_NAME, "backend", [server.export() for server in self.server_pool])

if __name__ == "__main__":
    back1 = NginxBackend()
    b_serv1 = NginxBackendServer(address="127.0.0.1", port=80, params=NginxBackendServerParameters(backup=True, max_fails=3))

    back1.add_backend_server(b_serv1)

    print(back1)
    print(back1.export())