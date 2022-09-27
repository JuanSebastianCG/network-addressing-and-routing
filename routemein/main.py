
from Library.RmiAddressingLib import addressingHandler as adr
from Library.RmiRoutingLib import routingHandler as rth


from Library.ipHandling.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip


from Library.devices.RmiHostDevice import HostDevice as hd
from Library.devices.RmiRouterDevice import RouterDevice as rd

from Library.conections.RmiFastEthernet import FastEthernet as fc
from Library.conections.RmiWanConection import WanConection as wc




""" ------------pureba disporitivos----------------- """

hosts = [122,13,312] 
hosts =  sorted(hosts, reverse=True)

ipAd = adr.addressing(hosts, ip(129, 10, 0, 0 ))

""" for i in range(len(ipAd)):
    print(ipAd[i].getAllData())
print(adr.showAddressing(ipAd,hosts))
 """

routers = [rd("r0"),
           rd("r1"),
           rd("r2")]

hosts = [hd("host0",hosts[0], ipAd[0]) ,
         hd("host1 ",hosts[1], ipAd[1]) ,
         hd("host2",hosts[2], ipAd[2])  ]

wanConection = [
                wc(routers[0], routers[1], ip(200, 10, 4, 0,29)),
                wc(routers[1], routers[2], ip(200, 10, 4, 8,29)),
                wc(routers[2], routers[0], ip(200, 10, 4, 16,29)),    
                ]

fastEthernetConection = [
                fc(hosts[0], routers[0]),
                fc(hosts[1], routers[1]),     
                fc(hosts[2], routers[2]),     
                ]

print(rth.basicConfiguration(routers)) 


""" print(rth.addressingRipV4(routers))  """
""" print(rth.addressingOSPF(routers))  """
""" print(rth.addresingStatic(routers,hosts)) """





""" ----------pureba mascara, wildcard y subredes-------------- """

""" one = ip(192, 10, 253, 10,30)
one.oct3 = bnh.addEspecificOne(one.ipV4[3], 7)  
print (one)
print (one.getMaskIp())  
print (one.getWildcard())  
print (one.increaseSubclass(1)) """

 
""" ----------prueba direccionamiento--------------------------- """

""" hosts = [3,201,23] 
ipAd = adr.addressing(hosts, ip(200, 30, 4, 255 ))
print(adr.showAddressing(ipAd,hosts))


hosts = [48,1000,2100,10] 
ipAd = adr.addressing(hosts, ip(140, 27, 0, 0))
print(adr.showAddressing(ipAd,hosts))


hosts = [120,501,1200,16] 
ipAd = adr.addressing(hosts, ip(130, 10, 255, 0))
print(adr.showAddressing(ipAd,hosts))
 """

 
 
 
 
 