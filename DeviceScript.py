#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from Exporter.FileExporter import file_exporter
from NGINXConfiguration.NginxConfiguration import NginxConfiguration
from NginxDevice import NginxDevice
from utils import logger
from API.ReturnValue import ReturnValue
from API.Configuration import Configuration
from API.Device import Device
from Insieme.Config import Result

__author__ = 'Fabrice Servais'

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))


# Device
def deviceValidate(device, version):
    logger.log("\n---- deviceValidate with parameters\n--> 'device' : {}\n--> 'version' : {}".format(device, version))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def deviceAudit(device, interfaces, configuration):
    logger.log("\n---- deviceAudit with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def deviceModify(device, interfaces, configuration):
    logger.log("\n---- deviceModify with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()



def deviceHealth(device, interfaces, configuration):
    logger.log("\n---- deviceHealth with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def deviceCounters(device, interfaces, configuration):
    logger.log("\n---- deviceCounters with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


#
# Clusters
def clusterAudit(device, interfaces, configuration):
    logger.log("\n---- clusterAudit with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def clusterModify(device, interfaces, configuration):
    logger.log("\n---- clusterModify with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


#
# Services
def serviceAudit(device, configuration):
    logger.log("\n---- serviceAudit with parameters\n--> 'device' : {}\n--> 'configuration' : {}".format(device, configuration))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def serviceModify(device, configuration):
    logger.log("\n---- serviceModify with parameters\n--> 'device' : {}\n--> 'configuration' : {}".format(device, configuration))

    # Convert configuration into API object
    api_config = Configuration(configuration)

    # Create NginxDevice
    nginx_device = NginxDevice(device)

    # Convert configuration into NGINX objects
    nginx_configurations = NginxConfiguration.from_configurations(api_config)

    for nginx_configuration in nginx_configurations:

        # Generate (nginx) string of the configuration
        string_config_file = nginx_configuration.visit(file_exporter())

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

    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def serviceHealth(device, configuration):
    logger.log("\n---- serviceHealth with parameters\n--> 'device' : {}\n--> 'configuration' : {}".format(device, configuration))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def serviceCounters(device, configuration):
    logger.log("\n---- serviceCounters with parameters\n--> 'device' : {}\n--> 'configuration' : {}".format(device, configuration))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def attachEndpoint(device, configuration, endpoints):
    logger.log("\n---- attachEndpoint with parameters\n--> 'device' : {}\n--> 'configuration' : {}\n--> 'endpoints' : {}".format(device, configuration, endpoints))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def detachEndpoint(device, configuration, endpoints):
    logger.log("\n---- detachEndpoint with parameters\n--> 'device' : {}\n--> 'configuration' : {}\n--> 'endpoints' : {}".format(device, configuration, endpoints))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def attachNetwork(device, configuration, connector, networks):
    logger.log("\n---- attachNetwork with parameters\n--> 'device' : {}\n--> 'configuration' : {}\n--> 'connector' : {}\n--> 'networks' : {}".format(device, configuration, connector, networks))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()


def detachNetwork(device, configuration, connector, networks):
    logger.log("\n---- detachNetwork with parameters\n--> 'device' : {}\n--> 'configuration' : {}\n--> 'connector' : {}\n--> 'networks' : {}".format(device, configuration, connector, networks))
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()
