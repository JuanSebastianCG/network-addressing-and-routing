import imp
import string


from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

from Library.conections.RmiConection import Conection


class WanConection(Conection):

    def __init__(self, device1: Device, device2: Device, ipWan: ip):

        self.ipWan = ipWan
        self.device1Serial = WanConection.selectPorts(device1)
        self.device2Serial = WanConection.selectPorts(device2)

        super().__init__(device1, device2)

    def __str__(self) -> string:
        text = "ipWan: " + str(self.ipWan) + "\n"
        text += super().__str__()
        return text

    def selectPorts(device):
        for port in device.serialPorts:
            if port.isFree:
                port.isFree = False
                return port
        raise Exception("Error: The device has no free serial ports")
