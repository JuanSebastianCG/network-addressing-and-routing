from cgitb import text
import imp
import string

from  Library.ports.RmiPortManage import Port



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
            text += "router Rip\n"
            devicesConected = router.portsConected()
            
            for device in devicesConected:
                text += "network "+str(device.ipConected())+"\n"
            text += "exit\n\n"
            
  
        return text
        
        
        
        
        
        
        


