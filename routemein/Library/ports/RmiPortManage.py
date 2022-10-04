""
import imp
import string



""" this class is assigned to the devices simulating the port entries in each one """
class Port:
    def __init__(self, name: string,isFree: bool = True):
        self.name = name
        self.isFree = isFree
        
        self.conection = None
        """ this attribute allows you to see if the device is to the right or left of the connection, metaphorically speaking """
        self.portHubication = None
        
        
    def __str__(self) -> string:
        text =""
        if self.conection != None:
            if self.portHubication == "end":
                text += self.conection.port2.name +"  "+self.actualDevice().name+" <--------> Device Conected: " +  self.conectedDevice().name + " Port: " + self.name 
            elif self.portHubication == "start":
                text += self.name +"  "+self.actualDevice().name+ " <--------> Device Conected: " + self.conectedDevice().name + " Port: " + self.conection.port2.name
        else:
            text += self.name+ " <--------> Device Conected: None"
   
        return  text
        
    def addDevice(self,conection,portHubication):
        self.isFree = False
        self.conection = conection
        self.portHubication = portHubication
        
        
    def getJustNumber(self):
        number =  self.name.split("/")
        return number
        
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
    
    def ipActual(self):
        if self.portHubication == "start":
            return self.conection.ip2
        elif self.portHubication == "end":
             return self.conection.ip1
    
    def portActual(self):
        if self.portHubication == "start":
            return self
        elif self.portHubication == "end":
             return self.conection.port2
        return None
    
        
        
        
        
        
        
    
        


   