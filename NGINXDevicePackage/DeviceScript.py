#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Fabrice Servais'
__version__ = "$Revision: #0 $"

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

#
# Device
def deviceValidate(device, version):
    return


def deviceAudit(device, interfaces, configuration):
    return

def deviceModify(device, interfaces, configuration):
    return


def deviceHealth(device, interfaces, configuration):
    return


def deviceCounters(device, interfaces, configuration):
    return

#
# Clusters
def clusterAudit(device, interfaces, configuration):
    return


def clusterModify(device, interfaces, configuration):
    return

#
# Services
def serviceAudit(device, configuration):
    return


def serviceModify(device, configuration):
    return


def serviceHealth(device, configuration):
    return


def serviceCounters(device, configuration):
    return


def attachEndpoint(device, configuration, endpoints):
    return


def detachEndpoint(device, configuration, endpoints):
    return


def attachNetwork(device, configuration, connector, networks):
    return


def detachNetwork(device, configuration, connector, networks):
    return
