from ast import For

import imp
import string


from  Library.ports.RmiPortManage import Port
from  Library.ipHandling import RmiIPv4Lib as ip



class routingHandler:
    
    
    @staticmethod 
    def basicConfiguration(routers):
        text = ""

        for router in routers:
            text += "--------- router "+str(router.name)+" ------------\n"
            text += "enable \n"
            text += "configure terminal\n"
            text += "hostname "+router.name+"\n"
            text += "enable secret class\n"
            text += "enable password cisco\n"
    
            portFastethernet = router.fastEthernetPortsConected()
            for port in portFastethernet:
                text += "interface fastethernet "+str(port.name)+"\n"
            text += "ip addres "+ str(port.ipConected())+" "+str(port.ipConected().getMaskIp())+"\n"
            text += "no shutdown\n"
            text += "exit\n"

            portSerial = router.serialsPortsConected()
            for port in portSerial:
                text += "interface serial "+str(port.name)+"\n"
                text += "ip addres "+ str(port.ipConected())+" "+str(port.ipConected().getMaskIp())+"\n"
                if port.portHubication == "start":
                    text += "clock rate 250000\n"
            text += "no shutdown\n"
            text += "exit\n"  
            text += "\n"   
            
  
        return text
        
    
    
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
    
    
    @staticmethod
    def addresingStatic(routers,hosts)->string:

        text = ""        
        for router in routers:
            for host in hosts:
                
                wayFound = routingHandler.shortPathStaticRouting(host,router)
                
                for way in wayFound:
                    text += "ip route "+str(host.assignedIp)+" "+str(host.assignedIp.getWildcard())+" "+str(way.ipActual())+"\n"
            text += "\n"
        
        return text

   
        
    
  
        
        
        
    """ searches through branches if the device to find is on the network. and returns the ports of that router """  
    @staticmethod
    def shortPathStaticRouting(actualDevice, deviceToLook, roadTraveled = [], lastDevice = None):
        
        actualDevicesPort = actualDevice.portsConected()
        foundPath = []
        
        if lastDevice != None:
            roadTraveled.append(lastDevice)
        else:
            roadTraveled = []

        
        """ si ya no hay mas dispositivos por donde seguir """
        if actualDevicesPort == None: return None
        
        for port in actualDevicesPort:
            conectedDevice = port.conectedDevice()
            
            """ si el puerto es diferente que el de la rama anterior """
            if conectedDevice == lastDevice: continue    
            """ si encontro el dispositivo-+ """
            print("actualDevice: "+str(actualDevice.name)+" conectedDevice: "+str(conectedDevice.name)+" deviceToLook: "+str(deviceToLook.name)+" len: "+str(actualDevicesPort))
            if conectedDevice == deviceToLook:
                foundPath.append(port.portActual())
            else:  
                if conectedDevice not in roadTraveled:
                     way = (routingHandler.shortPathStaticRouting(conectedDevice, deviceToLook,  roadTraveled, actualDevice))
                     if way != None:
                         for w in way:
                             foundPath.append(w)


        return foundPath
    
    
        
        
        
        
        
        
        


