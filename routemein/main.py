
from Library.RmiAddressingLib import addressingHandler as adr
from Library.RmiRoutingLib import routingHandler as rth


from Library.ipHandling.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip


from Library.devices.RmiHostDevice import HostDevice as hd
from Library.devices.RmiRouterDevice import RouterDevice as rd

from Library.conections.RmiFastEthernet import FastEthernet as fc
from Library.conections.RmiWanConection import WanConection as wc




""" ------------test Zone----------------- """

hosts = [122,13,312] 
hosts =  sorted(hosts, reverse=True)

""" addressing(hosts, ip (opcional)) """
ipAd = adr.addressing(hosts)
"""  wanGenerator(wan numbers, base ip (optional), 4(number of hosts per wan))"""
wan = rth.wanGenerator(3,None,4)


print(adr.showAddressing(ipAd,hosts))


""" rd(name of the device) """
routers = [rd("r0"),
           rd("r1"),
           rd("r2")]


""" hd (name, host number// ex: 400, assigned ip(red))"""
hosts = [hd("host0",hosts[0], ipAd[0]) ,
         hd("host1 ",hosts[1], ipAd[1]) ,
         hd("host2",hosts[2], ipAd[2])  ]


""" connection order matters!! """
""" wc( dispositivo1, dispositivo 2 ,assigned ip(red)) """
wanConection = [
                wc(routers[0], routers[1], wan[0]),
                wc(routers[1], routers[2], wan[1]),
                wc(routers[2], routers[0], wan[2]),    
                ]

""" connection order matters!! """
""" fc( dispositivo1, dispositivo 2) """
fastEthernetConection = [
                fc(hosts[0], routers[0]),
                fc(hosts[1], routers[1]),     
                fc(hosts[2], routers[2]),     
                ]


""" print(rth.basicConfiguration(routers)) """ 
""" print(rth.addressingRipV4(routers))  """
print(rth.addressingOSPF(routers)) 
""" print(rth.addresingStatic(routers,hosts)) """



 
 