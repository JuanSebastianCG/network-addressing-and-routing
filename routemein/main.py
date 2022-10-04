
from Library.settingDevice.RmiVlan import Vlan

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
from Library.devices.RmiSwitchDevice import SwitchDevice as sd

""" conections """
from Library.conections.RmiFastEthernet import FastEthernet as fc
from Library.conections.RmiWanConection import WanConection as wc




""" ------------test Zone----------------- """


hosts = [30,550,2950,6] 
hosts =  sorted(hosts, reverse=True)

""" addressing(hosts, ip (opcional)) """
ipAd = adr.addressing(hosts,ip(198,168,0,0,29))
""" add one host to each ip """
ipAd = adr.addAHostToIps(ipAd)

"""  wanGenerator(wan numbers of wan directions, base ip (optional), 4(number of hosts per wan))"""
wan = rth.wanGenerator(2,ip(220,11,10,0,29))


""" print(adr.showAddressing(ipAd,hosts)) """
""" for i in wan:
    print(i) """

""" rd(name of the device, serial port ejem: [port("0/0"),port("0/2")], fasethernet port ejem:  [port("0/0"),port("0/2")]  ) """
routers = [rd("router0"),
           rd("router1"),
           rd("router2"),
        ]

""" hd (name, assigned ip(red), fasethernet port :  [port("0/0"),port("0/2")] (opcional))"""
hosts = [hd("host0", ip(193,33,20,0,25)) ,
         hd("host1 ", ip(193,33,20,128,27)) ,
         hd("host2 ", ip(193,33,20,160,28)) ,
           ]

""" wc( dispositivo 1, dispositivo 2 ,zona,assigned ip(red), portDispositivo1(opcional), portDispositivo2(opcional)) """""" connection order matters!! """
wanConection = [
                wc(routers[0], routers[1], wan[0],0),
                wc(routers[0], routers[2], wan[1],0),   
                ]


""" fc( dispositivo1, dispositivo 2, portDispositivo1(opcional), portDispositivo2(opcionale)) """""" connection order matters!! """
fastEthernetConection = [
                fc(hosts[0], routers[1],0),
                fc(hosts[1], routers[0],0),     
                fc(hosts[2], routers[2],0),          
                ]


""" print(rth.showConections([routers, hosts])) """ ; """  show all conection of the devices """
""" print(rth.basicConfiguration(routers))  """
""" print(rth.addressingRipV4(routers)) 
print(rth.addressingOSPF(routers))  """
""" print(rth.addresingStatic(routers,hosts)) """









""" -------------------------------------------- """




vlanIpHost = [30,550,2950,6] 
vlanIpHost =  sorted(vlanIpHost, reverse=True)

""" addressing(hosts, ip (opcional)) """
vlanIp= adr.addressing(vlanIpHost,ip(198,168,0,0,29))

print(adr.showAddressing(vlanIp,vlanIpHost))

vlans = [
    Vlan( vlanIp[0],"vlan1",10,10,12),
    Vlan( vlanIp[1],"vlan2",20,13,17),
    Vlan( vlanIp[2],"vlan3",30,18,20),     
    Vlan( vlanIp[3],"vlanAd",99,1,4, True),     
         ] 


""" rd(name of the device, serial port ejem: [port("0/0"),port("0/2")], fasethernet port ejem:  [port("0/0"),port("0/2")]  ) """
switch = [
          sd("switch0",vlans),
          sd("switch1",vlans),
          sd("switch2",vlans),
          ]

hostsGroup1 = [
         hd("host0") ,
         hd("host1") ,
         hd("host2") ,
           ]
hostsGroup2 = [
         hd("host3") ,
         hd("host4") ,
         hd("host5") ,
           ]
hostsGroup3 = [
         hd("host6") ,
         hd("host7") ,
         hd("host8") ,
           ]

conectionGroup1 = [
          fc(hostsGroup1[0], switch[0], 0, vlans[3]),
  
  
  
]
print(str(conectionGroup1[0]))









""" print(rth.showConections([routers, hosts])) """ ; """  show all conection of the devices """
""" print(rth.basicConfiguration(routers))  """
""" print(rth.addressingRipV4(routers)) 
print(rth.addressingOSPF(routers))  """
""" print(rth.addresingStatic(routers,hosts)) """





 
 