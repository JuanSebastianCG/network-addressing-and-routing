
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

""" add one host to each ip """
ipAd = Addressing.addAHostToIps(ipAd)

"""  wanGenerator(wan numbers of wan directions, base ip (optional), 4(number of hosts per wan))"""
wan = Addressing.wanGenerator(2,ip(220,11,10,0,29))

""" print(adr.showAddressing(ipAd,hosts)) """
""" for i in wan: print(i) """


easyIp = [
    dhcpEasyIp("r1",ip(130,10,2,0,25),
               [[ip(130,10,2,1,25),5]],
               ip(130,10,2,222,30)),
    
    dhcpEasyIp("r2",ip(130,10,2,128,26 ),
               [[ip(130,10,2,128,26),6]] ,
               ip(130,10,2,222,30)),
    
    dhcpEasyIp("r3", ip(130,10,0,0,23 ),
               [[ip(130,10,0,0,23),6]] ,
               ip(130,10,2,222,30)),

]


""" rd(name of the device, setting [dhcpEasyIp,setting2](opcional) ,serial port ejem: [port("0/0"),port("0/2")](opcional), fasethernet port ejem:  [port("0/0"),port("0/2")](opcional)  ) """
routers = [
           RouterD("router0",[easyIp[0],easyIp[1]]),
           RouterD("router1",),
           RouterD("router2",[easyIp[2]]),
           RouterD("ISP"),
        ]

""" hd (name, assigned ip, fasethernet port :  [port("0/0"),port("0/2")] (opcional))"""
hosts = [HostD("pc0",  ip(130,10,2,7,25),easyIp[0].gateWay) ,
         HostD("pc1 ",  ip(130,10,2,135,26),easyIp[1].gateWay) ,
         HostD("pc3", ip(130,10,0,7,23),easyIp[2].gateWay) ,
         HostD("server0",ip(130,10,2,222,27),ip(130,10,2,193,27)) ,
         HostD("server1", ip(210,22,66,85,24),ip(210,22,66,1,24)) ,
           ]

""" wc( dispositivo 1, dispositivo 2 ,assigned ip(red), Area , portDispositivo1(opcional), portDispositivo2(opcional)) """""" connection oRouterDer matters!! """
wanConection = [
                WanConection(routers[0], routers[1], ip(15,15,15,0,30),0),
                WanConection(routers[1], routers[2],  ip(15,15,15,4,30),0),   
                WanConection(routers[1], routers[3] , ip(198,120,33,12,30),0),   
                ]


""" fc( dispositivo1, dispositivo 2, Area ,portDispositivo1(opcional), portDispositivo2(opcionale)) """""" connection order matters!! """
fastEthernetConection = [                
                FastEthernetConection(hosts[3], routers[1],0),
                FastEthernetConection(hosts[4], routers[3],0),
                
                FastEthernetConection(hosts[0], routers[0],0),
                FastEthernetConection(hosts[1], routers[0],0),
                FastEthernetConection(hosts[2], routers[2],0),
                
                ]

""" print(Routing.showConections([routers])) """ ; """  show all conection of the devices """
print(Routing.showHosts(hosts))
print(Routing.basicConfiguration(routers)) 
""" print(Routing.addressingRipV4(routers))  """
""" print(Routing.addressingOSPF(routers))  """
""" print(Routing.addressingRipv2OSPF(routers)) """
""" print(Routing.addresingStatic(routers,hosts)) """

""" -------------------show running-config ------------------------- """
