from API.Device import Device
from Network.RequestHandler import RequestHandler

__author__ = 'Fabrice Servais'


class NginxDevice(Device):

    def __init__(self, device_dict):
        Device.__init__(self, device_dict)
        self.request_handler = RequestHandler(self.host_ip, self.port)

    # GET config ?
    def get(self, location):
        return self.request_handler.send("GET", location)
