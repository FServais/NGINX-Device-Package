# ===== Service modify
# Arguments
from NginxDevice import NginxDevice

device = {'name': 'NginxLoadBalancer', 'virtual': True, 'devs': {'NginxLoadBalancer_Device_1': {'creds': {'username': 'fservais', 'password': '<hidden>'}, 'host': '127.0.0.1', 'port': 80, 'virtual': True}}, 'host': '127.0.0.1', 'contextaware': False, 'port': 5000, 'creds': {'username': 'fservais', 'password': '<hidden>'}}
configuration = {(0, '', 4099): {'ackedstate': 0,
                 'ctxName': 'VRF_NG',
                 'dn': u'uni/vDev-[uni/tn-NGINX/lDevVip-NginxDevice]-tn-[uni/tn-NGINX]-ctx-VRF_NG',
                 'state': 1,
                 'tenant': 'NGINX',
                 'transaction': 0,
                 'txid': 10000,
                 'value': {(1, '', 39100): {'absGraph': 'NginxLB_SGT',
                                            'ackedstate': 0,
                                            'rn': u'vGrp-[uni/tn-NGINX/GraphInst_C-[uni/tn-NGINX/brc-NginxLB_AllIPContract]-G-[uni/tn-NGINX/AbsGraph-NginxLB_SGT]-S-[uni/tn-NGINX]]',
                                            'state': 1,
                                            'transaction': 0,
                                            'value': {(3, 'LoadBalancer', 'NginxLB'): {'ackedstate': 0,
                                                                                       'state': 1,
                                                                                       'transaction': 0,
                                                                                       'value': {(2, 'external', 'consumer'): {'ackedstate': 0,
                                                                                                                               'state': 1,
                                                                                                                               'transaction': 0,
                                                                                                                               'value': {(9, '', 'NginxDevice_client_2129920_49160'): {'ackedstate': 0,
                                                                                                                                                                                       'state': 1,
                                                                                                                                                                                       'target': 'NginxDevice_client_2129920_49160',
                                                                                                                                                                                       'transaction': 0}}},
                                                                                                 (2, 'internal', 'provider'): {'ackedstate': 0,
                                                                                                                               'state': 1,
                                                                                                                               'transaction': 0,
                                                                                                                               'value': {(9, '', 'NginxDevice_pool_2129920_16395'): {'ackedstate': 0,
                                                                                                                                                                                     'state': 1,
                                                                                                                                                                                     'target': 'NginxDevice_pool_2129920_16395',
                                                                                                                                                                                     'transaction': 0}}},
                                                                                                 (4, 'configuration', 'MyConfiguration'): {'ackedstate': 0,
                                                                                                                                           'state': 1,
                                                                                                                                           'transaction': 0,
                                                                                                                                           'value': {(4, 'frontendServerCfg', 'frontendServerCfg'): {'ackedstate': 0,
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
                                                                                                                                                                                                                                       'transaction': 0}}},
                                                                                                                                                     (5, 'enabled', 'enabled'): {'ackedstate': 0,
                                                                                                                                                                                 'state': 1,
                                                                                                                                                                                 'transaction': 0,
                                                                                                                                                                                 'value': 'true'}}},
                                                                                                 (4, 'management', 'management'): {'ackedstate': 0,
                                                                                                                                   'state': 1,
                                                                                                                                   'transaction': 0,
                                                                                                                                   'value': {(5, 'https', 'https'): {'ackedstate': 0,
                                                                                                                                                                     'state': 1,
                                                                                                                                                                     'transaction': 0,
                                                                                                                                                                     'value': 'false'}}}}}}},
                           (4, 'frontendServer', 'frontendServer'): {'ackedstate': 0,
                                                                     'state': 1,
                                                                     'transaction': 0,
                                                                     'value': {(4, 'listen', 'listen'): {'ackedstate': 0,
                                                                                                         'state': 1,
                                                                                                         'transaction': 0,
                                                                                                         'value': {(5, 'address', 'address'): {'ackedstate': 0,
                                                                                                                                               'state': 1,
                                                                                                                                               'transaction': 0,
                                                                                                                                               'value': '10.9.217.1'},
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
                                                                                                                       'value': '10.9.218.1'},
                                                                                                     (5, 'port', 'port'): {'ackedstate': 0,
                                                                                                                           'state': 1,
                                                                                                                           'transaction': 0,
                                                                                                                           'value': '80'}}},
                                                                   (4, 'server', 'web2'): {'ackedstate': 0,
                                                                                           'state': 1,
                                                                                           'transaction': 0,
                                                                                           'value': {(5, 'ip', 'ip'): {'ackedstate': 0,
                                                                                                                       'state': 1,
                                                                                                                       'transaction': 0,
                                                                                                                       'value': '10.9.218.2'},
                                                                                                     (5, 'port', 'port'): {'ackedstate': 0,
                                                                                                                           'state': 1,
                                                                                                                           'transaction': 0,
                                                                                                                           'value': '80'}}},
                                                                   (5, 'upstreamName', 'upstreamName'): {'ackedstate': 0,
                                                                                                         'state': 1,
                                                                                                         'transaction': 0,
                                                                                                         'value': 'backend'}}},
                           (7, '', '2129920_16395'): {'ackedstate': 0,
                                                      'state': 1,
                                                      'tag': 2073,
                                                      'transaction': 0,
                                                      'type': 1},
                           (7, '', '2129920_49160'): {'ackedstate': 0,
                                                      'state': 1,
                                                      'tag': 2072,
                                                      'transaction': 0,
                                                      'type': 1},
                           (8, '', 'NginxDevice_client_2129920_49160'): {'ackedstate': 0,
                                                                         'encap': '2129920_49160',
                                                                         'state': 1,
                                                                         'transaction': 0,
                                                                         'vif': 'NginxDevice_client'},
                           (8, '', 'NginxDevice_pool_2129920_16395'): {'ackedstate': 0,
                                                                       'encap': '2129920_16395',
                                                                       'state': 1,
                                                                       'transaction': 0,
                                                                       'vif': 'NginxDevice_pool'},
                           (10, '', 'NginxDevice_client'): {'ackedstate': 0,
                                                            'cifs': {'NginxDevice_Device_1': 'eth0'},
                                                            'state': 1,
                                                            'transaction': 0},
                           (10, '', 'NginxDevice_pool'): {'ackedstate': 0,
                                                          'cifs': {'NginxDevice_Device_1': 'eth2'},
                                                          'state': 1,
                                                          'transaction': 0}}}}


