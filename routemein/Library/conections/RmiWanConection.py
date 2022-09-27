from cgitb import text
import imp
import string


from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

from Library.conections.RmiConection import Conection


class WanConection(Conection):

    def __init__(self, device1: Device, device2: Device, ipWan: ip, area = 0):
        
        
        if (device1 == device2):
            raise Exception("WanConection: The devices are the same")

        """ taking into account the parent ip assigns an ipa to each connection without taking the broadcast or network """
        super().__init__(device1, device2, area,
                         WanConection.selectPorts(self,device1,"start"),
                         WanConection.selectPorts(self,device2,"end"),  
                         ipWan.increaseHost(1),
                         ipWan.increaseHost(2))
        

    def __str__(self) -> string:
        text = ""
        text += "ipWan1: " + str(self.ip1) + "\n"
        text += "ipWan2: " + str(self.ip2) + "\n"
        text += super().__str__()
        
        return text


    def selectPorts(self,device,portHubication):
        for port in device.serialPorts:
            if port.isFree:    
                port.addDevice(self,portHubication)
                return port
        raise Exception("Error: The device has no free serial ports")
