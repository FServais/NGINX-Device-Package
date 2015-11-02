__author__ = 'Fabrice Servais'


class VDevs:

    def __init__(self, vdev_dict):
        self.ctx_name = vdev_dict.get('ctxName', None)
        self.id = vdev_dict.get('id', None)
        self.tenant = vdev_dict.get('tenant', None)
    pass


class Device:
    def __init__(self, device_dict):
        self.devices = []

        self.host_ip = device_dict.get('host', None)
        self.port = device_dict.get('port', None)
        self.name = device_dict.get('name', None)

        self.credentials = device_dict.get('creds', None)
        if self.credentials is not None:
            self.username = self.credentials.get('username', None)
            self.password = self.credentials.get('password', None)

        self.virtual = device_dict.get('virtual', None)

        devs = device_dict.get('devs', None)
        if devs is not None:
            for k, v in devs.iteritems():
                device = Device(v)
                device.name = k
                self.devices.append(device)

        self.vdevs = []
        vdevs = device_dict.get('vdevs', None)
        if vdevs is not None:
            for vdev in vdevs:
                self.vdevs.append(VDevs(vdev))


if __name__ == "__main__":
    device = {'creds': {'password': '<hidden>', 'username': 'nsroot'},
                 'devs': {'Generic1': {'creds': {'password': '<hidden>',
                                                 'username': 'nsroot'},
                                       'host': '42.42.42.100',
                                       'port': 80,
                                       'version': '1.0',
                                       'virtual': True},
                          'Generic2': {'creds': {'password': '<hidden>',
                                                 'username': 'nsroot'},
                                       'host': '42.42.42.101',
                                       'port': 80,
                                       'version': '1.0',
                                       'virtual': True}},
                 'host': '42.42.42.99',
                 'name': 'InsiemeCluster',
                 'port': 80,
                 'vdevs': [{'ctxName': 'cokectx1', 'id': 9597, 'tenant': 'coke'}],
                 'virtual': True}

    d = Device(device)
    print(d.vdevs[0].ctx_name)