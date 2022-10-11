from cgitb import text
import imp
import string


from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

from Library.conections.RmiConection import Conection


class WanConection(Conection):

    def __init__(self, device1: Device, device2: Device, ipWan: ip, area:int = 0, portSerial1:string = None, portSerial2 = None):
        
        if (device1 == device2):
            raise Exception("WanConection: The devices are the same")
        
        
        if portSerial1 != None: port1 = self.searchPort(device1,"start",portSerial1)
        else: port1 = WanConection.selectPorts(self,device1,"start")
        
        if portSerial2 != None:port2 = self.searchPort(device2,"end",portSerial2)
        else: port2 = WanConection.selectPorts(self,device2,"end")

  
        """ taking into account the parent ip assigns an ipa to each connection without taking the broadcast or network """
        super().__init__(device1, device2, area,
                         port1,
                         port2,  
                         ipWan.increaseHost(1),
                         ipWan.increaseHost(2))
        

    def __str__(self) -> string:
        text = ""
        text += "ipWan1: " + str(self.ip1) + "\n"
        text += "ipWan2: " + str(self.ip2) + "\n"
        text += super().__str__()
        
        return text



    def searchPort(self,device,portHubication, portName):
        for port in device.serialPorts:
            if port.isFree and port.name == portName:    
                port.addDevice(self,portHubication)
                return port
        raise Exception("Error: The device has no free serial ports or the port name is not correct")
    
    def selectPorts(self,device,portHubication):
        for port in device.serialPorts:
            if port.isFree:    
                port.addDevice(self,portHubication)
                return port
        raise Exception("Error: The device has no free serial ports")
