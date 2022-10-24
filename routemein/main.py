
from unicodedata import name


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
""" hosts = [30,550,2950] 
hosts =  sorted(hosts, reverse=True)
 """
""" addressing(hosts, ip (opcional)) """
""" ipAd = Addressing.addressing(hosts,ip(192,168,10,0,0))
ipAd = Addressing.addressing(hosts) """

""" add one host to each ip """
""" ipAd = Addressing.addAHostToIps(ipAd) """

"""  wanGenerator(wan numbers of wan directions, base ip (optional), 4(number of hosts per wan))"""
""" wan = Addressing.wanGenerator(2,ip(220,11,10,0,29)) """

""" print(adr.showAddressing(ipAd,hosts)) """
""" for i in wan: print(i) """


"""dhcpEasyIp(name: String, initialIp: ip, [[exclusiveip,fromIpHowMani]], dns: Ip, gateWay)  """
easyIp = [
    dhcpEasyIp("R1Fa0",
               ip(192,168,10,0,24),
               [[ip( 192,168,10,1,24),9]],
               ip(192,168,20,254,30),
               ip(192,168,10,1,24))
    ,
    dhcpEasyIp("R1Fa1",
               ip(192,168,11,0,24),
               [[ip( 192,168,11,1,25),9]],
               ip(192,168,20,254,30),
               ip(192,168,11,1,24)),
]

serverGatewayIp = ip(192,168,20,254,24) 
""" Nat(Name, [publicIp,publicIp,publicIp], maskPublicIp, [[staticIpinternal, staticIpExternal],.. ], ...) """
nat =  Nat("MY-NAT-POOL", 
           [ip(209,165,200,241), ip(209,165,200,246)],ip(255,255,255,248),
           [[serverGatewayIp,ip(209,165,200,254)] ]
           )


""" rd(name of the device, setting [dhcpEasyIp,setting2](opcional) ,serial port ejem: [port("0/0"),port("0/2")](opcional), fasethernet port ejem:  [port("0/0"),port("0/2")](opcional)  ) """
routers = [
           RouterD("router0",[dhcpHelper(ip(10,1,1,2,24))]),
           RouterD("router1",[easyIp[0], easyIp[1], nat]),
           RouterD("ISP"),
        ]

""" hd (name, assigned ip, gateWay : ip(opcional), fasethernet port :  [port("0/0"),port("0/2")] (opcional))"""
hosts = [HostD("pc0",  easyIp[0].getNextIp(),easyIp[0].gateWay) ,
         HostD("pc1",  easyIp[1].getNextIp(),easyIp[1].gateWay) ,
         HostD("server0",ip(192,168,20,1,24),serverGatewayIp) 
          ]



""" switch (name, vlans: vlan, assigned ip, gateWay : ip(opcional), fasethernet port :  [port("0/0"),port("0/2")] (opcional))"""
switch = [
    SwitchD("switch0",None,easyIp[0].gateWay),
    SwitchD("switch1",None,easyIp[1].gateWay),
]



""" wc( disConected1, disConected2 ,assigned ip(red), Area , portDispositivo1(opcional), portDispositivo2(opcional)) """""" connection oRouterDer matters!! """
wanConection = [
                WanConection(routers[1], routers[0], ip(10,1,1,0,30),0),
                WanConection(routers[2], routers[1], ip(209,165,200,224,30),0),      
                ]


""" fc( disConected1, disConected2, Area ,portDispositivo1(opcional), portDispositivo2(opcionale)) """""" connection order matters!! """
fastEthernetConection = [                
                FastEthernetConection(hosts[2], routers[1],0),
                
                FastEthernetConection(routers[0], switch[0],0),
                FastEthernetConection(routers[0], switch[1],0),
                
                FastEthernetConection(switch[0], hosts[0],0),
                FastEthernetConection(switch[1], hosts[1],0),
                
                ]


""" print(Routing.showConections([routers])) """ ; """  show all conection of the devices """
""" print(Routing.showHosts(hosts)) """
print(Routing.basicConfiguration(routers)) 
""" print(Routing.addressingRipV4(routers))  """
""" print(Routing.addressingOSPF(routers))  """
""" print(Routing.addressingRipv2OSPF(routers)) """
""" print(Routing.addresingStatic(routers,hosts)) """

""" -------------------show running-config ------------------------- """
