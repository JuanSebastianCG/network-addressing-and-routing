import imp
import string


from Library.devices.RmiDevice import Device
from Library.devices.RmiHostDevice import HostDevice
from Library.devices.RmiRouterDevice import RouterDevice

from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

from Library.conections.RmiConection import Conection


class FastEthernet(Conection):

    def __init__(self, device1: Device, device2: Device, area = 0):
        
        """ verify that the connection is from router to pc """
        ip1 = None
        ip2 = None
        
        if (type(device1) == HostDevice and type(device2) == RouterDevice):
            ip1 = device1.assignedIp.increaseHost(2)
            ip2 = ip1.increaseHost(1)
        elif (type(device1) == RouterDevice and type(device2) == HostDevice):
            ip2 = device2.assignedIp.increaseHost(2)
            ip1 = ip2.increaseHost(1)
        elif ( device1 == device2):
            raise Exception("FastEthernetConection: The devices are the same")
        else:
            raise Exception("FastEthernetConection: The devices are not compatible")
        
        
      
        super().__init__(device1, device2, area ,FastEthernet.selectPorts(self,device1,"start"),FastEthernet.selectPorts(self,device2,"end"),ip1,ip2)
    
        
        
    def __str__(self) -> string:
        text = "" 
        if (type(self.device1) == HostDevice and type(self.device2) == RouterDevice):
            text += "ipHosts: " + str(self.ip1) + "\n"
            text += "ipRouter: " + str(self.ip2) + "\n"       
        elif (type(self.device1) == RouterDevice and type(self.device2) == HostDevice):
            text += "ipHosts: " + str(self.ip2) + "\n"
            text += "ipRouter: " + str(self.ip1) + "\n"  
        text += super().__str__()
        return text


    def selectPorts(self,device,portHubication): 
        for port in device.fastEthernetPorts:
            if port.isFree:
                port.addDevice(self,portHubication)
                return port
        raise Exception("Error: The device has no free fastEthernet ports")