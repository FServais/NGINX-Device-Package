from API.Device import Device
from Network.RequestHandler import RequestHandler
from utils import logger

__author__ = 'Fabrice Servais'


class NginxDevice(Device):
    # -- URIs to send the requests to the agent

    # Ping
    __URI_ROOT = "/"

    __URI_CONFIG = "/config"

    # Set nginx parameter (directory)
    __URI_NGINX_CONFIG = __URI_CONFIG + "/nginx"
    __URI_NGINX_DIR_CONFIG = __URI_NGINX_CONFIG + "/directory"

    # Site-related configurations
    __URI_SITE_CONFIG = __URI_CONFIG + "/site"

    # Health check
    __URI_HEALTH_DEVICE = "/health/device"

    def __init__(self, device_dict):
        """
        Constructor.
        Args:
            device_dict: (Type: Python dictionary) Configuration of the device sent by the APIC.
        """
        Device.__init__(self, device_dict)
        self.request_handler = RequestHandler(self.host_ip, self.port, self.username, self.password)

    # ---- String representation

    def __str__(self):
        return '{} -> {}:<hidden>@{}:{}'.format(self.name, self.username, self.host_ip, self.port)
        # return pformat(self.orig_dict)

    def __repr__(self):
        return str(self)

    # ----

    # ---- Connection management

    def enable_https(self):
        """
        Set the connection between the controller and the Agent to be sent using HTTPS.
        """
        self.request_handler.https = True

    def disable_https(self):
        """
        Set the connection between the controller and the Agent to be sent using HTTP.
        """
        self.request_handler.https = False

    # ----

    # ---- Methods to interact with the agent

    def ping(self):
        """
        Check if the Agent is running on the device.

        Returns: Boolean
            Boolean: True if the Agent has correctly replied (200 OK), False otherwise.

        """
        status, _ = self.request_handler.send("GET", self.__URI_ROOT)
        return status == 200

    def check_device_status(self):
        """
        Send health state and score of the device.

        Returns: Boolean, int
            Boolean: True if the Agent has correctly replied (200 OK), False otherwise.
            int: Health score

        """

        # -- Score calculated by the Device Script

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

        # -- Score calculated by the Agent

        device_name = 'lb'  # TODO Get LB (device) name before hand

        status, message = self.request_handler.send('GET', self.__URI_HEALTH_DEVICE + '/' + device_name)
        if status != 200:
            return False, 0

        score = message['score']
        logger.log("Health score of {}: {}".format(device_name, score))

        return status == 200, score

    def get_site_list(self, all_available_sites=False):
        """
        Get the list of all the names of the sites (i.e. configurations) on the Device.

        Args:
            all_available_sites: True if the function has to return all the configurations, even when not enabled. False for only the enabled configurations.

        Returns: Boolean, List<String>
            Boolean: True if the Agent has correctly replied (200 OK), False otherwise.
            List<String>: List of names.

        """
        status, message = self.request_handler.send("GET", self.__URI_SITE_CONFIG, url_params={'allAvailable':all_available_sites})

        if status != 200:
            logger.log("Error {}: {}".format(status, message))
            return (False, [])

        return (True, [str(site) for site in message['sites']])

    def get_site_config(self, site_name):
        """
        Get a particular configuration based on its name 'site_name'.

        Args:
            site_name: (String) Name of the configuration.

        Returns: Boolean, List<String>
            Boolean: True if the Agent has correctly replied (200 OK), False otherwise.
            String: Configuration.

        """
        status, message = self.request_handler.send("GET", self.__URI_SITE_CONFIG + '/' + site_name)

        if status != 200:
            logger.log("Error {}: {}".format(status, message['message']))
            return False, ""

        return True, message['config']

    def create_site_config(self, site_name, config, enable=True):
        """
        Create a configuration named 'site_name' on the device, that contains 'config'. If 'enable', the configuration is activated.

        Args:
            site_name: (String) Name of the configuration.
            config: (String) Content of the configuration.
            enable: (Boolean) True to enable the configuration on the device.

        Returns: Boolean
            Boolean: True if the configuration has been created, False otherwise.

        """
        status, message = self.request_handler.send("POST", self.__URI_SITE_CONFIG + '/' + site_name, payload={'config': config, 'enable': enable})

        if status != 200:
            logger.log("Error {}: {}".format(status, message['message']))
            return False

        return message['state'] == 1

    def update_site_config(self, site_name, config, enable=True):
        """
        Update a configuration named 'site_name' on the device, that contains 'config'. If 'enable', the configuration is activated.

        Args:
            site_name: (String) Name of the configuration.
            config: (String) Content of the configuration.
            enable: (Boolean) True to enable the configuration on the device.

        Returns: Boolean
            Boolean: True if the configuration has been updated, False otherwise.

        """
        status, message = self.request_handler.send("PUT", self.__URI_SITE_CONFIG + '/' + site_name, payload={'config': config, 'enable': enable})

        if status != 200:
            logger.log("Error {}: {}".format(status, message['message']))
            return False

        return message['state'] == 1

    def update_nginx_dir_config(self, new_path):
        """
        Set the directory where is nginx (by default: /etc/nginx).

        Args:
            new_path: Path to NGINX directory.

        Returns: Boolean
            Boolean: True if the path has been updated, False otherwise.

        """
        status, message = self.request_handler.send("PUT", self.__URI_NGINX_DIR_CONFIG, payload={'path': new_path})

        if status != 200:
            logger.log("Error {}: {}".format(status, message))
            return False

        return message['state'] == 1
