# ===== Service modify
# Arguments
from API.Configuration import Configuration
from API.Device import Device
from Exporter.FileExporter import file_exporter
from NGINXConfiguration.NginxConfiguration import NginxConfiguration
from NginxDevice import NginxDevice
from NginxDeviceSSH import NginxDeviceSSH

device = {'creds': {'username': 'fservais', 'password': '<hidden>'}, 'host': '127.0.0.1', 'port': 5000, 'virtual': True}
configuration = {(0, '', 5167): {'ackedstate': 0,
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
                           (4, 'configuration', 'Configuration'): {'ackedstate': 0,
                                                                   'state': 1,
                                                                   'transaction': 0,
                                                                   'value': {(4, 'frontendServer', 'frontendServer'): {'ackedstate': 0,
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
                                                                             (4, 'frontendServer', 'frontendServer2'): {'ackedstate': 0,
                                                                                                                       'state': 1,
                                                                                                                       'transaction': 0,
                                                                                                                       'value': {(4, 'listen', 'listen'): {'ackedstate': 0,
                                                                                                                                                           'state': 1,
                                                                                                                                                           'transaction': 0,
                                                                                                                                                           'value': {(5, 'address', 'address'): {'ackedstate': 0,
                                                                                                                                                                                                 'state': 1,
                                                                                                                                                                                                 'transaction': 0,
                                                                                                                                                                                                 'value': '127.0.0.2'},
                                                                                                                                                                     (5, 'port', 'port'): {'ackedstate': 0,
                                                                                                                                                                                           'state': 1,
                                                                                                                                                                                           'transaction': 0,
                                                                                                                                                                                           'value': '80003'}}},
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
                                                                             (5, 'enabled', 'enabled'): {'ackedstate': 0,
                                                                                                         'state': 1,
                                                                                                         'transaction': 0,
                                                                                                         'value': 'True'},
                                                                             (5, 'name', 'name'): {'ackedstate': 0,
                                                                                                   'state': 1,
                                                                                                   'transaction': 0,
                                                                                                   'value': 'test_config'}}},
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

# Convert configuration into API object
api_config = Configuration(configuration)

# Create NginxDevice
nginx_device = NginxDeviceSSH(device)

# Convert configuration into NGINX objects
nginx_configurations = NginxConfiguration.from_configurations(api_config)

for nginx_configuration in nginx_configurations:
    print(nginx_configuration)
    # Generate (nginx) string of the configuration
    # string_config_file = nginx_configuration.export()
    string_config_file = nginx_configuration.visit(file_exporter())
    print(string_config_file)

    # Using the Agent

    # # Get the list of existing configurations
    # status, sites = nginx_device.get_site_list(all_available_sites=True)
    #
    # if status:
    #     # Push
    #     if nginx_configuration.name in sites:
    #         print("Update '{}'".format(nginx_configuration.name))
    #         nginx_device.update_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)
    #     else:
    #         print("Add '{}'".format(nginx_configuration.name))
    #         nginx_device.create_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)

    # Using SSH

    connection_status = nginx_device.connect()

    if connection_status:
        # Get the list of existing configurations
        status, sites = nginx_device.get_site_list(all_available_sites=True)

        if status:
            # Push
            if nginx_configuration.name in sites:
                print("Update '{}'".format(nginx_configuration.name))
                nginx_device.update_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)
            else:
                print("Add '{}'".format(nginx_configuration.name))
                nginx_device.create_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)