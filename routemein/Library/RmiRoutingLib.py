from cgitb import text
import imp
import string

from  Library.ports.RmiPortManage import Port
from  Library.ipHandling import RmiIPv4Lib as ip



class routingHandler:
    
    
    @staticmethod
    def addressingRipV4(routers)->string:  
        
        text = ""
        for router in routers:
            text += "--------- router "+str(router.name)+" ------------\n"
            text += "router Rip\n"
            devicesConected = router.portsConected()
            
            for device in devicesConected:
                text += "network "+str(device.ipConected())+"\n"
            text += "exit\n\n"
            
  
        return text
    
    
    @staticmethod
    def addressingOSPF(routers)->string:  
        
        text = ""
        for router in routers:
            text += "--------- router "+str(router.name)+" ------------\n"
            text += "router ospf \n"
            devicesConected = router.portsConected()
            
            for device in devicesConected:
                ipConected = device.ipConected()
                text += "network "+str(ipConected)+" "+str(ipConected.getWildcard())+" area "+str(device.conection.area)+"\n"
            text += "exit\n\n"
            
  
        return text
        
        
        
        
        
        
        


