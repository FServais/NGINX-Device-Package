__author__ = 'Fabrice Servais'


class NginxServerLocation:

    def __init__(self, backend_name="", uri="", pass_method="proxy_pass", https="False"):
        self.uri = uri
        self.pass_method = pass_method
        self.https = https
        self.backend_name = backend_name

    def __str__(self):
        return "{{ 'backend_name': '{}', 'uri': '{}', 'pass_method': '{}', 'https': '{}' }}".format(self.backend_name, self.uri, self.pass_method, self.https)

    def __repr__(self):
        return str(self)
