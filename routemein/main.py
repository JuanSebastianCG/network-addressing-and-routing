
from unicodedata import name
from webbrowser import get


""" addresing and routing """
from Library.RmiAddressingLib import addressingHandler as Addressing
from Library.RmiRoutingLib import routingHandler as Routing
from Library.RmiSwitchRoutingLib import SwitchRouting as swr

""" ip management """
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

""" settings """
from Library.settingDevice.RmiPortManage  import Port as Port
from Library.settingDevice.RmiDHCP  import DhcpEasyIP  as dhcpEasyIp 
from Library.settingDevice.RmiDHCP  import helperDhcp  as dhcpHelper
from Library.settingDevice.RmiNAT  import NAT as Nat

from Library.settingDevice.RmiVlan import Vlan

""" devices """
from Library.devices.RmiHostDevice import HostDevice as HostD
from Library.devices.RmiRouterDevice import RouterDevice as RouterD
from Library.devices.RmiSwitchDevice import SwitchDevice as SwitchD

""" conections """
from Library.conections.RmiFastEthernet import FastEthernet as FastEthernetConection
from Library.conections.RmiWanConection import WanConection as WanConection




""" ------------test Zone----------------- """



"""dhcpEasyIp(name: String, initialIp: ip, [[exclusiveip,fromIpHowMani]], dns: Ip, gateWay)  """
easyIp = [
    dhcpEasyIp("R1Fa0",
               ip(150,30,4,0,25),
               [[ip( 150,30,4,1,25),9]],
               ip(150,30,0,15,30),
               ip(150,30,4,1,25))
    ,
    dhcpEasyIp("R1Fa1",
               ip(150,30,4,128,27),
               [[ip(150,30,4,129,27),9]],
               ip(150,30,0,15,30),
               ip(150,30,4,129,27)),
]

host1 = [easyIp[0].getNextIp(),easyIp[0].gateWay]
host2 = [easyIp[1].getNextIp(),easyIp[1].gateWay]
server1 = [ip(150,30,0,2,22), ip(150,30,0,15,22)]
server2 = [ip(192,168,10,2,24),ip(192,168,10,1,24)]


ipStaticas = [ip(210,20,0,190)]
ipPublicas = [ip(210,20,0,161), ip(210,20,0,172)]


""" Nat(Name, [publicIp,publicIp,publicIp], maskPublicIp, ip afected by the dinamic Nat ,[[staticIpinternal, staticIpExternal],.. ], ...) """
nat =  Nat("MY-NAT-POOL", 
           ipPublicas,ip.getIpMaskFromMask(28),
           [easyIp[0].initialIp, easyIp[1].initialIp],
           [[server1[0],ipStaticas[0]] ]
           )

""" rd(name of the device, setting [dhcpEasyIp,setting2](opcional) ,serial port ejem: [port("0/0"),port("0/2")](opcional), fasethernet port ejem:  [port("0/0"),port("0/2")](opcional)  ) """
routers = [
           RouterD("router0",[easyIp[0], easyIp[1]]),
           RouterD("router1",[nat]),
           RouterD("router2"),
           RouterD("ISP"),
        ]

""" hd (name, assigned ip, gateWay : ip(opcional), fasethernet port :  [port("0/0"),port("0/2")] (opcional))"""
hosts = [HostD("pc0",  host1[0],host1[1]),
         HostD("pc1", host2[0], host2[1]),
         HostD("brasil",server1[0],server1[1]) ,
         HostD("server1",server2[1],server2[1]) 
          ]



""" switch (name, vlans: vlan, assigned ip, gateWay : ip(opcional), fasethernet port :  [port("0/0"),port("0/2")] (opcional))"""






""" wc( disConected1, disConected2 ,assigned ip(red), Area , portDispositivo1(opcional), portDispositivo2(opcional)) """""" connection oRouterDer matters!! """
wanConection = [
                WanConection(routers[0], routers[1], ip(100,10,0,8,29),0),
                WanConection(routers[1], routers[2], ip(100,10,0,0,29),0),      
                WanConection(routers[1], routers[3], ip(200,100,30,0,30),0),      
                ]


""" fc( disConected1, disConected2, Area ,portDispositivo1(opcional), portDispositivo2(opcionale)) """""" connection order matters!! """
fastEthernetConection = [                
                FastEthernetConection(hosts[0], routers[0],0),
                FastEthernetConection(hosts[1], routers[0],0),
                
                FastEthernetConection(hosts[2], routers[2],0),
                FastEthernetConection(hosts[3], routers[3],0),
                

                
                ]


""" print(Routing.showConections([routers])) """ ; """  show all conection of the devices """
print(Routing.showHosts(hosts))
print(Routing.basicConfiguration(routers)) 
""" print(Routing.addressingRipV4(routers))  """
print(Routing.addressingOSPF(routers)) 
""" print(Routing.addressingRipv2OSPF(routers)) """
""" print(Routing.addresingStatic(routers,hosts)) """

""" -------------------show running-config ------------------------- """
