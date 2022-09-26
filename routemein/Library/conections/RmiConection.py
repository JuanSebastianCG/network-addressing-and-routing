
import imp
from operator import ipow
import string

from Library.devices.RmiDevice import Device
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip



""" this parent class is created to provide a base for connection types like wan and fastetherned """
class Conection:
    
   def __init__(self, device1: Device, device2: Device):
      
      self.device1 = device1
      self.device2 = device2
      
   def __str__(self) -> string:
      text = "Device conection: " + self.device1.name+' <---------------------> '+self.device2.name+"\n"
      return text
   
   """ allows devices added to the connection to update their due slots
   
         Parameters
        ----------
        device1 : class : Device
           List of hosts taken to evaluate
        device2: class : Device
            the initial ip from where each host takes
        Raises
        ------
   
   
   """
   def selectPorts(device1, device2):
      pass
      