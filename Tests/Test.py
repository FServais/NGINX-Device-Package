# ===== Service modify
# Arguments
from API.Configuration import Configuration
from Exporter.FileExporter import file_exporter
from NGINXConfiguration.NginxConfigurationFactory import NginxConfigurationFactory
from NGINXConfiguration.NginxConfiguration import NginxConfiguration
from NginxDevice import NginxDevice

device = {'name': 'NginxLoadBalancer', 'virtual': True, 'devs': {'NginxLoadBalancer_Device_1': {'creds': {'username': 'fservais', 'password': '<hidden>'}, 'host': '10.9.14.73', 'port': 80, 'virtual': True}}, 'host': '10.9.14.73', 'contextaware': False, 'port': 80, 'creds': {'username': 'fservais', 'password': '<hidden>'}}
configuration = {(0, '', 32847): {'ackedstate': None,
                  'ctxName': 'VRF_NG',
                  'dn': u'uni/vDev-[uni/tn-NGINX/lDevVip-NginxLoadBalancer]-tn-[uni/tn-NGINX]-ctx-VRF_NG',
                  'state': 3,
                  'tenant': 'NGINX',
                  'transaction': 0,
                  'txid': 10001,
                  'value': {(1, '', 12099): {'absGraph': 'NginxLB_SG',
                                             'ackedstate': None,
                                             'rn': u'vGrp-[uni/tn-NGINX/GraphInst_C-[uni/tn-NGINX/brc-NginxLB_Contract]-G-[uni/tn-NGINX/AbsGraph-NginxLB_SG]-S-[uni/tn-NGINX]]',
                                             'state': 3,
                                             'transaction': 0,
                                             'value': {(3, 'LoadBalancer', 'NG'): {'ackedstate': None,
                                                                                   'state': 3,
                                                                                   'transaction': 0,
                                                                                   'value': {(2, 'external', 'consumer'): {'ackedstate': None,
                                                                                                                           'state': 3,
                                                                                                                           'transaction': 0,
                                                                                                                           'value': {(9, '', 'NginxLoadBalancer_client_2129920_32771'): {'ackedstate': None,
                                                                                                                                                                                         'state': 3,
                                                                                                                                                                                         'target': 'NginxLoadBalancer_client_2129920_32771',
                                                                                                                                                                                         'transaction': 0}}},
                                                                                             (2, 'internal', 'provider'): {'ackedstate': None,
                                                                                                                           'state': 3,
                                                                                                                           'transaction': 0,
                                                                                                                           'value': {(9, '', 'NginxLoadBalancer_pool_2129920_32772'): {'ackedstate': None,
                                                                                                                                                                                       'state': 3,
                                                                                                                                                                                       'target': 'NginxLoadBalancer_pool_2129920_32772',
                                                                                                                                                                                       'transaction': 0}}},
                                                                                             (4, 'configuration', 'Configuration'): {'ackedstate': None,
                                                                                                                                     'state': 3,
                                                                                                                                     'transaction': 0,
                                                                                                                                     'value': {(4, 'frontendServerCfg', 'frontendServerCfg'): {'ackedstate': None,
                                                                                                                                                                                               'state': 3,
                                                                                                                                                                                               'transaction': 0,
                                                                                                                                                                                               'value': {(6, 'frontendServerRel', 'frontendServerRel'): {'ackedstate': None,
                                                                                                                                                                                                                                                         'state': 3,
                                                                                                                                                                                                                                                         'target': 'frontendServer',
                                                                                                                                                                                                                                                         'transaction': 0}}},
                                                                                                                                               (4, 'upstreamCfg', 'upstreamCfg'): {'ackedstate': None,
                                                                                                                                                                                   'state': 3,
                                                                                                                                                                                   'transaction': 0,
                                                                                                                                                                                   'value': {(6, 'upstreamRel', 'upstreamRel'): {'ackedstate': None,
                                                                                                                                                                                                                                 'state': 3,
                                                                                                                                                                                                                                 'target': 'upstream',
                                                                                                                                                                                                                                 'transaction': 0}}},
                                                                                                                                               (5, 'name', 'name'): {'ackedstate': None,
                                                                                                                                                                     'state': 3,
                                                                                                                                                                     'transaction': 0,
                                                                                                                                                                     'value': 'loadBalancing'},
                                                                                                                                               (5, 'enabled', 'enabled'): {'state': 3, 'transaction': 0, 'ackedstate': None, 'value': 'true'}}}}}}},
                            (4, 'frontendServer', 'frontendServer'): {'ackedstate': None,
                                                                      'state': 3,
                                                                      'transaction': 0,
                                                                      'value': {(4, 'listen', 'listen'): {'ackedstate': None,
                                                                                                          'state': 3,
                                                                                                          'transaction': 0,
                                                                                                          'value': {(5, 'address', 'address'): {'ackedstate': None,
                                                                                                                                                'state': 3,
                                                                                                                                                'transaction': 0,
                                                                                                                                                'value': '10.9.217.1'},
                                                                                                                    (5, 'port', 'port'): {'ackedstate': None,
                                                                                                                                          'state': 3,
                                                                                                                                          'transaction': 0,
                                                                                                                                          'value': '80'}}},
                                                                                (4, 'location', 'location'): {'ackedstate': None,
                                                                                                              'state': 3,
                                                                                                              'transaction': 0,
                                                                                                              'value': {(5, 'backend_name', 'backend_name'): {'ackedstate': None,
                                                                                                                                                              'state': 3,
                                                                                                                                                              'transaction': 0,
                                                                                                                                                              'value': 'backend'},
                                                                                                                        (5, 'uri', 'uri'): {'ackedstate': None,
                                                                                                                                            'state': 3,
                                                                                                                                            'transaction': 0,
                                                                                                                                            'value': '/'},}}}},
                            (4, 'upstream', 'upstream'): {'ackedstate': None,
                                                          'state': 3,
                                                          'transaction': 0,
                                                          'value': {(4, 'server', 'web1'): {'ackedstate': None,
                                                                                            'state': 3,
                                                                                            'transaction': 0,
                                                                                            'value': {(5, 'ip', 'ip'): {'ackedstate': None,
                                                                                                                        'state': 3,
                                                                                                                        'transaction': 0,
                                                                                                                        'value': '10.9.218.1'},
                                                                                                      (5, 'port', 'port'): {'ackedstate': None,
                                                                                                                            'state': 3,
                                                                                                                            'transaction': 0,
                                                                                                                            'value': '80'}}},
                                                                    (4, 'server', 'web2'): {'ackedstate': None,
                                                                                            'state': 3,
                                                                                            'transaction': 0,
                                                                                            'value': {(5, 'ip', 'ip'): {'ackedstate': None,
                                                                                                                        'state': 3,
                                                                                                                        'transaction': 0,
                                                                                                                        'value': '10.9.218.2'},
                                                                                                      (5, 'port', 'port'): {'ackedstate': None,
                                                                                                                            'state': 3,
                                                                                                                            'transaction': 0,
                                                                                                                            'value': '80'}}},
                                                                    (5, 'upstreamName', 'upstreamName'): {'ackedstate': None,
                                                                                                          'state': 3,
                                                                                                          'transaction': 0,
                                                                                                          'value': 'backend'}}},
                            (7, '', '2129920_32771'): {'ackedstate': None,
                                                       'state': 3,
                                                       'tag': 2072,
                                                       'transaction': 0,
                                                       'type': 1},
                            (7, '', '2129920_32772'): {'ackedstate': None,
                                                       'state': 3,
                                                       'tag': 2004,
                                                       'transaction': 0,
                                                       'type': 1},
                            (8, '', 'NginxLoadBalancer_client_2129920_32771'): {'ackedstate': None,
                                                                                'encap': '2129920_32771',
                                                                                'state': 3,
                                                                                'transaction': 0,
                                                                                'vif': 'NginxLoadBalancer_client'},
                            (8, '', 'NginxLoadBalancer_pool_2129920_32772'): {'ackedstate': None,
                                                                              'encap': '2129920_32772',
                                                                              'state': 3,
                                                                              'transaction': 0,
                                                                              'vif': 'NginxLoadBalancer_pool'},
                            (10, '', 'NginxLoadBalancer_client'): {'ackedstate': None,
                                                                   'cifs': {'NginxLoadBalancer_Device_1': 'eth0'},
                                                                   'state': 3,
                                                                   'transaction': 0},
                            (10, '', 'NginxLoadBalancer_pool'): {'ackedstate': None,
                                                                 'cifs': {'NginxLoadBalancer_Device_1': 'eth2'},
                                                                 'state': 3,
                                                                 'transaction': 0}}}}

# Convert configuration into API object
api_config = Configuration(configuration)
# print(api_config)

# Create NginxDevice
nginx_device = NginxDevice(device)
print(nginx_device)

# Convert configuration into NGINX objects
# nginx_configurations = NginxConfiguration.from_configurations(api_config)
nginx_configurations = NginxConfigurationFactory.from_API_configuration(api_config)
print(nginx_configurations)

for nginx_configuration in nginx_configurations:

    # Generate (nginx) string of the configuration
    # string_config_file = nginx_configuration.export()
    string_config_file = nginx_configuration.visit(file_exporter())
    print(string_config_file)
#
#     # Using the Agent
#
#     # Get the list of existing configurations
#     status, sites = nginx_device.get_site_list(all_available_sites=True)
#     print(sites)
#
#     if status:
#         # Push
#         if nginx_configuration.name in sites:
#             print("Update '{}'".format(nginx_configuration.name))
#             nginx_device.update_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)
#         else:
#             print("Add '{}'".format(nginx_configuration.name))
#             nginx_device.create_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)
