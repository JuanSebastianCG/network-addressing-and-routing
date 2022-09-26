
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
      
      self.ip1 = ip2
      self.ip2 = ip1
      
      self.area = area
      
      self.port1 = port1
      self.port2 = port2
            
      self.device1 = device1
      self.device2 = device2
      
   def __str__(self) -> string:
      text = ""
      text += "Area: "+self.area+"\n"
      text += "Device conection: " + self.device1.name +'  '+self.port1.name+'<--------------------->'+self.port2.name+'  '+self.device2.name+"\n"
      return text
   
   """ allows devices added to the connection to update their due slots"""
   def selectPorts(device1, device2):
      pass
      