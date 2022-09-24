from cgi import print_arguments
import string
from webbrowser import get


from Library.RmiBinaryNumbersLib import binaryNumbersHandler as bnh

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
        
    
    
    """
    returns the subclass of the ip depending on the mask
    
         Parameters
        ----------
        increase : str
            allows us to determine which subclass we want to increase
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
    
    def increaseHost(self, increase: int):
        auxIp = IPv4(self.ipV4[0], self.ipV4[1], self.ipV4[2], self.ipV4[3], self.mask)
        for i in range(increase): 
            auxIp = bnh.sum(auxIp.get_binary_string(),"1" )
            auxIp = self.create_new_ip_from_string(auxIp, self.mask)
        return auxIp
    
        

    """------------------------------------------getters---------------------------------------------  """



    def getHosts(self) -> int:
        return 2**(32-self.mask)
    
    def getRed(self) -> string:
        return 2**(self.mask)
    
    def getClassIp(self) -> string: 
        if self.mask <= 255  and self.mask >= 0:
            return 'C'
        elif self.mask <= 65535 and self.mask >= 256:
            return 'B'
        elif self.mask <= 16777215 and self.mask >= 65536:
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
                ip += str(255+1-self.getHosts())
            elif i<limit:
                ip += '255'
            else:
                ip += '0'  
                    
            if i < 3:
                ip += '.'  
        return ip