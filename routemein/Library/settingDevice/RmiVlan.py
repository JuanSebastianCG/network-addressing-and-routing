import imp
import string


from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

class Vlan():
    
    def __init__(self , nextHostsIp: ip ,name, number, fastethernetRangeIn, fastethernetRangeFin,  gigaethernet: bool = False ):
        self.name = name
        self.number = number
        self.fastethernetRangeIn = fastethernetRangeIn
        self.fastethernetRangeFin = fastethernetRangeFin
        self.gigaethernet = gigaethernet 
        self.nextHostsIp = nextHostsIp
        
    def __str__(self) -> string:
        text = ""
        text += "Vlan Name: " + self.name + "\n"
        text += "Vlan Number: " + str(self.number) + "\n"
        text += "FastEthernet Range: " + str(self.fastethernetRangeIn) + " - " + str(self.fastethernetRangeFin) + "\n"
        text += "GigaEthernet: " + str(self.gigaethernet) + "\n"
        text += "Next Host Ip: " + str(self.nextHostsIp) + "\n"
        return  text
    
    
    def getNextIpforVlan(self):
        self.nextHostsIp = self.nextHostsIp.increaseHost(1)
        return self.nextHostsIp
