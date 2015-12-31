__author__ = 'Fabrice Servais'


class FaultCode(object):
    AgentNotReachable = 10
    DeviceNotReachable = 20


class Fault(object):
    """
    Class representing a fault in the APIC, encapsulating the tuple: (path, code, description)
    """

    def __init__(self, object_path, code, fault_desc):
        self.object_path = object_path
        self.code = code
        self.fault_desc = fault_desc

    def value(self):
        """
        Get the associated tuple of the fault.

        Returns: Tuple<String, int, String>
            Tuple<String, int, String>: Tuple representation a fault: (path, code, description)

        """
        return self.object_path, self.code, self.fault_desc