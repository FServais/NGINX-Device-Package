import re
import socket
import subprocess

__author__ = 'Fabrice Servais'

class ConnectivityChecking:

    @classmethod
    def ping(self, host):
        try:
            ping = subprocess.Popen(["ping -c1 -t5 " + host], stdout=subprocess.PIPE, shell=True)
            out, error = ping.communicate()
            if out:
                try:
                    icmp_seq = int(re.findall(r"icmp_seq=(\d+)", out)[0])
                    ttl = int(re.findall(r"ttl=(\d+)", out)[0])
                    return True
                except:
                    return False
            else:
                return False

        except subprocess.CalledProcessError:
            return False

