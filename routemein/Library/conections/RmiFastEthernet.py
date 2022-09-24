import imp
import string


from Library.devices.RmiDevice import Device
from Library.devices.RmiHostDevice import HostDevice
from Library.devices.RmiRouterDevice import RouterDevice


from Library.conections.RmiConection import Conection


class FastEthernet(Conection):

    def __init__(self, device1: Device, device2: Device):

        self.device1FastEthernet = FastEthernet.selectPorts(device1)
        self.device2FastEthernet = FastEthernet.selectPorts(device2)

        if (type(device1) == HostDevice and type(device2) == RouterDevice):
            self.ipHosts = device1.assignedIp
        elif (type(device1) == RouterDevice and type(device2) == HostDevice):
            self.ipHosts = device2.assignedIp
        else:
            raise Exception("Error: The devices are not compatible")

        super().__init__(device1, device2)

    def __str__(self) -> string:
        text = "ipHosts: " + str(self.ipHosts) + "\n"
        text += super().__str__()
        return text

    def selectPorts(device1):
        for port in device1.fastEthernetPorts:
            if port.isFree:
                port.isFree = False
                return port
        raise Exception("Error: The device has no free fastEthernet ports")