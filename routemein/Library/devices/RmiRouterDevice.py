import imp
import string


from Library.devices.RmiDevice import Device
from Library.settingDevice.RmiPortManage  import Port as port
from Library.settingDevice.RmiNAT import NAT as nat


class RouterDevice(Device):

    def __init__(self, name: string, settings = None ,serialPorts= None, fastEthernetPorts= None):
        
        if settings == None: self.settings = []
        else: self.settings = settings
        
        """ add serial ports if the user does not provide them """
        if serialPorts == None: self.serialPorts = [port("0/0"), port("0/1"),port("0/2")]
        else: self.serialPorts = serialPorts
        
        for setting in self.settings:
            if type(setting) == nat:
                setting.mainDevice = self
            
        super().__init__(name, fastEthernetPorts)


    def __str__(self) -> string:
        text = super().__str__()
        text += "  -Serials: \n" + self.showPorts(self.serialPorts) + "\n"
        for conf in self.settings:
            text += str(conf) + "\n"
        return text


    """ returns all port conected """
    def portsConected(self):
        portConected = []
        for port in self.serialPorts:
            if port.isFree == False:
                portConected.append(port)  
        return super().portsConected(portConected)
    
    """ return all types of ports whether fastethernet or serial and it does not matter if they are connected """
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
        
