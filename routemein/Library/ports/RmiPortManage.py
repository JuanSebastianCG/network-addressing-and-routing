""
import imp
import string

""" this class is assigned to the devices simulating the port entries in each one """
class Port:
    def __init__(self, name: string,isFree: bool = True):
        self.name = name
        self.isFree = isFree
        self.typeOfConection = None
        self.device = None
        
        
    def __str__(self) -> string:
        text =""
        text += "    Port Name: " + self.name 
        if self.device != None:
            text += " <----"+self.typeOfConection+"----> Device Conected: " + self.device.name 
        return  text
        
    def addDevice(self,device,typeOfConection):
        self.device = device
        self.isFree = False
        self.typeOfConection = typeOfConection
        


   