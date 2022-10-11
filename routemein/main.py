
from unicodedata import name

""" addresing and routing """
from Library.RmiAddressingLib import addressingHandler as adr
from Library.RmiRoutingLib import routingHandler as rth
from Library.RmiSwitchRoutingLib import SwitchRouting as swr

""" ip management """
from Library.ipHandling.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

""" settings """
from Library.settingDevice.RmiPortManage  import Port as port
from Library.settingDevice.RmiDHCP  import DhcpEasyIP as dhcpEasyIp 
from Library.settingDevice.RmiVlan import Vlan

""" devices """
from Library.devices.RmiHostDevice import HostDevice as hd
from Library.devices.RmiRouterDevice import RouterDevice as rd
from Library.devices.RmiSwitchDevice import SwitchDevice as sd

""" conections """
from Library.conections.RmiFastEthernet import FastEthernet as fc
from Library.conections.RmiWanConection import WanConection as wc




""" ------------test Zone----------------- """


hosts = [30,550,2950] 
hosts =  sorted(hosts, reverse=True)

""" addressing(hosts, ip (opcional)) """
ipAd = adr.addressing(hosts,ip(192,168,10,0,0))
ipAd = adr.addressing(hosts)
ipAd = [ip(192,168,10,0,24), ip(192,168,30,0,24), ip(192,168,20,0,24)]

""" add one host to each ip """
ipAd = adr.addAHostToIps(ipAd)

"""  wanGenerator(wan numbers of wan directions, base ip (optional), 4(number of hosts per wan))"""
wan = rth.wanGenerator(2,ip(220,11,10,0,29))

""" print(adr.showAddressing(ipAd,hosts)) """
""" for i in wan: print(i) """

easyIp = [
    dhcpEasyIp(ip(192,168,10,0,24),9,ip(192,168,20,254,30)),
    dhcpEasyIp(ip(192,168,30,0,24),9,ip(255,255,255,0,30)),
]


""" rd(name of the device, serial port ejem: [port("0/0"),port("0/2")], fasethernet port ejem:  [port("0/0"),port("0/2")]  ) """
routers = [
           rd("router1",[easyIp[0]]),
           rd("router2",),
           rd("router3",[easyIp[1]]),
           rd("router4"),
        ]

""" hd (name, assigned ip(red), fasethernet port :  [port("0/0"),port("0/2")] (opcional))"""
hosts = [hd("pc0", ipAd[0]) ,
         hd("pc1 ", ipAd[2]) ,
         hd("server0 ", ipAd[1]) ,
         hd("server1", ipAd[1]) ,
         hd("server2", ipAd[1]) ,
           ]

""" wc( dispositivo 1, dispositivo 2 ,zona,assigned ip(red), portDispositivo1(opcional), portDispositivo2(opcional)) """""" connection order matters!! """
wanConection = [
                wc(routers[0], routers[1], ip(10,1,1,0,30),0),
                wc(routers[1], routers[2], ip(10,2,2,0,30),0),   
                wc(routers[1], routers[3], ip(209,165,200,224,27),0),   
                ]


""" fc( dispositivo1, dispositivo 2, portDispositivo1(opcional), portDispositivo2(opcionale)) """""" connection order matters!! """
fastEthernetConection = [
                fc(hosts[0], routers[0],0),
                fc(hosts[1], routers[2],0),     
                fc(hosts[2], routers[1],0),     
                ]



""" print(rth.showConections([routers]))  """; """  show all conection of the devices """
print(rth.basicConfiguration(routers)) 
""" print(rth.addressingRipV4(routers))  """
""" print(rth.addressingOSPF(routers))  """
""" print(rth.addressingRipv2OSPF(routers)) """
""" print(rth.addresingStatic(routers,hosts)) """



""" -------------------------------------------- """
