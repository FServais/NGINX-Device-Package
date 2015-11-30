__author__ = 'Fabrice Servais'


class NginxBackendServerParameters:

    def __init__(self, backup=False, down=False, fail_timeout=-1, max_fails=-1, weight=-1):
        """
        Constructor. See details of the parameters: http://nginx.org/en/docs/http/ngx_http_upstream_module.html#server
        :param backup:
        :param down:
        :param fail_timeout:
        :param max_fails:
        :param weight:
        """
        self.backup = backup
        self.down = down
        self.fail_timeout = fail_timeout
        self.max_fails = max_fails
        self.weight = weight

    def __str__(self):
        to_return = {}

        if self.backup:
            to_return["backup"] = self.backup

        if self.down:
            to_return["down"] = self.down

        if self.fail_timeout != -1:
            to_return["fail_timeout"] = self.fail_timeout

        if self.max_fails != -1:
            to_return["max_fails"] = self.max_fails

        if self.weight != -1:
            to_return["weight"] = self.weight

        return "{}".format(to_return)

    def __repr__(self):
        return str(self)

    def export(self):
        to_return = []

        if self.backup:
            to_return.append("backup")

        if self.down:
            to_return.append("down")

        if self.fail_timeout != -1:
            to_return.append("fail_timeout={}".format(self.fail_timeout))

        if self.max_fails != -1:
            to_return.append("max_fails={}".format(self.max_fails))

        if self.weight != -1:
            to_return.append("weight={}".format(self.weight))

        return to_return

    def visit(self, visitor):
        return visitor(self)

if __name__ == "__main__":
    params = NginxBackendServerParameters(backup=True, down=False, fail_timeout=4)
    print(params)
    print(params.export())
