from API.Configuration import Configuration
from NGINXConfiguration.NginxBackend import NginxBackend
from NGINXConfiguration.NginxFrontend import NginxFrontend

__author__ = 'Fabrice Servais'


class NginxConfiguration:

    def __init__(self, frontends=None, backends=None, name="default", enabled=True):
        """
        Constructor.
        :param frontend: Type: NginxFrontend, Frontend
        :param backends: Type: NginxBackend or List<NginxBackend>, Backend(s)
        :return:
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

    @classmethod
    def from_configurations(cls, configurations):
        """

        :param configurations: Type list<API.Configuration>
        :return:
        """
        nginx_configurations = []
        if configurations.get_type() == 0:
            configs = configurations.get_value()

            for config in configs:
                if config.get_type() == 4 and config.get_key() == "configuration":
                    nginx_configurations.append(NginxConfiguration.from_configuration(config.get_value()))

        return nginx_configurations

    @classmethod
    def from_configuration(cls, configuration):
        """

        :param configuration: Type API.Configuration or list<API.Configuration>
        :return:
        """
        fronts = []
        backends = []
        name = "default"
        enabled = True

        for config in configuration:
            if config.get_type() == 4:

                if config.get_key() == "frontendServer":
                    fronts.append(NginxFrontend.from_configuration(config.get_value()))
                elif config.get_key() == "upstream":
                    backends.append(NginxBackend.from_configuration(config.get_value()))

            if config.get_type() == 5:
                # [(5, "name", ..) -> {}, (5, "enabled", ..) -> {}]
                if config.get_key() == "name":
                    name = config.get_value()
                elif config.get_key() == "enabled":
                    en = config.get_value()
                    if en is not None:
                        enabled = en.lower() == "true"

        return NginxConfiguration(fronts, backends, name, enabled)

    def add_frontend(self, frontend):
        """Add a 'frontend' block, i.e. a frontend pool
        :param frontend: Type: NginxFrontend, frontend
        """
        self.frontends.append(frontend)

    def add_frontends(self, frontends):
        """Add a list of 'frontends' blocks, i.e. a frontend pool
        :param frontends: Type: List<NginxFrontend>, frontends
        """
        self.frontends.extend(frontends)

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
        return "{}".format({'cfgParameters': {'name': self.name, 'enabled': self.enabled}, 'http': {'frontends': self.frontends, 'backends': self.backends}})

    def __repr__(self):
        return str(self)

    def export(self):
        """
        Generate the String containing the corresponding configuration for NGINX.
        :return: String of the configuration, usable by NGINX.
        """
        # front = [str(self.frontend.export())] if self.frontend is not None else []
        fronts = [str(frontend.export()) for frontend in self.frontends]
        back = [str(backend.export()) for backend in self.backends]

        content = fronts + back

        return '\n'.join(content)

    def visit(self, visitor):
        return visitor(self)
