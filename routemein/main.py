
""" addresing and routing """
from Library.RmiAddressingLib import addressingHandler as adr
from Library.RmiRoutingLib import routingHandler as rth

""" ip management """
from Library.ipHandling.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

""" port """
from Library.ports.RmiPortManage import Port as port


""" devices """
from Library.devices.RmiHostDevice import HostDevice as hd
from Library.devices.RmiRouterDevice import RouterDevice as rd

""" conections """
from Library.conections.RmiFastEthernet import FastEthernet as fc
from Library.conections.RmiWanConection import WanConection as wc




""" ------------test Zone----------------- """

hosts = [1000,500,30, 20] 
hosts =  sorted(hosts, reverse=True)

""" addressing(hosts, ip (opcional)) """
ipAd = adr.addressing(hosts,ip(198,168,0,0,29))
"""  wanGenerator(wan numbers, base ip (optional), 4(number of hosts per wan))"""
wan = rth.wanGenerator(5,ip(192,168,0,0,29))


print(adr.showAddressing(ipAd,hosts))
""" for i in wan:
    print(i) """


""" rd(name of the device, serial port ejem: [port("0/0"),port("0/2")], fasethernet port ejem:  [port("0/0"),port("0/2")]  ) """
routers = [rd("router0"),
           rd("router1"),
           rd("router2"),
           rd("router3"),
           rd("router4")]


""" hd (name, host number// ex: 400, assigned ip(red), fasethernet port :  [port("0/0"),port("0/2")])"""
hosts = [hd("host0",hosts[0], ipAd[0]) ,
         hd("host1 ",hosts[1], ipAd[1]) ,
         hd("host1 ",hosts[2], ipAd[2]) ,
         hd("host2",hosts[3], ipAd[3])  ]


""" connection order matters!! """
""" wc( dispositivo1, dispositivo 2 ,zona,assigned ip(red), portDispositivo1(opcional), portDispositivo2(opcional)) """
wanConection = [
                wc(routers[0], routers[1], wan[0],0),
                wc(routers[1], routers[3], wan[1],0),
                wc(routers[3], routers[2], wan[2],0),    
                wc(routers[0], routers[2], wan[3],0),    
                wc(routers[3], routers[4], wan[4],0),    
                ]

""" connection order matters!! """
""" fc( dispositivo1, dispositivo 2, portDispositivo1(opcional), portDispositivo2(opcionale)) """
fastEthernetConection = [
                fc(hosts[0], routers[1],0),
                fc(hosts[1], routers[0],0),     
                fc(hosts[2], routers[2],0),     
                fc(hosts[3], routers[4],0),     
                ]


""" print(rth.showConections([routers, hosts])) """ ; """  show all conection of the devices """
print(rth.basicConfiguration(routers)) 
""" print(rth.addressingRipV4(routers))  """
""" print(rth.addressingOSPF(routers))  """
""" print(rth.addresingStatic(routers,hosts)) """



 
 