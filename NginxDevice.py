from API.Device import Device
from Network.RequestHandler import RequestHandler

__author__ = 'Fabrice Servais'


class NginxDevice(Device):
    __URI_ROOT = "/"
    __URI_CONFIG = "/config"
    __URI_SITE = __URI_CONFIG + "/site"

    def __init__(self, device_dict):
        Device.__init__(self, device_dict)
        self.request_handler = RequestHandler(self.host_ip, self.port)

    def ping(self):
        status, _ = self.request_handler.send("GET", self.__URI_ROOT)
        return status == 200

    def get_site_list(self, all_available_sites=False):
        status, message = self.request_handler.send("GET", self.__URI_SITE, url_params={'allAvailable':all_available_sites})

        if status != 200:
            return (False, [])
        print(message)
        return (True, [str(site) for site in message['sites']])

    def get_site_config(self, site_name):
        return self.request_handler.send("GET", self.__URI_SITE + '/' + site_name)

    def create_site_config(self, site_name, config, enable=True):
        return self.request_handler.send("POST", self.__URI_SITE + '/' + site_name, payload={'config': config, 'enable': enable})

    def update_site_config(self, site_name, config, enable=True):
        return self.request_handler.send("PUT", self.__URI_SITE + '/' + site_name, payload={'config': config, 'enable': enable})

if __name__ == "__main__":
    device = {'creds': {'username': 'fservais', 'password': '<hidden>'}, 'host': '127.0.0.1', 'port': 5000, 'virtual': True}
    nginx_device = NginxDevice(device)

    status = nginx_device.ping()
    print("Status: {}".format(status))

    status, message = nginx_device.get_site_list(all_available_sites=None)
    print("Status: {}".format(status))
    print("Message: {}".format(message))

    # status, message = nginx_device.get_site_config("default")
    # print("Status: {}".format(status))
    # print(message)
    #
    # status, message = nginx_device.create_site_config("test_site", "test-config3")
    # print("Status: {}".format(status))
    # print(message)
    #
    # status, message = nginx_device.get_site_list(all_available_sites=True)
    # print("Status: {}".format(status))
    # print(message)
    #
    # status, message = nginx_device.get_site_config("test_site")
    # print("Status: {}".format(status))
    # print(message)