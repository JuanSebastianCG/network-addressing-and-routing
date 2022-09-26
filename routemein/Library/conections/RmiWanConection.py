from cgitb import text
import imp
import string


from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

from Library.conections.RmiConection import Conection


class WanConection(Conection):

    def __init__(self, device1: Device, device2: Device, ipWan: ip):

        """ update ports of connected devices """
        self.portSerial1 = WanConection.selectPorts(device1,device2)
        self.portSerial2 = WanConection.selectPorts(device2,device1)
        
        """ taking into account the parent ip assigns an ipa to each connection without taking the broadcast or network """
        self.ipWan1 = ipWan.increaseHost(1)
        self.ipWan2 = ipWan.increaseHost(2)
        
        super().__init__(device1, device2)

    def __str__(self) -> string:
        text = ""
        text += "ipWan1: " + str(self.ipWan1) + "\n"
        text += "ipWan2: " + str(self.ipWan2) + "\n"
        text += "   Device conection: " + self.device1.name+'  '+ self.portSerial1.name+' <-------------> '+self.portSerial2.name+" "+self.device2.name+"\n"
        
        return text


    def selectPorts(device1,device2):
        for port in device1.serialPorts:
            if port.isFree:    
                port.addDevice(device2,"wan")
                return port
        raise Exception("Error: The device has no free serial ports")
