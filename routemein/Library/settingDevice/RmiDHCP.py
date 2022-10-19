import imp
import string
from tokenize import String


from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip



class DhcpEasyIP():

    def __init__(self, name: String ,initialIp: ip, hostExclusives :None ,dns_Server: ip ):
        self.name = name
        self.initialIp = initialIp
        self.mask = initialIp.getMaskIp()
        self.gateWay = initialIp.increaseHost(1)
        self.dns_Server = dns_Server
        self.hostExclusives = hostExclusives      
        if self.hostExclusives != None:
            for i in self.hostExclusives:
                i[1] = i[0].increaseHost(i[1])
             
        
    def __str__(self) -> string:
        text = "---------DhcpEasyIP: "+self.name +"---------\n" 
        text += "Initial Ip: " + str(self.initialIp) + "\n"
        text += "Mask: " + str(self.mask) + "\n"
        text += "GateWay: " + str(self.gateWay) + "\n"
        text += "Dns_Server: " + str(self.dns_Server) + "\n"
        for host in self.hostExclusives:
            text += "Host: " + str(host[0]) +" - " + str(host[1])+  "\n" 
        return text
    
  
