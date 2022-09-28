import imp
import string


from Library.devices.RmiDevice import Device
from Library.devices.RmiHostDevice import HostDevice
from Library.devices.RmiRouterDevice import RouterDevice

from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

from Library.conections.RmiConection import Conection


class FastEthernet(Conection):

    def __init__(self, device1: Device, device2: Device, area = 0, portFastethernet1 = None, portFastethernet2 =None):
        
        """ verify that the connection is from router to pc """
        ip1 = None
        ip2 = None
        
        if (type(device1) == HostDevice and type(device2) == RouterDevice):
            ip1 = device1.assignedIp.increaseHost(1)
            ip2 = ip1.increaseHost(2)
        elif (type(device1) == RouterDevice and type(device2) == HostDevice):
            ip2 = device2.assignedIp.increaseHost(1)
            ip1 = ip2.increaseHost(2)
        elif ( device1 == device2):
            raise Exception("FastEthernetConection: The devices are the same")
        else:
            raise Exception("FastEthernetConection: The devices are not compatible")
        
        if portFastethernet1 != None: port1 = self.searchPort(device1,"start",portFastethernet1)
        else: port1 = FastEthernet.selectPorts(self,device1,"start")
        
        if portFastethernet2 != None: port2 = self.searchPort(device2,"end",portFastethernet2)
        else: port2 = FastEthernet.selectPorts(self,device2,"end")
            
    
        super().__init__(device1, device2, area ,port1 ,port2 ,ip1,ip2)
    
        
        
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

    def searchPort(self,device,portHubication, portName):
        for port in device.fastEthernetPorts:
            if port.isFree and port.name == portName:
                port.addDevice(self,portHubication)
                return port
        raise Exception("Error: The device has no free fastEthernet ports or the port name is not correct")

    def selectPorts(self,device,portHubication): 
        for port in device.fastEthernetPorts:
            if port.isFree:
                port.addDevice(self,portHubication)
                return port
        raise Exception("Error: The device has no free fastEthernet ports")