import imp
import string


from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip
from Library.ports.RmiPortManage import Port as port


class HostDevice(Device):

    def __init__(self, name: string, hosts: int, assignedIp: ip, fastEthernetPorts: port = None):
        self.hosts = hosts
        self.assignedIp = assignedIp
        super().__init__(name, fastEthernetPorts)

    def __str__(self) -> string:
        text = "Hosts: " + str(self.hosts) + "\n"
        text += "Assigned Ip: " + str(self.assignedIp) + "\n"
        text += super().__str__()
        return text
