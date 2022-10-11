import imp
import string


from Library.devices.RmiDevice import Device
from Library.devices.RmiHostDevice import HostDevice
from Library.devices.RmiRouterDevice import RouterDevice
from Library.devices.RmiSwitchDevice import SwitchDevice

from Library.settingDevice.RmiPortManage import Port
from Library.conections.RmiConection import Conection
from Library.settingDevice.RmiVlan import Vlan




class FastEthernet(Conection):

    def __init__(self, device1: Device, device2: Device, area = 0, configuration = None ,portFastethernet1 = None, portFastethernet2 =None):
        
        """ verify that the connection is from router to pc """
        ip1 = None
        ip2 = None
          
        """ ip """
        if (type(device1) == HostDevice ):
            if ((type(device2) == RouterDevice or type(device2) == SwitchDevice) and configuration == None):
                ip1 = device1.assignedIp
                ip2 = ip1.increaseHost(1)
            elif (type(device2) == SwitchDevice and configuration != None):
                ip1 = configuration.getNextIpforVlan()
                device1.assignedIp = ip1
                ip2 = None
  
        elif (type(device2) == HostDevice ):
            if ((type(device1) == RouterDevice or type(device1) == SwitchDevice) and configuration == None):
                ip2 = ip2.increaseHost(1)
                ip1 = device2.assignedIp
            elif (type(device1) == SwitchDevice and configuration != None):
                ip2 = configuration.getNextIpforVlan()
                device2.assignedIp = ip2
                ip1 = None

        elif (type(device1) == SwitchDevice):
            if (type(device2) == RouterDevice) :
                ip1 = device1.assignedIp
                ip2 = None
            elif(type(device2) == SwitchDevice and configuration != None) :
                ip1 = configuration.getNextIpforVlan()
                ip2 = configuration.getNextIpforVlan()
        
        elif (type(device2) == SwitchDevice):
            if (type(device1) == RouterDevice) :
                ip2 = device2.assignedIp
                ip1 = None
            
                         
        """ ports """
        if portFastethernet1 != None: port1 = self.searchPort(device1,"start",portFastethernet1)
        elif (type(configuration) == Vlan and type(device1) == SwitchDevice and configuration != None): port1 = self.searchPortRange( device1,"start",configuration.fastethernetRangeIn,configuration.fastethernetRangeFin)
        else: port1 = FastEthernet.selectPorts(self,device1,"start")
        
        if portFastethernet2 != None: port2 = self.searchPort(device2,"end",portFastethernet2)
        elif (type(configuration) == Vlan and type(device2) == SwitchDevice and configuration != None): port2 = self.searchPortRange( device2,"end",configuration.fastethernetRangeIn,configuration.fastethernetRangeFin)
        else: port2 = FastEthernet.selectPorts(self,device2,"end")
        
        super().__init__(device1, device2, area ,port1 ,port2 ,ip1,ip2)
    
        
        



    
    