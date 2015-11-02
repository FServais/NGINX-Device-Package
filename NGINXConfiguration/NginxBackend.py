__author__ = 'Fabrice Servais'


class NginxBackend:

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
        return "{{ 'method': '{method}', 'name': '{name}', 'server_pool': {pool} }}".format(method=self.method, name=self.name, pool=map(lambda x: eval(x.__str__()), self.server_pool))

    def __repr__(self):
        return str(self)