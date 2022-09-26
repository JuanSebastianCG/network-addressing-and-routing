from cgitb import lookup
import imp
import string

from Library.ports.RmiPortManage import Port as port


""" this class is taken as parent to represent devices like routers or computers """
class Device:
    
    def __init__(self ,name, fastEthernetPorts ):
        self.name = name
        if fastEthernetPorts == None: self.fastEthernetPorts = [port("0/0", True)]
        else: self.fastEthernetPorts = fastEthernetPorts
    
    def __str__(self) -> string:
        text = ""
        text += "---------------------------\n" 
        text += "Device Name: " + self.name +"\n"
        text +="\n  -FastEthernet Gates: \n" + self.showPorts(self.fastEthernetPorts) +"\n"
        return  text
    
    
    """ shows the ports assigned to this device """
    def showPorts(self, arrayPort):
        text = "" 
        for port in arrayPort:  
            text += str(port)
            """ check if any port is connected and show it if so """
            ipConected = self.lookForTherPortConected(port)
            if ipConected != None:
                text += " " + ipConected.name +"\n"
            else:
                text += "\n"     
        return text 
    
    """ if the port is connected it will go looking for which device is connected to the other side """
    def lookForTherPortConected(self, port):
        if port.isFree == False:
           for conectedPort in port.device.fastEthernetPorts:
               if(conectedPort.device == self):
                   return conectedPort
            
            
            
            
        
    
    
    

