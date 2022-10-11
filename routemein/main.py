
from unicodedata import name

""" addresing and routing """
from Library.RmiAddressingLib import addressingHandler as Addressing
from Library.RmiRoutingLib import routingHandler as Routing
from Library.RmiSwitchRoutingLib import SwitchRouting as swr

""" ip management """
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

""" settings """
from Library.settingDevice.RmiPortManage  import Port as port
from Library.settingDevice.RmiDHCP  import DhcpEasyIP as dhcpEasyIp 
from Library.settingDevice.RmiVlan import Vlan

""" devices """
from Library.devices.RmiHostDevice import HostDevice as HostD
from Library.devices.RmiRouterDevice import RouterDevice as RouterD
from Library.devices.RmiSwitchDevice import SwitchDevice as SwitchD

""" conections """
from Library.conections.RmiFastEthernet import FastEthernet as FastEthernetConection
from Library.conections.RmiWanConection import WanConection as WanConection




""" ------------test Zone----------------- """


hosts = [30,550,2950] 
hosts =  sorted(hosts, reverse=True)

""" addressing(hosts, ip (opcional)) """
ipAd = Addressing.addressing(hosts,ip(192,168,10,0,0))
ipAd = Addressing.addressing(hosts)
ipAd = [ip(192,168,10,0,24), ip(192,168,30,0,24), ip(192,168,20,0,24)]

""" add one host to each ip """
ipAd = Addressing.addAHostToIps(ipAd)

"""  wanGenerator(wan numbers of wan directions, base ip (optional), 4(number of hosts per wan))"""
wan = Addressing.wanGenerator(2,ip(220,11,10,0,29))

""" print(adr.showAddressing(ipAd,hosts)) """
""" for i in wan: print(i) """


easyIp = [
    dhcpEasyIp(ip(192,168,10,0,24),9,ip(192,168,20,254,30)),
    dhcpEasyIp(ip(192,168,30,0,24),9,ip(255,255,255,0,30)),
]


""" rd(name of the device, serial port ejem: [port("0/0"),port("0/2")], fasethernet port ejem:  [port("0/0"),port("0/2")]  ) """
routers = [
           RouterD("router1",[easyIp[0]]),
           RouterD("router2",),
           RouterD("router3",[easyIp[1]]),
           RouterD("router4"),
        ]


switchs = [
    SwitchD("switch0",None, ipAd[0]),
    SwitchD("switch1",None, ipAd[2]),
    
]



""" hd (name, assigned ip(red), fasethernet port :  [port("0/0"),port("0/2")] (opcional))"""
hosts = [HostD("pc0", ipAd[0]) ,
         HostD("pc1 ", ipAd[2]) ,
         HostD("server0 ", ipAd[1]) ,
         HostD("server1", ipAd[1]) ,
         HostD("server2", ipAd[1]) ,
           ]

""" wc( dispositivo 1, dispositivo 2 ,zona,assigned ip(red), portDispositivo1(opcional), portDispositivo2(opcional)) """""" connection oRouterDer matters!! """
wanConection = [
                WanConection(routers[0], routers[1], ip(10,1,1,0,30),0),
                WanConection(routers[1], routers[2], ip(10,2,2,0,30),0),   
                WanConection(routers[1], routers[3], ip(209,165,200,224,27),0),   
                ]


""" fc( dispositivo1, dispositivo 2, portDispositivo1(opcional), portDispositivo2(opcionale)) """""" connection order matters!! """
fastEthernetConection = [
                FastEthernetConection(hosts[0], switchs[0],0),
                FastEthernetConection(switchs[0], routers[0],0),
                
                ]


print(fastEthernetConection[1])
print(Routing.showConections([routers, switchs])) ; """  show all conection of the devices """
print(Routing.basicConfiguration(routers)) 
""" print(Routing.addressingRipV4(routers))  """
""" print(Routing.addressingOSPF(routers))  """
""" print(Routing.addressingRipv2OSPF(routers)) """
""" print(Routing.addresingStatic(routers,hosts)) """



""" -------------------------------------------- """