# print("\n---- serviceModify with parameters\n--> 'device' : {}\n--> 'configuration' : {}".format(device, configuration))
# print("Initialize the configurations...")
# # Convert configuration into API object
# api_config = Configuration(configuration)
# print("> Configuration\n{}".format(api_config))
#
# Create NginxDevice
nginx_device = NginxDevice(device)
print("> Device\n{}".format(nginx_device))

nginx_device.disable_https()

print("PING")
status, device_status = nginx_device.check_device_status()
print(status)
print(device_status)

# # Convert configuration into NGINX objects
# nginx_configurations, management_configuration = ConfigurationParser.from_API_configuration(api_config)
# https_enable = management_configuration['https']
#

# if not https_enable:
#     nginx_device.disable_https()
#
# print("Configuration: {} (len {})".format(nginx_configurations, len(nginx_configurations)))
#
# for nginx_configuration in nginx_configurations:
#     print(">> For configuration {}".format(nginx_configuration.name))
#     print("Generating the string...")
#     # Generate (nginx) string of the configuration
#     string_config_file = nginx_configuration.accept(file_exporter())
#     print(string_config_file)
#
#     print("Getting the list of the sites...")
#     # Get the list of existing configurations
#     status, sites = nginx_device.get_site_list(all_available_sites=True)
#     print('Status: {} ; Sites: {}'.format(status, sites))
    #
    # if status:
    #     print("Pushing the configuration...")
    #     # Push
    #     if nginx_configuration.name in sites:
    #         print("Update '{}'".format(nginx_configuration.name))
    #         nginx_device.update_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)
    #     else:
    #         print("Add '{}'".format(nginx_configuration.name))
    #         nginx_device.create_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)