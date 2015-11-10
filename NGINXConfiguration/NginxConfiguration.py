from NGINXConfiguration.NginxBackend import NginxBackend
from NGINXConfiguration.NginxBackendServer import NginxBackendServer
from NGINXConfiguration.NginxBackendServerParameters import NginxBackendServerParameters
from NGINXConfiguration.NginxFrontend import NginxFrontend
from NGINXConfiguration.NginxServerLocation import NginxServerLocation

__author__ = 'Fabrice Servais'


class NginxConfiguration:

    def __init__(self, frontend=None, backends=None):
        """
        Constructor.
        :param frontend: Type: NginxFrontend, Frontend
        :param backends: Type: NginxBackend or List<NginxBackend>, Backend(s)
        :return:
        """
        self.frontend = frontend

        if backends is not None:
            if type(backends) is not list:
                self.backends = [backends]
            else:
                self.backends = backends
        else:
            self.backends = []

    def set_frontend_config(self, frontend_config):
        """
        Set the configuration of the frontend server
        :param frontend_config: Type: NginxFrontend, configuration of the frontend
        """
        self.frontend = frontend_config

    def add_backend(self, backend):
        """Add a 'backend' block, i.e. a backend pool
        :param backend: Type: NginxBackend, backend (= 'upstream')
        """
        self.backends.append(backend)

    def add_backends(self, backends):
        """Add a list of 'backends' blocks, i.e. a backend pool
        :param backends: Type: List<NginxBackend>, backends (= 'upstream')
        """
        self.backends.extend(backends)

    def __str__(self):
        return "{}".format({'http': {'frontend' : self.frontend, 'backends': self.backends}})

    def __repr__(self):
        return str(self)

    def export(self):
        """
        Generate the String containing the corresponding configuration for NGINX.
        :return: String of the configuration, usable by NGINX.
        """
        front = [str(self.frontend.export())] if self.frontend is not None else []
        back = [str(backend.export()) for backend in self.backends]

        content = front + back

        return '\n'.join(content)


if __name__ == "__main__":
    loc = NginxServerLocation("backend", '/')
    frontend = NginxFrontend()
    frontend.add_location(loc)

    back1 = NginxBackend()
    b_serv1 = NginxBackendServer(address="127.0.0.1", port=80)
    b_serv1.set_parameters(NginxBackendServerParameters(backup=True, max_fails=3, weight=3))
    back1.add_backend_server(b_serv1)

    config = NginxConfiguration(frontend=frontend, backends=back1)

    print(config)
    print(config.export())