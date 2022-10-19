from ast import For

import imp
from pickle import NONE
import string
from telnetlib import IP


from Library.RmiAddressingLib import addressingHandler as addressing
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

from Library.devices.RmiRouterDevice import RouterDevice as router
from Library.devices.RmiHostDevice import HostDevice as host
from Library.settingDevice.RmiDHCP import DhcpEasyIP as dhcpE



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
                deviceConected = port.conectedDevice()
   
                text += "interface fastethernet "+str(port.name)+"\n"
                if(type(deviceConected) == host):
                    text += "ip address "+str(deviceConected.gateWay.getOnlyIp())+" "+str(deviceConected.gateWay.getMaskIp())+"\n"
                text += "no shutdown\n"
                text += "exit\n"

            portSerial = router.serialsPortsConected()
            for port in portSerial:
                text += "interface serial "+str(port.name)+"\n"
                text += "ip addres "+ str(port.ipConected().getOnlyIp())+" "+str(port.ipConected().getMaskIp())+"\n"
                if port.portHubication == "start":
                    text += "clock rate 250000\n"
                text += "no shutdown\n"
                text += "exit\n"
            
            
            for setting in router.settings:
                if type(setting) ==  dhcpE:
                    for ip in setting.hostExclusives:
                        text += "ip dhcp excluded-address "+str(ip[0].getOnlyIp())+" "+str(ip[1].getOnlyIp())+"\n"
                    text += "ip dhcp pool "+str(setting.name)+"\n"
                    text += "network "+str(setting.initialIp.getOnlyIp())+" "+str(setting.mask) +"\n"
                    text += "default-router "+str(setting.gateWay.getOnlyIp())+"\n"
                    text += "dns-server "+str(setting.dns_Server.getOnlyIp())+"\n"
            

            text += "\n"   
        return text
        
    
    
    @staticmethod
    def addressingRipV4(routers)->string:  
        text = ""
        for router in routers:
            text += "--------- router "+str(router.name)+" ------------\n"
            text += "configure terminal\n"
            text += "router Rip\n"
            text += "version 2\n"
            devicesConected = router.portsConected()
            
            for device in devicesConected:
                ipConected = device.ipConected()
                text += "network "+str(ipConected.getOnlyIp())+"\n"
            text += "exit\n\n"
            
  
        return text
    
    
    @staticmethod
    def addressingOSPF(routers)->string:  
        
        text = ""
        for router in routers:
            text += "--------- router "+str(router.name)+" ------------\n"
            text += "router ospf 1\n"
            devicesConected = router.portsConected()
            
            for device in devicesConected:
                ipConected = device.ipConected()
                text += "network "+str(ipConected.getOnlyIp())+" "+str(ipConected.getWildcard())+" area "+str(device.conection.area)+"\n"
            text += "exit\n\n"
            
        return text
    
    
    @staticmethod
    def addressingRipv2OSPF(routers)->string:
        
        text = ""
        for router in routers:
            text += "--------- router "+str(router.name)+" --<----------\n"
            text += "router ospf 1\n"
            devicesConected = router.portsConected()
            for device in devicesConected:
                ipConected = device.ipConected()
                text += "network "+str(ipConected.getOnlyIp())+" "+str(ipConected.getWildcard())+" area "+str(device.conection.area)+"\n"
            text += "redistribute rip metric 200 subnet\n"
            text += "exit\n\n"
            
            text += "router Rip\n"
            text += "version 2\n"
            for device in devicesConected:
                text += "network "+str(device.ipConected().getOnlyIp())+"\n"
            text += "redistribute ospf 1 metric 1\n"
            text += "exit\n\n"
                 
        return text
        
    
    
    @staticmethod
    def addresingStatic(routers,hosts)->string:

        text = ""        
        for router in routers:
            text += "--------- router "+str(router.name)+" ------------\n"
            for host in hosts:
                
                wayFound = routingHandler.shortPathStaticRouting(host,router)
                
                for way in wayFound:
                    if str(host.assignedIp.increaseHost(2)) != str(way.ipActual()):
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
            
        """ if the device dont have more conections """
        if actualDevicesPort == None: return None
        
        for port in actualDevicesPort:
            conectedDevice = port.conectedDevice()
            
            """ if the device is difertent to the last device """
            if conectedDevice == lastDevice: continue    
            """ device found """
            """  print("actualDevice: "+str(actualDevice.name)+" conectedDevice: "+str(conectedDevice.name)+" deviceToLook: "+str(deviceToLook.name)+" len: "+str(actualDevicesPort)) """
            if conectedDevice == deviceToLook:
                foundPath.append(port.portActual())
            else:  
                if conectedDevice not in roadTraveled:
                     way = (routingHandler.shortPathStaticRouting(conectedDevice, deviceToLook,  roadTraveled, actualDevice))
                     if way != None:
                         for w in way:
                             foundPath.append(w)


        return foundPath
    
    
    """ --------------------------------------------------------------------------------------------------------- """

    
    
    def showConections(GroupOfDevices):
        text = ""  
          
        for devices in GroupOfDevices:
            for device in devices:
                text += "--------- router "+str(device.name)+" ------------\n"
                for portsConected in device.allPorts():
                    text += str(portsConected)+"\n"
                text += "\n"
            
        return text
            
            
    @staticmethod
    def showHosts(hosts):
        text = ""
        for host in hosts:
            text +=  host.name +"ip:  " + str(host.assignedIp.getOnlyIp()) + " - " + str(host.assignedIp.getMaskIp()) +"  | gateWay "+  str(host.gateWay.getOnlyIp())   +" --------> " +str(host.fastEthernetPorts[0].portConected().name)+"\n"
        return text
            
          
    
    
        
        
        
        
        
        
        


