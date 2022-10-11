import imp
import string


from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip
from Library.settingDevice.RmiPortManage  import Port as port


class HostDevice(Device):

    def __init__(self, name: string,  assignedIp: ip = None, fastEthernetPorts: port = None):
        self.assignedIp = assignedIp
        super().__init__(name, fastEthernetPorts)

    def __str__(self) -> string:
        text = "" 
        text += super().__str__()
        text += "   Assigned Ip: " + str(self.assignedIp) + "\n"
        return text
    
  
