""
import imp
import string



""" this class is assigned to the devices simulating the port entries in each one """
class Port:
    def __init__(self, name: string,isFree: bool = True):
        self.name = name
        self.isFree = isFree
        
        self.conection = None
        self.portHubication = None
        
        
    def __str__(self) -> string:
        text =""
        text += "    Port Name: " + self.name 
        if self.conection != None:
            if self.portHubication == "start":
                text += " <--------> Device Conected: " + self.actualDevice().name + " Port: " + self.conection.port2.name
            elif self.portHubication == "end":
                text += " <--------> Device Conected: " + self.conectedDevice().name + " Port: " + self.conection.port1.name
        return  text
        
    def addDevice(self,conection,portHubication):
        self.isFree = False
        self.conection = conection
        self.portHubication = portHubication
        
    def actualDevice(self):
        if self.portHubication == "start":
            return self.conection.device1
        elif self.portHubication == "end":
            return self.conection.device2
        return None
    
    def conectedDevice(self):
        if self.portHubication == "start":
            return self.conection.device2
        elif self.portHubication == "end":
            return self.conection.device1
        return None
    
    def ipConected(self):
        if self.portHubication == "start":
            return self.conection.ip1
        elif self.portHubication == "end":
             return self.conection.ip2
        return None
        
        
        
        
    
        


   