from pprint import PrettyPrinter

__author__ = 'Fabrice Servais'


class ReturnValue:
    def __init__(self, state, health, fault):
        self.return_value = {'state': state, 'health': health, 'fault': fault}

    def __repr__(self):
        return "{}".format(self.return_value)

    def __str__(self):
        return PrettyPrinter(indent=2).pformat(self.return_value)

    def get_return_value(self):
        return self.return_value

if __name__ == "__main__":
    ret = ReturnValue(0, [], [])
    print(ret)