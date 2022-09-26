import imp
import string


from Library.devices.RmiDevice import Device
from Library.devices.RmiHostDevice import HostDevice
from Library.devices.RmiRouterDevice import RouterDevice

from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

from Library.conections.RmiConection import Conection


class FastEthernet(Conection):

    def __init__(self, device1: Device, device2: Device):
        
        """ verify that the connection is from router to pc """
        if (type(device1) == HostDevice and type(device2) == RouterDevice):
            self.ipHosts = device1.assignedIp
        elif (type(device1) == RouterDevice and type(device2) == HostDevice):
            self.ipHosts = device2.assignedIp
        else:
            raise Exception("Error: The devices are not compatible")
        
        """ update device ports """
        self.portFastEthernet1 = FastEthernet.selectPorts(device1,device2)
        self.portFastEthernet2 = FastEthernet.selectPorts(device2,device1)
        self.ipAssignedToHost = self.ipHosts.increaseHost(1)

        super().__init__(device1, device2)
        
        
    def __str__(self) -> string:
        text = "" 
        text += "ipHosts: " + str(self.ipHosts) + "\n"
        text += "ipRouter: " + str(self.ipAssignedToHost) + "\n"
        text += "   Device conection: " + self.device1.name+'  '+ self.portFastEthernet1.name+' <-------------> '+self.portFastEthernet2.name+" "+self.device2.name+"\n"
        return text

    def selectPorts(device1,device2):
        
        for port in device1.fastEthernetPorts:
            if port.isFree:
                port.addDevice(device2,"fastEthernet")
                return port
        raise Exception("Error: The device has no free fastEthernet ports")