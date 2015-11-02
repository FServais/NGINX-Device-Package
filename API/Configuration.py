__author__ = 'Fabrice Servais'


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

        for k, v in config_dict.iteritems():
            self.type, self.key, self.name = k

            self.state = v.get('state', -1)
            self.transaction = v.get('transaction', -1)
            self.connector = v.get('connector', None)
            self.value = v.get('value', None)
            if self.value is not None and type(self.value) is dict:
                self.value = Configuration(self.value)

            self.target = v.get('target', "")
            self.device = v.get('device', None)

            self.acked_state = v.get('acked_state', -1)
            self.ctx_name = v.get('ctxName', None)
            self.tenant = v.get('tenant', None)
            self.txid = v.get('txid', -1)
            self.abs_graph = v.get('absGraph', None)


if __name__ == "__main__":
    c = {(0, '', 5229): {'ackedState': 0,
                         'ctxName': 'Ciscoctx1',
                         'state': 1,
                         'tenant': 'Cisco',
                         'transaction': 0,
                         'txid': 10000,
                         'value': {(1, '', 5973): {'absGraph': 'WebGraph',
                                                   'ackedState': 0,
                                                   'state': 1,
                                                   'transaction': 0,
                                                   'value': {(3, 'VirtualServer', 'lb'): {'ackedState': 0,
                                                                                          'state': 1,
                                                                                          'transaction': 0,
                                                                                          'value': {(2, 'external',
                                                                                                     'external'): {
                                                                                              'ackedState': 0,
                                                                                              'state': 1,
                                                                                              'transaction': 0,
                                                                                              'value': {(9, '',
                                                                                                         'HAProxy_external_2818048_32770'): {
                                                                                                  'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'target': 'HAProxy_external_2818048_32770',
                                                                                                  'transaction': 0}}},
                                                                                              (2, 'internal',
                                                                                               'internal'): {
                                                                                                  'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'transaction': 0,
                                                                                                  'value': {(
                                                                                                      9, '',
                                                                                                      'HAProxy_internal_2818048_49156'): {
                                                                                                      'ackedState': 0,
                                                                                                      'state': 1,
                                                                                                      'target': 'HAProxy_internal_2818048_49156',
                                                                                                      'transaction': 0}}},
                                                                                              (4, 'backendCfg',
                                                                                               'backendCfg'): {
                                                                                                  'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'transaction': 0,
                                                                                                  'value': {(6,
                                                                                                             'backendCfgRel',
                                                                                                             'backendCfgRel'): {
                                                                                                      'ackedState': 0,
                                                                                                      'state': 1,
                                                                                                      'target': 'webserver',
                                                                                                      'transaction': 0}}},
                                                                                              (4, 'frontendCfg',
                                                                                               'frontendCfg'): {
                                                                                                  'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'transaction': 0,
                                                                                                  'value': {(6,
                                                                                                             'frontendCfgRel',
                                                                                                             'frontendCfgRel'): {
                                                                                                      'ackedState': 0,
                                                                                                      'state': 1,
                                                                                                      'target': 'webVirtualServer',
                                                                                                      'transaction': 0}}}}}}},
                                   (4, 'backend', 'webserver'): {'ackedState': 0,
                                                                 'state': 1,
                                                                 'transaction': 0,
                                                                 'value': {(5, 'mode', 'mode'): {'ackedState': 0,
                                                                                                 'state': 1,
                                                                                                 'transaction': 0,
                                                                                                 'value': 'http'},
                                                                           (6, 'server', 'server1'): {'ackedState': 0,
                                                                                                      'state': 1,
                                                                                                      'target': 'webserver1',
                                                                                                      'transaction': 0},
                                                                           (6, 'server', 'server2'): {'ackedState': 0,
                                                                                                      'state': 1,
                                                                                                      'target': 'webserver2',
                                                                                                      'transaction': 0},
                                                                           (6, 'server', 'server3'): {'ackedState': 0,
                                                                                                      'state': 1,
                                                                                                      'target': 'webserver3',
                                                                                                      'transaction': 0}}},
                                   (4, 'frontend', 'webVirtualServer'): {'ackedState': 0,
                                                                         'state': 1,
                                                                         'transaction': 0,
                                                                         'value': {
                                                                             (4, 'bind', 'bind'): {'ackedState': 0,
                                                                                                   'state': 1,
                                                                                                   'transaction': 0,
                                                                                                   'value': {(5,
                                                                                                              'address',
                                                                                                              'address'): {
                                                                                                       'ackedState': 0,
                                                                                                       'state': 1,
                                                                                                       'transaction': 0,
                                                                                                       'value': '10.0.0.1'},
                                                                                                       (5, 'port',
                                                                                                        'port'): {
                                                                                                           'ackedState': 0,
                                                                                                           'state': 1,
                                                                                                           'transaction': 0,
                                                                                                           'value': '80'}}},
                                                                             (5, 'mode', 'mode'): {'ackedState': 0,
                                                                                                   'state': 1,
                                                                                                   'transaction': 0,
                                                                                                   'value': 'http'},
                                                                             (5, 'name', 'name'): {'ackedState': 0,
                                                                                                   'state': 1,
                                                                                                   'transaction': 0,
                                                                                                   'value': 'webVirtualServer'}}},
                                   (4, 'server', 'webserver1'): {'ackedState': 0,
                                                                 'state': 1,
                                                                 'transaction': 0,
                                                                 'value': {(5, 'address', 'address1'): {'ackedState': 0,
                                                                                                        'state': 1,
                                                                                                        'transaction': 0,
                                                                                                        'value': '192.168.10.2'},
                                                                           (5, 'name', 'name1'): {'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'transaction': 0,
                                                                                                  'value': 'webserver1'},
                                                                           (5, 'port', 'port1'): {'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'transaction': 0,
                                                                                                  'value': '80'}}},
                                   (4, 'server', 'webserver2'): {'ackedState': 0,
                                                                 'state': 1,
                                                                 'transaction': 0,
                                                                 'value': {(5, 'address', 'address1'): {'ackedState': 0,
                                                                                                        'state': 1,
                                                                                                        'transaction': 0,
                                                                                                        'value': '192.168.10.3'},
                                                                           (5, 'name', 'name1'): {'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'transaction': 0,
                                                                                                  'value': 'webserver2'},
                                                                           (5, 'port', 'port2'): {'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'transaction': 0,
                                                                                                  'value': '80'}}},
                                   (4, 'server', 'webserver3'): {'ackedState': 0,
                                                                 'state': 1,
                                                                 'transaction': 0,
                                                                 'value': {(5, 'address', 'address1'): {'ackedState': 0,
                                                                                                        'state': 1,
                                                                                                        'transaction': 0,
                                                                                                        'value': '192.168.10.4'},
                                                                           (5, 'name', 'name1'): {'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'transaction': 0,
                                                                                                  'value': 'webserver3'},
                                                                           (5, 'port', 'port3'): {'ackedState': 0,
                                                                                                  'state': 1,
                                                                                                  'transaction': 0,
                                                                                                  'value': '80'}}},
                                   (7, '', '2818048_32770'): {'ackedState': 0,
                                                              'state': 1,
                                                              'tag': 437,
                                                              'transaction': 0,
                                                              'type': 1},
                                   (7, '', '2818048_49156'): {'ackedState': 0,
                                                              'state': 1,
                                                              'tag': 371,
                                                              'transaction': 0,
                                                              'type': 1},
                                   (8, '', 'HAProxy_external_2818048_32770'): {'ackedState': 0,
                                                                               'encap': '2818048_32770',
                                                                               'state': 1,
                                                                               'transaction': 0,
                                                                               'value': {},
                                                                               'vif': 'HAProxy_external'},
                                   (8, '', 'HAProxy_internal_2818048_49156'): {'ackedState': 0,
                                                                               'encap': '2818048_49156',
                                                                               'state': 1,
                                                                               'transaction': 0,
                                                                               'value': {},
                                                                               'vif': 'HAProxy_internal'},
                                   (10, '', 'HAProxy_external'): {'OspfVEncapAscCfg': {},
                                                                  'ackedState': 0,
                                                                  'cifs': {'dev1': 'eth0'},
                                                                  'state': 1,
                                                                  'transaction': 0},
                                   (10, '', 'HAProxy_internal'): {'OspfVEncapAscCfg': {},
                                                                  'ackedState': 0,
                                                                  'cifs': {'dev1': 'eth1'},
                                                                  'state': 1,
                                                                  'transaction': 0}}}}

    config = Configuration(c)

    print(config.state)
