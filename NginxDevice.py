from API.Device import Device
from Network.RequestHandler import RequestHandler
from utils import logger

__author__ = 'Fabrice Servais'


class NginxDevice(Device):
    __URI_ROOT = "/"

    __URI_CONFIG = "/config"

    __URI_NGINX_CONFIG = __URI_CONFIG + "/nginx"
    __URI_NGINX_DIR_CONFIG = __URI_NGINX_CONFIG + "/directory"

    __URI_SITE_CONFIG = __URI_CONFIG + "/site"

    __URI_HEALTH_DEVICE = "/health/device"

    def __init__(self, device_dict):
        Device.__init__(self, device_dict)
        self.request_handler = RequestHandler(self.host_ip, self.port, self.username, self.password)

    def __str__(self):
        return '{} -> {}:<hidden>@{}:{}'.format(self.name, self.username, self.host_ip, self.port)
        # return pformat(self.orig_dict)

    def __repr__(self):
        return str(self)

    def enable_https(self):
        self.request_handler.https = True

    def disable_https(self):
        self.request_handler.https = False

    def ping(self):
        status, _ = self.request_handler.send("GET", self.__URI_ROOT)
        return status == 200

    def check_device_status(self):
        # status, message = self.request_handler.send("GET", self.__URI_ROOT)
        #
        # if status != 200:
        #     return False, 1
        #
        # if message is None:
        #     return status == 200, 1
        #
        # print("Status", status)
        # print("Message", message)
        # device_status = message["status"]
        #
        # return status == 200, device_status

        # TODO Get LB (device) name
        device_name = 'lb'

        status, message = self.request_handler.send('GET', self.__URI_HEALTH_DEVICE + '/' + device_name)
        if status != 200:
            return False, 0

        score = message['score']
        logger.log("Health score of {}: {}".format(device_name, score))

        return status == 200, score

    def get_site_list(self, all_available_sites=False):
        status, message = self.request_handler.send("GET", self.__URI_SITE_CONFIG, url_params={'allAvailable':all_available_sites})

        if status != 200:
            logger.log("Error {}: {}".format(status, message))
            return (False, [])

        return (True, [str(site) for site in message['sites']])

    def get_site_config(self, site_name):
        return self.request_handler.send("GET", self.__URI_SITE_CONFIG + '/' + site_name)

    def create_site_config(self, site_name, config, enable=True):
        return self.request_handler.send("POST", self.__URI_SITE_CONFIG + '/' + site_name, payload={'config': config, 'enable': enable})

    def update_site_config(self, site_name, config, enable=True):
        return self.request_handler.send("PUT", self.__URI_SITE_CONFIG + '/' + site_name, payload={'config': config, 'enable': enable})

    def update_nginx_dir_config(self, new_path):
        return self.request_handler.send("PUT", self.__URI_NGINX_DIR_CONFIG, payload={'path': new_path})
