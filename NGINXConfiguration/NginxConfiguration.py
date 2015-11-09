from NGINXConfiguration.NginxBackend import NginxBackend
from NGINXConfiguration.NginxBackendServer import NginxBackendServer
from NGINXConfiguration.NginxBackendServerParameters import NginxBackendServerParameters
from NGINXConfiguration.NginxFrontend import NginxFrontend
from NGINXConfiguration.NginxServerLocation import NginxServerLocation

__author__ = 'Fabrice Servais'


class NginxConfiguration:

    def __init__(self, frontend=None, backends=[]):
        self.frontend = frontend
        self.backends = backends

    def set_frontend_config(self, frontend_config):
        """Set the configuration of the frontend server

        :param frontend_config: Type: NginxFrontend, configuration of the frontend
        """
        self.frontend = frontend_config

    def add_backend(self, backend):
        """Add a 'backend' block, i.e. a backend pool
        :param backend: Type: NginxBackend, backend (= 'upstream')
        """
        self.backends.append(backend)

    def __str__(self):
        return "{}".format({'http': {'frontend' : self.frontend, 'backends': self.backends}})

    def __repr__(self):
        return str(self)

    def export(self):
        return '\n'.join([str(self.frontend.export())] + [str(backend.export()) for backend in self.backends])


if __name__ == "__main__":
    loc = NginxServerLocation("backend", '/')
    frontend = NginxFrontend()
    frontend.add_location(loc)

    back1 = NginxBackend()
    b_serv1 = NginxBackendServer(address="127.0.0.1", port=80)
    b_serv1.set_parameters(NginxBackendServerParameters(backup=True, max_fails=3, weight=3))
    back1.add_backend_server(b_serv1)

    config = NginxConfiguration(frontend=frontend, backends=[back1])

    print(config)
    print(config.export())