__author__ = 'Fabrice Servais'


class NginxBackendServerParameters:

    def __init__(self, backup="False", down="False", fail_timeout="-1", max_fails="-1", weight="-1"):
        self.backup = backup
        self.down = down
        self.fail_timeout = fail_timeout
        self.max_fails = max_fails
        self.weight = weight

    def __str__(self):
        to_print_backup = "'backup': '{}'".format(self.backup) if self.backup != "False" else ""
        to_print_down = "'down': '{}'".format(self.down) if self.down != "False" else ""
        to_print_fail_timeout = "'fail_timeout': '{}'".format(self.fail_timeout) if self.fail_timeout != "-1" else ""
        to_print_max_fails = "'max_fails': '{}'".format(self.max_fails) if self.max_fails != "-1" else ""
        to_print_weight = "'weight': '{}'".format(self.weight) if self.weight != "-1" else ""

        l = [to_print_backup, to_print_down, to_print_fail_timeout, to_print_max_fails, to_print_weight]

        to_return = ""
        for i in range(0, len(l)):
            if l[i] != "":
                to_return += l[i]

                if i != len(l)-1:
                    to_return += ', '

        return "{{ {} }}".format(to_return)

    def __repr__(self):
        return str(self)

    # def __str__(self):
    #     return "{{ 'backup':'{backup}' }}".format(backup=self.backup)
    #
    # def __repr__(self):
    #     return str(self)