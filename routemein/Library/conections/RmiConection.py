
import imp
from operator import ipow
import string

from Library.devices.RmiDevice import Device
from Library.RmiIPv4Lib import IPv4 as ip

class Conection:
    
   def __init__(self, device1: Device, device2: Device):
      
      self.device1 = device1
      self.device2 = device2
      
   def __str__(self) -> string:
      text = "Device conection: " + self.device1.name+' <---------------------> '+self.device2.name+"\n"
      return text
   
   def selectPorts(device1, device2):
      pass
      