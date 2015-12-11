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


if __name__ == "__main__":
    from Exporter.FileExporter import file_exporter

    # loc = NginxServerLocation("backend", '/')
    # frontend = NginxFrontend()
    # frontend.add_location(loc)
    #
    # back1 = NginxBackend()
    # b_serv1 = NginxBackendServer(address="127.0.0.1", port=80)
    # b_serv1.set_parameters(NginxBackendServerParameters(backup=True, max_fails=3, weight=3))
    # back1.add_backend_server(b_serv1)
    #
    # config = NginxConfiguration(frontend=frontend, backends=back1)
    #
    # print(config)
    # print(config.export())

    print("------------------------------------")

    nginx_service_modify = {(0, '', 32847): {'dn': u'uni/vDev-[uni/tn-NGINX/lDevVip-NginxLoadBalancer]-tn-[uni/tn-NGINX]-ctx-VRF_NG', 'transaction': 0, 'ackedstate': None, 'value': {(1, '', 12099): {'transaction': 0, 'ackedstate': None, 'value': {(3, 'LoadBalancer', 'NG'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(2, 'external', 'consumer'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(9, '', 'NginxLoadBalancer_client_2129920_32771'): {'state': 3, 'transaction': 0, 'target': 'NginxLoadBalancer_client_2129920_32771', 'ackedstate': None}}}, (4, 'configuration', 'Configuration'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(4, 'upstreamCfg', 'upstreamCfg'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(6, 'upstreamRel', 'upstreamRel'): {'state': 3, 'transaction': 0, 'target': 'upstream', 'ackedstate': None}}}, (5, 'name', 'name'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': 'loadBalancing'}, (4, 'frontendServerCfg', 'frontendServerCfg'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(6, 'frontendServerRel', 'frontendServerRel'): {'state': 3, 'transaction': 0, 'target': 'frontendServer', 'ackedstate': None}}}}}, (2, 'internal', 'provider'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(9, '', 'NginxLoadBalancer_pool_2129920_32772'): {'state': 3, 'transaction': 0, 'target': 'NginxLoadBalancer_pool_2129920_32772', 'ackedstate': None}}}}}}, 'state': 3, 'absGraph': 'NginxLB_SG', 'rn': u'vGrp-[uni/tn-NGINX/GraphInst_C-[uni/tn-NGINX/brc-NginxLB_Contract]-G-[uni/tn-NGINX/AbsGraph-NginxLB_SG]-S-[uni/tn-NGINX]]'}, (8, '', 'NginxLoadBalancer_client_2129920_32771'): {'state': 3, 'transaction': 0, 'vif': 'NginxLoadBalancer_client', 'ackedstate': None, 'encap': '2129920_32771'}, (8, '', 'NginxLoadBalancer_pool_2129920_32772'): {'state': 3, 'transaction': 0, 'vif': 'NginxLoadBalancer_pool', 'ackedstate': None, 'encap': '2129920_32772'}, (10, '', 'NginxLoadBalancer_client'): {'state': 3, 'transaction': 0, 'cifs': {'NginxLoadBalancer_Device_1': 'eth0'}, 'ackedstate': None}, (7, '', '2129920_32771'): {'state': 3, 'tag': 2072, 'type': 1, 'ackedstate': None, 'transaction': 0}, (10, '', 'NginxLoadBalancer_pool'): {'state': 3, 'transaction': 0, 'cifs': {'NginxLoadBalancer_Device_1': 'eth2'}, 'ackedstate': None}, (4, 'upstream', 'upstream'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(4, 'server', 'web2'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(5, 'port', 'port'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': '80'}, (5, 'ip', 'ip'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': '10.9.218.2'}}}, (4, 'server', 'web1'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(5, 'port', 'port'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': '80'}, (5, 'ip', 'ip'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': '10.9.218.1'}}}, (5, 'upstreamName', 'upstreamName'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': 'backend'}}}, (7, '', '2129920_32772'): {'state': 3, 'tag': 2004, 'type': 1, 'ackedstate': None, 'transaction': 0}, (4, 'frontendServer', 'frontendServer'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(4, 'listen', 'listen'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(5, 'address', 'address'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': '10.9.217.1'}, (5, 'port', 'port'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': '80'}}}, (4, 'location', 'location'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': {(5, 'backend_name', 'backend_name'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': 'backend'}, (5, 'uri', 'uri'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': '/'}}}}}}, 'txid': 10001, 'state': 3, 'ctxName': 'VRF_NG', 'tenant': 'NGINX'}}

    # nginxServiceAuditConfig = {(0, '', 5167): {'ackedstate': 0,
    #              'ctxName': 'VRF_NG',
    #              'dn': u'uni/vDev-[uni/tn-NGINX/lDevVip-NginxDevice]-tn-[uni/tn-NGINX]-ctx-VRF_NG',
    #              'state': 1,
    #              'tenant': 'NGINX',
    #              'transaction': 0,
    #              'txid': 10000,
    #              'value': {(1, '', 52847): {'absGraph': 'NginxServiceGraph',
    #                                         'ackedstate': 0,
    #                                         'rn': u'vGrp-[uni/tn-NGINX/GraphInst_C-[uni/tn-NGINX/brc-NginxTestContractAllowAll]-G-[uni/tn-NGINX/AbsGraph-NginxServiceGraph]-S-[uni/tn-NGINX]]',
    #                                         'state': 1,
    #                                         'transaction': 0,
    #                                         'value': {(3, 'LoadBalancer', 'N1'): {'ackedstate': 0,
    #                                                                               'state': 1,
    #                                                                               'transaction': 0,
    #                                                                               'value': {(2, 'external', 'consumer'): {'ackedstate': 0,
    #                                                                                                                       'state': 1,
    #                                                                                                                       'transaction': 0,
    #                                                                                                                       'value': {(9, '', 'NginxDevice_ext_2162688_32774'): {'ackedstate': 0,
    #                                                                                                                                                                            'state': 1,
    #                                                                                                                                                                            'target': 'NginxDevice_ext_2162688_32774',
    #                                                                                                                                                                            'transaction': 0}}},
    #                                                                                         (2, 'internal', 'provider'): {'ackedstate': 0,
    #                                                                                                                       'state': 1,
    #                                                                                                                       'transaction': 0,
    #                                                                                                                       'value': {(9, '', 'NginxDevice_ext_2162688_32774'): {'ackedstate': 0,
    #                                                                                                                                                                            'state': 1,
    #                                                                                                                                                                            'target': 'NginxDevice_ext_2162688_32774',
    #                                                                                                                                                                            'transaction': 0}}},
    #                                                                                         (4, 'frontendServerCfg', 'frontendServerCfg'): {'ackedstate': 0,
    #                                                                                                                                         'state': 1,
    #                                                                                                                                         'transaction': 0,
    #                                                                                                                                         'value': {(6, 'frontendServerRel', 'frontendServerRel'): {'ackedstate': 0,
    #                                                                                                                                                                                                   'state': 1,
    #                                                                                                                                                                                                   'target': 'frontendServer',
    #                                                                                                                                                                                                   'transaction': 0}}},
    #                                                                                         (4, 'upstreamCfg', 'upstreamCfg'): {'ackedstate': 0,
    #                                                                                                                             'state': 1,
    #                                                                                                                             'transaction': 0,
    #                                                                                                                             'value': {(6, 'upstreamRel', 'upstreamRel'): {'ackedstate': 0,
    #                                                                                                                                                                           'state': 1,
    #                                                                                                                                                                           'target': 'upstream',
    #                                                                                                                                                                           'transaction': 0}}}}}}},
    #                        (4, 'configuration', 'Configuration'): {'ackedstate': 0,
    #                                                                'state': 1,
    #                                                                'transaction': 0,
    #                                                                'value': {(4, 'frontendServer', 'frontendServer'): {'ackedstate': 0,
    #                                                                                                                    'state': 1,
    #                                                                                                                    'transaction': 0,
    #                                                                                                                    'value': {(4, 'listen', 'listen'): {'ackedstate': 0,
    #                                                                                                                                                        'state': 1,
    #                                                                                                                                                        'transaction': 0,
    #                                                                                                                                                        'value': {(5, 'address', 'address'): {'ackedstate': 0,
    #                                                                                                                                                                                              'state': 1,
    #                                                                                                                                                                                              'transaction': 0,
    #                                                                                                                                                                                              'value': '127.0.0.1'},
    #                                                                                                                                                                  (5, 'port', 'port'): {'ackedstate': 0,
    #                                                                                                                                                                                        'state': 1,
    #                                                                                                                                                                                        'transaction': 0,
    #                                                                                                                                                                                        'value': '80'}}},
    #                                                                                                                              (4, 'location', 'location'): {'ackedstate': 0,
    #                                                                                                                                                            'state': 1,
    #                                                                                                                                                            'transaction': 0,
    #                                                                                                                                                            'value': {(5, 'backend_name', 'backend_name'): {'ackedstate': 0,
    #                                                                                                                                                                                                            'state': 1,
    #                                                                                                                                                                                                            'transaction': 0,
    #                                                                                                                                                                                                            'value': 'backend'},
    #                                                                                                                                                                      (5, 'uri', 'uri'): {'ackedstate': 0,
    #                                                                                                                                                                                          'state': 1,
    #                                                                                                                                                                                          'transaction': 0,
    #                                                                                                                                                                                          'value': '/'}}}}},
    #                                                                          (4, 'upstream', 'upstream'): {'ackedstate': 0,
    #                                                                                                        'state': 1,
    #                                                                                                        'transaction': 0,
    #                                                                                                        'value': {(4, 'server', 'web1'): {'ackedstate': 0,
    #                                                                                                                                          'state': 1,
    #                                                                                                                                          'transaction': 0,
    #                                                                                                                                          'value': {(5, 'ip', 'ip'): {'ackedstate': 0,
    #                                                                                                                                                                      'state': 1,
    #                                                                                                                                                                      'transaction': 0,
    #                                                                                                                                                                      'value': '127.0.0.1'},
    #                                                                                                                                                    (5, 'port', 'port'): {'ackedstate': 0,
    #                                                                                                                                                                          'state': 1,
    #                                                                                                                                                                          'transaction': 0,
    #                                                                                                                                                                          'value': '8001'}}},
    #                                                                                                                  (4, 'server', 'web2'): {'ackedstate': 0,
    #                                                                                                                                          'state': 1,
    #                                                                                                                                          'transaction': 0,
    #                                                                                                                                          'value': {(5, 'ip', 'ip'): {'ackedstate': 0,
    #                                                                                                                                                                      'state': 1,
    #                                                                                                                                                                      'transaction': 0,
    #                                                                                                                                                                      'value': '127.0.0.1'},
    #                                                                                                                                                    (5, 'port', 'port'): {'ackedstate': 0,
    #                                                                                                                                                                          'state': 1,
    #                                                                                                                                                                          'transaction': 0,
    #                                                                                                                                                                          'value': '8002'}}},
    #                                                                                                                  (5, 'upstreamName', 'upstreamName'): {'ackedstate': 0,
    #                                                                                                                                                        'state': 1,
    #                                                                                                                                                        'transaction': 0,
    #                                                                                                                                                        'value': 'backend'}}},
    #                                                                          (5, 'enabled', 'enabled'): {'ackedstate': 0,
    #                                                                                                      'state': 1,
    #                                                                                                      'transaction': 0,
    #                                                                                                      'value': 'True'},
    #                                                                          (5, 'name', 'name'): {'ackedstate': 0,
    #                                                                                                'state': 1,
    #                                                                                                'transaction': 0,
    #                                                                                                'value': 'default'}}},
    #                        (7, '', '2162688_32774'): {'ackedstate': 0,
    #                                                   'state': 1,
    #                                                   'tag': 2077,
    #                                                   'transaction': 0,
    #                                                   'type': 1},
    #                        (8, '', 'NginxDevice_ext_2162688_32774'): {'ackedstate': 0,
    #                                                                   'encap': '2162688_32774',
    #                                                                   'state': 1,
    #                                                                   'transaction': 0,
    #                                                                   'vif': 'NginxDevice_ext'},
    #                        (10, '', 'NginxDevice_ext'): {'ackedstate': 0,
    #                                                      'cifs': {'NginxDevice_Device_1': 'eth0'},
    #                                                      'state': 1,
    #                                                      'transaction': 0}}}}

    config_api = Configuration(nginx_service_modify)
    nginx_configs = NginxConfiguration.from_configurations(config_api)

    for c in nginx_configs:
        print("Configuration '{}' ({}): ".format(c.name, "Enabled" if c.enabled else "Disabled"))
        print(c.export())

        # print("--------------- FILE EXPORTER ----------------------")
        # Does not work, try with the 'Test.py' file to test the export
        # print(c.visit(file_exporter()))
