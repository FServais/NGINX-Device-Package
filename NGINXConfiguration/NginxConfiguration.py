from API.Configuration import Configuration
from NGINXConfiguration.NginxBackend import NginxBackend
from NGINXConfiguration.NginxFrontend import NginxFrontend

__author__ = 'Fabrice Servais'


class NginxConfiguration:
    def __init__(self, frontends=None, backends=None, name="default", enabled=True):
        """
        Args:
            frontends: (NginxFrontend or List<Frontend>) Frontend(s)
            backends: (NginxBackend or List<NginxBackend>) Backend(s)
            name: (String) Name of the NGINX configuration.
            enabled: (Boolean) True if the configuration is enabled.
        """
        if frontends is not None:
            if type(frontends) is not list:
                self.frontends = [frontends]
            else:
                self.frontends = frontends
        else:
            self.frontends = []

        if backends is not None:
            if type(backends) is not list:
                self.backends = [backends]
            else:
                self.backends = backends
        else:
            self.backends = []

        self.name = name
        self.enabled = enabled

    def add_frontend(self, frontend):
        """
        Add a 'frontend' block, i.e. a frontend pool

        Args:
            frontend: (NginxFrontend) frontend

        """
        self.frontends.append(frontend)

    def add_frontends(self, frontends):
        """
        Add a list of 'frontends' blocks, i.e. a frontend pool

        Args:
            frontends: (List<NginxFrontend>) frontends

        """
        self.frontends.extend(frontends)

    def add_backend(self, backend):
        """
        Add a 'backend' block, i.e. a backend server pool
        Args:
            backend: (NginxBackend) backend (= 'upstream')

        """
        self.backends.append(backend)

    def add_backends(self, backends):
        """
        Add a list of 'backends' blocks
        Args:
            backends: (List<NginxBackend>) backends (= 'upstream')

        Returns:

        """
        self.backends.extend(backends)

    def get_backends(self):
        return self.backends

    def __str__(self):
        return "{}".format({'cfgParameters': {'name': self.name, 'enabled': self.enabled},
                            'http': {'frontends': self.frontends, 'backends': self.backends}})

    def __repr__(self):
        return str(self)

    def accept(self, visitor):
        """
        Method used to apply a function 'visitor' on the entire structure representing the configuration.

        Args:
            visitor: function (1 argument) to apply

        Returns: The result of the application of the function 'visitor' with the instance as the parameter.

        """
        return visitor(self)

