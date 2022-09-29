import imp
import string


from Library.devices.RmiDevice import Device
from Library.ports.RmiPortManage import Port as port


class RouterDevice(Device):

    def __init__(self, name: string,  serialPorts= None, fastEthernetPorts= None):
        """ add serial ports if the user does not provide them """
        if serialPorts == None: self.serialPorts = [port("0/0"), port("0/1"),port("0/2")]
        else: self.serialPorts = serialPorts
            
        super().__init__(name, fastEthernetPorts)


    def __str__(self) -> string:
        text = super().__str__()
        text += "  -Serials: \n" + self.showPorts(self.serialPorts) + "\n"
        return text


    """ returns all port conected """
    def portsConected(self):
        portConected = []
        for port in self.serialPorts:
            if port.isFree == False:
                portConected.append(port)
                
        return super().portsConected(portConected)
    
    def allPorts(self, addPort = []):
        auxArray = addPort
        addPort = [] 
        return super().allPorts( auxArray+self.serialPorts)
    
    """ returns all connected serial ports """
    def serialsPortsConected(self):
        portConected = []
        for port in self.serialPorts:
            if port.isFree == False:
                portConected.append(port)
                
        return portConected
        
