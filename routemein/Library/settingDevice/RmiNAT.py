


import string



from Library.ipHandling.RmiIPv4Lib import IPv4 as ip

class NAT():

    def __init__(self, name: string  ,publicIps, publicMask: ip ,staticIps = None, outSideNat = None ):
        self.name = name
        self.mainDevice = None
        self.publicIps = publicIps
        self.publicMask = publicMask
        
        if staticIps == None:
            self.staticIps = []
        else:
            self.staticIps = staticIps
            
        if outSideNat == None:
            self.outSideNat = []
        else:
            self.outSideNat = outSideNat
    
        
             
    """ take the initial device and go through the posts assigning them the output they have in front of the nat """
    def getNatOutsideInside(self):
        text = ""
        fastethernetPort  = self.mainDevice.fastEthernetPortsConected()
        serialPort  = self.mainDevice.serialsPortsConected()

        for port in fastethernetPort:
            text += "interface fa"+str(port.name)+"\n"
            text += "ip nat inside\n"
            text += "exit\n"
            
        for port in serialPort:
            deviceConected = port.conectedDevice()
            if self.outSideNat == []:
                if deviceConected.name == "ISP":
                    text += "interface serial "+str(port.name)+"\n"
                    text += "ip nat outside\n"
                    text += "exit\n"
                    continue
            elif port.ipConected  ==  self.outSideNat:
                text += "interface serial "+str(port.name)+"\n"
                text += "ip nat outside\n"
                text += "exit\n"  
                continue

            text += "interface serial "+str(port.name)+"\n"
            text += "ip nat inside\n"
            text += "exit\n"
                      
        return text 
            
                
             
        
    def __str__(self) -> string:
        text = "---------NAT configuration: "+self.name +"---------\n" 
        text += "Main Device: " + str(self.mainDevice.name) + "\n"
        text += "public mask: " + str(self.publicMask) + "\n"
        text += "Public Ips:\n"
        for publicIp in self.publicIps:
            text += "   " + str(publicIp) + "\n"
        text += "\n"
        
        text += "Static Ips:\n"
        for staticIp in self.staticIps:
            text += "ip:" + str(staticIp[0]) +" -public- "+str(staticIp[1])+ "\n"
        text += "\n"
        
        text += "OutSideNat:" + str(self.outSideNat) + "\n"
        
        return text
    
