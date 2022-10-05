import imp
import string


from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip
from Library.ports.RmiPortManage import Port as port


class SwitchDevice(Device):

    def __init__(self, name: string, vlans,assignedIp: ip = None, fastEthernetPorts= None):
        self.vlans = vlans
        self.assignedIp: ip = None
        
        if fastEthernetPorts == None:
            fastEthernetPorts = []
            for i in range(0,24):
                if i == 17: continue
                fastEthernetPorts.append(port("0/"+str(i)))
        super().__init__(name, fastEthernetPorts)


    def __str__(self) -> string:
        text = ""
        text += super().__str__()
        for vlan in self.vlans:
            text +=str(vlan.name) +" "+str(vlan.number) +" range: " +  str(vlan.fastethernetRangeIn) + "-" + str(vlan.fastethernetRangeFin) + "\n"
        return text
    


    def getVlanGigaethernet(self):
        for vlan in self.vlans:
            if vlan.gigaethernet:
                return vlan




