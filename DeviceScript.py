#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from Exporter.FileExporter import file_exporter
from NGINXConfiguration.NginxConfigurationFactory import NginxConfigurationFactory
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
    return return_ok()


def deviceAudit(device, interfaces, configuration):
    logger.log("\n---- deviceAudit with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return return_ok()


def deviceModify(device, interfaces, configuration):
    logger.log("\n---- deviceModify with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return return_ok()



def deviceHealth(device, interfaces, configuration):
    logger.log("\n---- deviceHealth with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return return_ok()


def deviceCounters(device, interfaces, configuration):
    logger.log("\n---- deviceCounters with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return return_ok()


#
# Clusters
def clusterAudit(device, interfaces, configuration):
    logger.log("\n---- clusterAudit with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return return_ok()


def clusterModify(device, interfaces, configuration):
    logger.log("\n---- clusterModify with parameters\n--> 'device' : {}\n--> 'interfaces' : {}\n--> 'configuration' : {}".format(device, interfaces, configuration))
    return return_ok()


#
# Services
def serviceAudit(device, configuration):
    logger.log("\n---- serviceAudit with parameters\n--> 'device' : {}\n--> 'configuration' : {}".format(device, configuration))

    logger.log("Initialize the configurations...")
    # Convert configuration into API object
    api_config = Configuration(configuration)
    logger.log("> Configuration\n{}".format(api_config))

    # Create NginxDevice
    nginx_device = NginxDevice(device)
    logger.log("> Device\n{}".format(nginx_device))

    # Convert configuration into NGINX objects
    nginx_configurations, management_configuration = NginxConfigurationFactory.from_API_configuration(api_config)
    logger.log("Nginxconfig: {}".format(nginx_configurations))
    logger.log("Management: {}".format(management_configuration))
    https_enable = management_configuration['https']

    if not https_enable:
        nginx_device.disable_https()

    logger.log("Configuration: {} (len {})".format(nginx_configurations, len(nginx_configurations)))

    for nginx_configuration in nginx_configurations:
        logger.log(">> For configuration {}".format(nginx_configuration.name))
        logger.log("Generating the string...")
        # Generate (nginx) string of the configuration
        string_config_file = nginx_configuration.visit(file_exporter())

        logger.log("Getting the list of the sites...")
        # Get the list of existing configurations
        status, sites = nginx_device.get_site_list(all_available_sites=True)

        if status:
            logger.log("Pushing the configuration...")
            # Push
            if nginx_configuration.name in sites:
                logger.log("Update '{}'".format(nginx_configuration.name))
                nginx_device.update_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)
            else:
                logger.log("Add '{}'".format(nginx_configuration.name))
                nginx_device.create_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)

    return return_ok()


def serviceModify(device, configuration):
    logger.log("\n---- serviceModify with parameters\n--> 'device' : {}\n--> 'configuration' : {}".format(device, configuration))
    logger.log("Initialize the configurations...")
    # Convert configuration into API object
    api_config = Configuration(configuration)
    logger.log("> Configuration\n{}".format(api_config))

    # Create NginxDevice
    nginx_device = NginxDevice(device)
    logger.log("> Device\n{}".format(nginx_device))

    # Convert configuration into NGINX objects
    nginx_configurations, management_configuration = NginxConfigurationFactory.from_API_configuration(api_config)
    logger.log("Nginxconfig: {}".format(nginx_configurations))
    logger.log("Management: {}".format(management_configuration))
    https_enable = management_configuration['https']

    if not https_enable:
        nginx_device.disable_https()

    logger.log("Configuration: {} (len {})".format(nginx_configurations, len(nginx_configurations)))

    for nginx_configuration in nginx_configurations:
        logger.log(">> For configuration {}".format(nginx_configuration.name))
        logger.log("Generating the string...")
        # Generate (nginx) string of the configuration
        string_config_file = nginx_configuration.visit(file_exporter())

        logger.log("Getting the list of the sites...")
        # Get the list of existing configurations
        status, sites = nginx_device.get_site_list(all_available_sites=True)
        logger.log('Status: {} ; Sites: {}'.format(status, sites))

        if status:
            logger.log("Pushing the configuration...")
            # Push
            if nginx_configuration.name in sites:
                logger.log("Update '{}'".format(nginx_configuration.name))
                nginx_device.update_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)
            else:
                logger.log("Add '{}'".format(nginx_configuration.name))
                nginx_device.create_site_config(nginx_configuration.name, string_config_file, enable=nginx_configuration.enabled)

    return return_ok()


def serviceHealth(device, configuration):
    logger.log("\n---- serviceHealth with parameters\n--> 'device' : {}\n--> 'configuration' : {}".format(device, configuration))
    return return_ok()


def serviceCounters(device, configuration):
    logger.log("\n---- serviceCounters with parameters\n--> 'device' : {}\n--> 'configuration' : {}".format(device, configuration))
    return return_ok()


def attachEndpoint(device, configuration, endpoints):
    logger.log("\n---- attachEndpoint with parameters\n--> 'device' : {}\n--> 'configuration' : {}\n--> 'endpoints' : {}".format(device, configuration, endpoints))
    return return_ok()


def detachEndpoint(device, configuration, endpoints):
    logger.log("\n---- detachEndpoint with parameters\n--> 'device' : {}\n--> 'configuration' : {}\n--> 'endpoints' : {}".format(device, configuration, endpoints))
    return return_ok()


def attachNetwork(device, configuration, connector, networks):
    logger.log("\n---- attachNetwork with parameters\n--> 'device' : {}\n--> 'configuration' : {}\n--> 'connector' : {}\n--> 'networks' : {}".format(device, configuration, connector, networks))
    return return_ok()


def detachNetwork(device, configuration, connector, networks):
    logger.log("\n---- detachNetwork with parameters\n--> 'device' : {}\n--> 'configuration' : {}\n--> 'connector' : {}\n--> 'networks' : {}".format(device, configuration, connector, networks))
    return return_ok()


# Misc. functions
def return_ok():
    return ReturnValue(state=Result.SUCCESS, health=[([], 100)], fault=[]).get_return_value()