
import imp
from operator import ipow
import string
from unicodedata import name

from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip
from Library.ports.RmiPortManage import Port



""" this parent class is created to provide a base for connection types like wan and fastetherned """
class Conection:
    
   def __init__(self, device1: Device, device2: Device, area , port1 = None, port2 =None, ip1 = None, ip2 = None):
      
      self.ip1 = ip1
      self.ip2 = ip2
      
      self.area = area
      
      self.port1 = port1
      self.port2 = port2
            
      self.device1 = device1
      self.device2 = device2
      
     
   def __str__(self) -> string:
      text = "\n"
      text += "Area: "+str(self.area)+"\n"
      text += "Device conection: " + self.device1.name +' '+str(self.ip1)+'  '+self.port1.name+'<--------------------->'+self.port2.name+' '+str(self.ip2)+'  '+self.device2.name+"\n"
      return text
   

      
   def searchPortRange(self,device,portHubication, min, max):
        for port in device.fastEthernetPorts:
            number = port.getJustNumber()
            if port.isFree and number >= min and number <= max:
                port.addDevice(self,portHubication)
                return port
        raise Exception("Error: The device has no free fastEthernet ports or the port name is not correct")
   
   def searchPort(self,device,portHubication, portName):
      for port in device.fastEthernetPorts:
         if port.isFree and port.name == portName:
               port.addDevice(self,portHubication)
               return port
      raise Exception("Error: The device has no free fastEthernet ports or the port name is not correct")
         
    
   def selectPorts(self,device,portHubication): 
      for port in device.fastEthernetPorts:
         if port.isFree:
               port.addDevice(self,portHubication)
               return port
      raise Exception("Error: The device has no free fastEthernet ports")
   