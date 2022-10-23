from cgitb import lookup
import imp
import string

from Library.settingDevice.RmiPortManage  import Port as port



""" this class is taken as parent to represent devices like routers or computers """
class Device:
    
    def __init__(self ,name, fastEthernetPorts ):
        self.name = name
        """ add fastEthernetPorts ports if the user does not provide them """
        if fastEthernetPorts == None: self.fastEthernetPorts = [port("0/0"),port("1/0")]
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
            text += str(port) + "\n"
        return text 
    
    """ returns all connected fastethernet ports """
    def fastEthernetPortsConected(self):
        portConected = []
        for port in self.fastEthernetPorts:
            if port.isFree == False:
                portConected.append(port) 
      
        return portConected
    
    """ returns all port conected """
    def portsConected(self,portConected = []):
        if len(portConected) == 0: portConected = []
        for port in self.fastEthernetPorts:
            if port.isFree == False:
                portConected.append(port) 
      
        return portConected

    """ return all ports including those of subclasses """
    def allPorts(self, addPort = []):
        auxArray = addPort
        addPort = [] 
        return auxArray+self.fastEthernetPorts
    
    

    
            
            
            
            
        
    
    
    

