from API.Configuration import Configuration
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

    @classmethod
    def from_configuration(cls, configuration):
        """

        :param configuration: Type API.Configuration or list<API.Configuration>
        :return:
        """

        if type(configuration) is list:
            front = None
            backends = []

            for config in configuration:
                if config.get_type() == 4:
                    if config.get_key() == "frontendServer":
                        front = NginxFrontend.from_configuration(config.get_value())
                    elif config.get_key() == "upstream":
                        backends.append(NginxBackend.from_configuration(config.get_value()))

            return NginxConfiguration(front, backends)

        elif configuration.get_type() == 0:
            return NginxConfiguration.from_configuration(configuration.get_value())

        print(configuration)
        return None


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
        return "{}".format({'http': {'frontend': self.frontend, 'backends': self.backends}})

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

    print("------------------------------------")

    nginxServiceAuditConfig = {(0, '', 5167): {'ackedstate': 0,
                 'ctxName': 'VRF_NG',
                 'dn': u'uni/vDev-[uni/tn-NGINX/lDevVip-NginxDevice]-tn-[uni/tn-NGINX]-ctx-VRF_NG',
                 'state': 1,
                 'tenant': 'NGINX',
                 'transaction': 0,
                 'txid': 10000,
                 'value': {(1, '', 52847): {'absGraph': 'NginxServiceGraph',
                                            'ackedstate': 0,
                                            'rn': u'vGrp-[uni/tn-NGINX/GraphInst_C-[uni/tn-NGINX/brc-NginxTestContractAllowAll]-G-[uni/tn-NGINX/AbsGraph-NginxServiceGraph]-S-[uni/tn-NGINX]]',
                                            'state': 1,
                                            'transaction': 0,
                                            'value': {(3, 'LoadBalancer', 'N1'): {'ackedstate': 0,
                                                                                  'state': 1,
                                                                                  'transaction': 0,
                                                                                  'value': {(2, 'external', 'consumer'): {'ackedstate': 0,
                                                                                                                          'state': 1,
                                                                                                                          'transaction': 0,
                                                                                                                          'value': {(9, '', 'NginxDevice_ext_2162688_32774'): {'ackedstate': 0,
                                                                                                                                                                               'state': 1,
                                                                                                                                                                               'target': 'NginxDevice_ext_2162688_32774',
                                                                                                                                                                               'transaction': 0}}},
                                                                                            (2, 'internal', 'provider'): {'ackedstate': 0,
                                                                                                                          'state': 1,
                                                                                                                          'transaction': 0,
                                                                                                                          'value': {(9, '', 'NginxDevice_ext_2162688_32774'): {'ackedstate': 0,
                                                                                                                                                                               'state': 1,
                                                                                                                                                                               'target': 'NginxDevice_ext_2162688_32774',
                                                                                                                                                                               'transaction': 0}}},
                                                                                            (4, 'frontendServerCfg', 'frontendServerCfg'): {'ackedstate': 0,
                                                                                                                                            'state': 1,
                                                                                                                                            'transaction': 0,
                                                                                                                                            'value': {(6, 'frontendServerRel', 'frontendServerRel'): {'ackedstate': 0,
                                                                                                                                                                                                      'state': 1,
                                                                                                                                                                                                      'target': 'frontendServer',
                                                                                                                                                                                                      'transaction': 0}}},
                                                                                            (4, 'upstreamCfg', 'upstreamCfg'): {'ackedstate': 0,
                                                                                                                                'state': 1,
                                                                                                                                'transaction': 0,
                                                                                                                                'value': {(6, 'upstreamRel', 'upstreamRel'): {'ackedstate': 0,
                                                                                                                                                                              'state': 1,
                                                                                                                                                                              'target': 'upstream',
                                                                                                                                                                              'transaction': 0}}}}}}},
                           (4, 'frontendServer', 'frontendServer'): {'ackedstate': 0,
                                                                     'state': 1,
                                                                     'transaction': 0,
                                                                     'value': {(4, 'listen', 'listen'): {'ackedstate': 0,
                                                                                                         'state': 1,
                                                                                                         'transaction': 0,
                                                                                                         'value': {(5, 'address', 'address'): {'ackedstate': 0,
                                                                                                                                               'state': 1,
                                                                                                                                               'transaction': 0,
                                                                                                                                               'value': '127.0.0.1'},
                                                                                                                   (5, 'port', 'port'): {'ackedstate': 0,
                                                                                                                                         'state': 1,
                                                                                                                                         'transaction': 0,
                                                                                                                                         'value': '80'}}},
                                                                               (4, 'location', 'location'): {'ackedstate': 0,
                                                                                                             'state': 1,
                                                                                                             'transaction': 0,
                                                                                                             'value': {(5, 'backend_name', 'backend_name'): {'ackedstate': 0,
                                                                                                                                                             'state': 1,
                                                                                                                                                             'transaction': 0,
                                                                                                                                                             'value': 'backend'},
                                                                                                                       (5, 'uri', 'uri'): {'ackedstate': 0,
                                                                                                                                           'state': 1,
                                                                                                                                           'transaction': 0,
                                                                                                                                           'value': '/'}}}}},
                           (4, 'upstream', 'upstream'): {'ackedstate': 0,
                                                         'state': 1,
                                                         'transaction': 0,
                                                         'value': {(4, 'server', 'web1'): {'ackedstate': 0,
                                                                                           'state': 1,
                                                                                           'transaction': 0,
                                                                                           'value': {(5, 'ip', 'ip'): {'ackedstate': 0,
                                                                                                                       'state': 1,
                                                                                                                       'transaction': 0,
                                                                                                                       'value': '127.0.0.1'},
                                                                                                     (5, 'port', 'port'): {'ackedstate': 0,
                                                                                                                           'state': 1,
                                                                                                                           'transaction': 0,
                                                                                                                           'value': '8001'}}},
                                                                   (4, 'server', 'web2'): {'ackedstate': 0,
                                                                                           'state': 1,
                                                                                           'transaction': 0,
                                                                                           'value': {(5, 'ip', 'ip'): {'ackedstate': 0,
                                                                                                                       'state': 1,
                                                                                                                       'transaction': 0,
                                                                                                                       'value': '127.0.0.1'},
                                                                                                     (5, 'port', 'port'): {'ackedstate': 0,
                                                                                                                           'state': 1,
                                                                                                                           'transaction': 0,
                                                                                                                           'value': '8002'}}},
                                                                   (5, 'upstreamName', 'upstreamName'): {'ackedstate': 0,
                                                                                                         'state': 1,
                                                                                                         'transaction': 0,
                                                                                                         'value': 'backend'}}},
                           (7, '', '2162688_32774'): {'ackedstate': 0,
                                                      'state': 1,
                                                      'tag': 2077,
                                                      'transaction': 0,
                                                      'type': 1},
                           (8, '', 'NginxDevice_ext_2162688_32774'): {'ackedstate': 0,
                                                                      'encap': '2162688_32774',
                                                                      'state': 1,
                                                                      'transaction': 0,
                                                                      'vif': 'NginxDevice_ext'},
                           (10, '', 'NginxDevice_ext'): {'ackedstate': 0,
                                                         'cifs': {'NginxDevice_Device_1': 'eth0'},
                                                         'state': 1,
                                                         'transaction': 0}}}}

    config_api = Configuration(nginxServiceAuditConfig)
    nginx_config = NginxConfiguration.from_configuration(config_api)
    print(nginx_config.export())