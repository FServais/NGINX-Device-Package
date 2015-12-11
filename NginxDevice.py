from API.Device import Device
from Network.RequestHandler import RequestHandler

__author__ = 'Fabrice Servais'


class NginxDevice(Device):
    __URI_ROOT = "/"

    __URI_CONFIG = "/config"

    __URI_NGINX_CONFIG = __URI_CONFIG + "/nginx"
    __URI_NGINX_DIR_CONFIG = __URI_NGINX_CONFIG + "/directory"

    __URI_SITE_CONFIG = __URI_CONFIG + "/site"

    def __init__(self, device_dict):
        Device.__init__(self, device_dict)
        self.request_handler = RequestHandler(self.host_ip, self.port, self.username, self.password)

    def __str__(self):
        return '{} -> {}:{}@{}:{}'.format(self.name, self.username, self.password, self.host_ip, self.port)
        # return pformat(self.orig_dict)

    def __repr__(self):
        return str(self)

    def ping(self):
        status, _ = self.request_handler.send("GET", self.__URI_ROOT)
        return status == 200

    def get_site_list(self, all_available_sites=False):
        status, message = self.request_handler.send("GET", self.__URI_SITE_CONFIG, url_params={'allAvailable':all_available_sites})

        if status != 200:
            return (False, [])
        print(message)
        return (True, [str(site) for site in message['sites']])

    def get_site_config(self, site_name):
        return self.request_handler.send("GET", self.__URI_SITE_CONFIG + '/' + site_name)

    def create_site_config(self, site_name, config, enable=True):
        return self.request_handler.send("POST", self.__URI_SITE_CONFIG + '/' + site_name, payload={'config': config, 'enable': enable})

    def update_site_config(self, site_name, config, enable=True):
        return self.request_handler.send("PUT", self.__URI_SITE_CONFIG + '/' + site_name, payload={'config': config, 'enable': enable})

    def update_nginx_dir_config(self, new_path):
        return self.request_handler.send("PUT", self.__URI_NGINX_DIR_CONFIG, payload={'path': new_path})

if __name__ == "__main__":
    # device = {'creds': {'username': 'root', 'password': '<hidden>'}, 'host': '127.0.0.1', 'port': 5000, 'virtual': True}
    device = {'creds': {'username': 'fservais', 'password': '<hidden>'}, 'host': '127.0.0.1', 'port': 5000, 'virtual': True}
    nginx_device = NginxDevice(device)

    print("--------PING---------")

    status = nginx_device.ping()
    print("Status: {}".format(status))

    print("--------GET SITE LIST---------")

    status, message = nginx_device.get_site_list(all_available_sites=None)
    print("Status: {}".format(status))
    print("Message: {}".format(message))

    print("--------GET SITE CONFIG---------")

    status, message = nginx_device.get_site_config("default")
    print("Status: {}".format(status))
    print(message)

    print("--------CREATE SITE CONFIG---------")

    status, message = nginx_device.create_site_config("test_site", "test-config3")
    print("Status: {}".format(status))
    print(message)

    print("--------GET SITE LIST---------")

    status, message = nginx_device.get_site_list(all_available_sites=True)
    print("Status: {}".format(status))
    print(message)

    print("--------GET SITE CONFIG---------")

    status, message = nginx_device.get_site_config("test_site")
    print("Status: {}".format(status))
    print(message)