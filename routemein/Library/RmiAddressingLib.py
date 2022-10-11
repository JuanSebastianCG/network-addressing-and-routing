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
    def showAddressing(list,device) -> str:
        device =  sorted(device, reverse=True)
        addressing  = ""
        for i in range(len(list)):    
            addressing += "name "+str(device[i])+"\n"    
            addressing += list[i].getAllData()+"\n"
        return  addressing
    
    """ take a list of ips and return a list of strings with the ips plus one host """
    @staticmethod
    def addAHostToIps(ips):
        ispPlusOneHost = []
        for i in range(len(ips)):
            ispPlusOneHost.append(ips[i].increaseHost(1))
        return ispPlusOneHost
    
    
    
        """ generate necessary ips for aggregation to a wan connection
    
         Parameters
        ----------
        amountOf : int // amount of wan connections
        inicIp : ip // ip to start the wan connections ( opcional )
        minHost : int // minimum amount of hosts to be able to connect to the wan ( opcional )
        ------
    """
    @staticmethod
    def wanGenerator(amountOf: int,inicIp: ip = None, minHost = None):
        
        wanIps = []
        if minHost == None and inicIp == None: 
            inicIp = ip.generateIp(addressingHandler.findMask(amountOf))
        elif inicIp == None and minHost != None:
            inicIp = ip.generateIp(addressingHandler.findMask(minHost))
        
        for i in range(amountOf):
            wanIps.append(inicIp.increaseSubclass(i))
            
        return wanIps
    
    
    
    
   