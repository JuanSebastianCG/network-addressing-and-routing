import imp
import string

from Library.ipHandling.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

class addressingHandler:


    """
    returns an array of ips according to the entered hosts
    
         Parameters
        ----------
        list : int
           List of hosts taken to evaluate
        initialIp: ip
            the initial ip from where each host takes
        Raises
        ------
    
    """
    @staticmethod
    def addressing(list, initialIp: ip = None) :
        list =  sorted(list, reverse=True)
        addresingIP = []   
        
        if initialIp == None:
            initialIp = ip.generateIp(addressingHandler.findMask(list[0]))
        
     
        for i in range(len(list)):
              
            initialIp.mask = addressingHandler.findMask(list[i])
            addresingIP.append(initialIp)
            initialIp = initialIp.increaseSubclass(1)

           
        return addresingIP
      
    
    """ find the mask depending on a given host """
    @staticmethod
    def findMask(number: int) -> int:
        mask = 1
        for i in range(2, 25):
            if number <= (2**i)-2:
                mask = 32-i
                break
        
        return mask
    
    """ properly shows the addressing, taking into account the array of hosts and assigned routes """
    @staticmethod
    def showAddressing(list,hosts) -> str:
        hosts =  sorted(hosts, reverse=True)
        addressing  = ""
        for i in range(len(list)):    
            addressing += "host "+str(hosts[i])+" : "+str(list[i])+" mask: "+str(list[i].mask)+"\n"    
        return  addressing
    
   