
class FaultCode(object):
    AgentNotReachable = 10
    DeviceNotReachable = 20

class Fault(object):
    def __init__(self, object_path, code, fault_desc):
        self.object_path = object_path
        self.code = code
        self.fault_desc = fault_desc

    def value(self):
        return (self.object_path, self.code, self.fault_desc)