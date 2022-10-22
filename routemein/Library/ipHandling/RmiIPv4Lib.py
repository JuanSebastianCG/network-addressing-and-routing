import string
import random
from gc import callbacks
from operator import ge
from webbrowser import get


from Library.ipHandling.RmiBinaryNumbersLib import binaryNumbersHandler as bnh

class IPv4:
    def __init__(self, oct1: int, oct2: int, oct3: int, oct4: int, mask: int = 8):
        self.ipV4 = [oct1, oct2, oct3, oct4]
        self.mask = mask
        self.check_ip()

    def __str__(self) -> string:
        return str(self.ipV4[0])+'.'+str(self.ipV4[1])+'.'+str(self.ipV4[2])+'.'+str(self.ipV4[3])+ '/' + str(self.mask)


    """ check if the ip is of type int and if it is greater than 0 and less than 255"""
    def check_ip(self) -> None:
        error = 'RmiIPv4Lib: Invalid value for IP at octet '
        if (self.ipV4[0] > 255 or self.ipV4[0] < 0) or (not isinstance(self.ipV4[0], int)):
            raise ValueError(error+'1. Value: '+str(self.ipV4[0]))
        elif (self.ipV4[1] > 255 or self.ipV4[1] < 0) or (not isinstance(self.ipV4[1], int)):
            raise ValueError(error+'1. Value: '+str(self.ipV4[1]))
        elif (self.ipV4[2] > 255 or self.ipV4[2] < 0) or (not isinstance(self.ipV4[2], int)):
            raise ValueError(error+'1. Value: '+str(self.ipV4[2]))
        elif (self.ipV4[3] > 255 or self.ipV4[3] < 0) or (not isinstance(self.ipV4[3], int)):
            raise ValueError(error+'1. Value: '+str(self.ipV4[3]))
        
        
    """Returns the full IP in binary as a string"""
    def get_binary_string(self) -> str:
        return bnh.int_to_bin(self.ipV4[0])+bnh.int_to_bin(self.ipV4[1])+bnh.int_to_bin(self.ipV4[2])+bnh.int_to_bin(self.ipV4[3])
   
    
    """Creates an IP object from a string of an IP in binary. """
    @staticmethod
    def create_new_ip_from_string(binary_str: str, mask: int) -> 'IPv4':
       return IPv4(int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32],  2),mask)
   
    """compares the first ip with the second saying if it is greater than, less than or equal to it"""
    @staticmethod
    def compareIp(ip1: 'IPv4', ip2: 'IPv4') -> bool:
        if ip1.ipV4[0] == ip2.ipV4[0] and ip1.ipV4[1] == ip2.ipV4[1] and ip1.ipV4[2] == ip2.ipV4[2] and ip1.ipV4[3] == ip2.ipV4[3]:
            return "="
        for i in range(4):
            if ip1.ipV4[i] > ip2.ipV4[i]:
                return ">"
            elif ip1.ipV4[i] < ip2.ipV4[i]:
                return "<"
        
        
   
    """ generates an ip given a mask """
    @staticmethod
    def generateIp(mask: int):
        firstOct = []
        secondOct = []
        """C"""
        if mask <=32  and mask >= 24:  
            firstOct = [192, 255]
            secondOct = [168, 168]

            """ class B """
        elif mask < 24  and mask >= 17:  
            firstOct = [10, 171]
            secondOct = [16, 255]
        
            """ class A """
        elif mask <=16  and mask >= 8:  
            firstOct = [10, 171]
            secondOct = [16, 31]
        
        return  IPv4(random.randint(firstOct[0],firstOct[1]), random.randint(secondOct[0],secondOct[1]), 0, 0, mask)
        
        
    
    
    """
    returns the subclass of the ip depending on the mask
    
         Parameters
        ----------
        increase : int // how many subclasse we want to increase
        Raises
        ------
        NotImplementedError
    
    """
    def increaseSubclass(self, increase: int):
        auxIp = IPv4(self.ipV4[0], self.ipV4[1], self.ipV4[2], self.ipV4[3], self.mask)
        for i in range(increase): 
            auxIp = bnh.sum(auxIp.get_binary_string(),'1'+bnh.zerosIp[:32 - auxIp.mask] )
            auxIp = self.create_new_ip_from_string(auxIp, self.mask)
        return auxIp
    
    """
    returns one ip plus the number of hosts that we want to increase
    
         Parameters
        ----------
        increase : inthow many hosts we want to increase
        ------
        NotImplementedError
    
    """
    def increaseHost(self, increase: int):

        auxIp = IPv4(self.ipV4[0], self.ipV4[1], self.ipV4[2], self.ipV4[3], self.mask)

        for i in range(increase):
            auxIp = bnh.sum(auxIp.get_binary_string(),"1" )
            auxIp = self.create_new_ip_from_string(auxIp, self.mask)
  
        return auxIp


    """------------------------------------------getters---------------------------------------------  """

    def getAllData(self) -> string:
        text = 'IP: '+str(self)+'\n'
        text += 'Class: '+self.getClassIp()+'\n'
        text += 'Mask: '+self.getMaskIp()+'\n'
        text += 'Wildcard: '+self.getWildcard()+'\n'
        text += 'hosts available : '+str(self.getHosts()-2)+"  red available :"+str(self.getAvailableRed())+'\n'
        return text

    def getHosts(self) -> int:
        return 2**(32-self.mask)
    
    def getOnlyIp(self):
        return str(self.ipV4[0])+'.'+str(self.ipV4[1])+'.'+str(self.ipV4[2])+'.'+str(self.ipV4[3])
        
    """ returns the number of ip networks that an ip can have """
    def getAvailableRed(self) -> string:
        classIp = self.getClassIp()
        availableIp : int 
        if classIp == 'A':
            availableIp = 2**(self.mask-3)
        elif classIp == 'B':
            availableIp = 2**(self.mask-2)
        elif classIp == 'C':
            availableIp = 2**(self.mask-1)
        return availableIp
    
    def getClassIp(self) -> string: 
        hosts = self.getHosts()
        if  hosts <= 255  and hosts >= 0:
            return 'C'
        elif hosts <= 65535 and hosts >= 256:
            return 'B'
        elif hosts <= 16777215 and hosts >= 65536:
            return 'A'
        
            
    def getWildcard(self) -> string:
        ip = ''
        limit =  self.mask//8 
        for i in range(self.ipV4.__len__()):
            if i == limit:
                ip += str(2**(8-(self.mask - 8*i ))-1)
            elif i<limit:
                ip += '0'
            else:
                ip += '255'  
                    
            if i < 3:
                ip += '.'  
        return ip
    
    
    def getMaskIp(self) -> string:
        ip = ''
        limit =  self.mask//8 
        
        for i in range(self.ipV4.__len__()):
            if i == limit:
                ip += str(bnh.bin_to_int(bnh.ones[:self.mask - limit*8]+bnh.zeros[:8-(self.mask - limit*8)]))
            elif i<limit:
                ip += '255'
            else:
                ip += '0'  
                    
            if i < 3:
                ip += '.'  
        return ip