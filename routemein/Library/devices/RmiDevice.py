import imp
import string

from Library.ports.RmiPortManage import Port as port

class Device:
    
    
    def __init__(self ,name, fastEthernetPorts ):
        self.name = name
        
        if fastEthernetPorts == None: self.fastEthernetPorts = [port("0/0", True)]
        else: self.fastEthernetPorts = fastEthernetPorts
    
    def __str__(self) -> string:
        text = "Device Name: " + self.name +"\n"
        text +="\nFastEthernet Gates: \n" + self.showPorts(self.fastEthernetPorts) +"\n"
        return  text
    
    def showPorts(self, arrayPort):
        text = "" 
        for port in arrayPort:
            text += str(port)
        return text
            
            
        
    
    
    

