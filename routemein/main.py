
from Library.RmiAddressingLib import addressingHandler as adr
from Library.ipHandling.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.ipHandling.RmiIPv4Lib import IPv4 as ip


from Library.devices.RmiHostDevice import HostDevice as hd
from Library.devices.RmiRouterDevice import RouterDevice as rd

from Library.conections.RmiFastEthernet import FastEthernet as fc
from Library.conections.RmiWanConection import WanConection as wc


""" ------------pureba disporitivos----------------- """

hosts = [4500,831,428,17] 
hosts =  sorted(hosts, reverse=True)

ipAd = adr.addressing(hosts, ip(128, 10, 0, 0 ))


print(ipAd[0].getAllData())
print(ipAd[1].getAllData())
print(ipAd[2].getAllData())
print(ipAd[3].getAllData())


""" router = rd("router1")
router1 = rd("router2")

host1 = hd("host1",hosts[0], ipAd[0]) 
host2 = hd("host2",hosts[1], ipAd[1]) 

wan1 = wc(router, router1, ip(200, 30, 4, 0))

fast = fc(host1, router1)


print(router)
print(router1)
 """

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

 
 
 
 
 