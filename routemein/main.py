from Library.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.RmiAddressingLib import addressingHandler as adr
from Library.RmiIPv4Lib import IPv4 as ip



""" print(bnh.int_to_bin(255))

print(bnh.sum('10000', '10000'))

for i in range(256):
    print(ip(i, i, i, i))

print(ip(254, 254, 254, 254).get_binary_string())
one = ip(254, 254, 254, 254)
one.set_ip_value_binary_str('11111100111111001111110011111100')
print(one) """


""" ----------pureba mascara, wildcard y subredes-------------- """

""" one = ip(192, 10, 253, 10,30)
one.oct3 = bnh.addEspecificOne(one.ipV4[3], 7)  
print (one)
print (one.getMaskIp())  
print (one.getWildcard())  
print (one.increaseSubclass(1)) """

 
""" ----------prueba direccionamiento--------------------------- """

hosts = [3,201,23] 
ipAd = adr.addressing(hosts, ip(200, 30, 4, 255 ))
print(adr.showAddressing(ipAd,hosts))


hosts = [48,1000,2100,10] 
ipAd = adr.addressing(hosts, ip(140, 27, 0, 0))
print(adr.showAddressing(ipAd,hosts))


hosts = [120,501,1200,16] 
ipAd = adr.addressing(hosts, ip(130, 10, 255, 0))
print(adr.showAddressing(ipAd,hosts))


 
 
 
 
 