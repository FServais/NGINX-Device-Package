__author__ = 'Fabrice Servais'

from pprint import pformat

class Configuration:
    """
    (type,  key, name) : {
        'state': ...
        'transaction': ...
        'connector': ...
        'value': ...
        'target': ...
        'device': ...
    }
    """

    def __init__(self, config_dict):
        self.orig_dict = config_dict

        for k, v in config_dict.iteritems():
            self.type, self.key, self.name = k

            self.state = v.get('state', -1)
            self.transaction = v.get('transaction', -1)
            self.connector = v.get('connector', None)
            self.value = v.get('value', None)
            if self.value is not None and type(self.value) is dict:
                self.value = [Configuration({k: v}) for k, v in self.value.items()]

            self.target = v.get('target', None)
            self.device = v.get('device', None)

            self.acked_state = v.get('acked_state', -1)
            self.ctx_name = v.get('ctxName', None)
            self.tenant = v.get('tenant', None)
            self.txid = v.get('txid', -1)
            self.abs_graph = v.get('absGraph', None)

    def __str__(self):
        return '({} - {}) -> {}'.format(self.type, self.key, self.value)
        # return pformat(self.orig_dict)

    def __repr__(self):
        return str(self)

    def get_type(self):
        return self.type

    def get_key(self):
        return self.key

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

if __name__ == "__main__":

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
                                                                                                   'value': 'default'}}},
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

    config = Configuration(nginxServiceAuditConfig)

    print(config)

    config2 = Configuration({(4, 'listen', 'listen'): {'ackedstate': 0,
                           'state': 1,
                           'transaction': 0,
                           'value': {(5, 'address', 'address'): {'ackedstate': 0,
                                                                 'state': 1,
                                                                 'transaction': 0,
                                                                 'value': '127.0.0.1'},
                                     (5, 'port', 'port'): {'ackedstate': 0,
                                                           'state': 1,
                                                           'transaction': 0,
                                                           'value': '80'}}}})
    print(config2)

