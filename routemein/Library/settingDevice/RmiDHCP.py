from ast import While
import imp
import string
from tokenize import String



from Library.ipHandling.RmiIPv4Lib import IPv4 as ip



class DhcpEasyIP():

    def __init__(self, name: String ,initialIp: ip, hostExclusives :None ,dns_Server: ip , gateWay: ip = None):
        self.name = name
        self.initialIp = initialIp
        self.mask = initialIp.getMaskIp()
        self.dns_Server = dns_Server
        self.hostExclusives = hostExclusives
        self.nextIp = 1
             
        if gateWay == None:
            self.gateWay = initialIp.increaseHost(1)
        else:
            self.gateWay = gateWay
        
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
    
    """ taking into account the exclusive hosts, you will find the following suitable ip for a host """
    def getNextIp(self):
        if self.hostExclusives != None:
            for i in range(100):
                newIp = self.initialIp.increaseHost(self.nextIp)
                for host in self.hostExclusives:
                    ipStatus1 = ip.compareIp(newIp,host[0])
                    ipStatus2 = ip.compareIp(newIp,host[1])
                    
                    if (ipStatus1 == ">" or  ipStatus1 == "=") and (ipStatus2 == "<" or ipStatus2 == "="):
                        self.nextIp += 1
                        break
                    else:
                        return newIp
                
        return self.initialIp.increaseHost(1)
    
  
