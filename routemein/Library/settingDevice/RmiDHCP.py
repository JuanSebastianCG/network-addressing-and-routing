import imp
import string
from tokenize import String


from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip



class DhcpEasyIP():

    def __init__(self, initialIp: ip, hostExclusives ,dns_Server: ip ):
        self.initialIp = initialIp
        self.mask = initialIp.getMaskIp()
        self.gateWay = initialIp.increaseHost(1)
        self.dns_Server = dns_Server
        self.initialExclusion = initialIp.increaseHost(1)
        self.finalExclusion = initialIp.increaseHost(hostExclusives)
        
        
    def __str__(self) -> string:
        text = "---------DhcpEasyIP---------\n" 
        text += "Initial Ip: " + str(self.initialIp) + "\n"
        text += "Mask: " + str(self.mask) + "\n"
        text += "GateWay: " + str(self.gateWay) + "\n"
        text += "Dns_Server: " + str(self.dns_Server) + "\n"
        text += "Exclusion: " + str(self.initialExclusion) + " - " +str(self.finalExclusion) +"\n"
        return text
    
  
