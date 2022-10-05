import imp
import string

from Library.devices.RmiSwitchDevice import SwitchDevice 
from Library.settingDevice.RmiVlan import Vlan as vlan

class SwitchRouting:
    
    @staticmethod
    def vlanConfiguration(switchs):
        text = "" 
   
        for switch in switchs:
            gigaethernet = switch.getVlanGigaethernet()
            text += "-------------"+switch.name+"------------------------- \n"
            text += "configure terminal\n"
            text += "interface range fastethernet0/1-24\n"
            text += "Shutdown \n"
            text += "interface range gigaethernet 0/1\n"
            text += "no shutdown\n"
            
            text += "enable\n"
            text += "configure terminal\n"
            text += "interface range fastethernet0/1-24\n"
            text += "switchport mode access\n"
            text += "no shutdown\n"
            text += "exit\n\n"
            
            for vlan in switch.vlans:
                text += "vlan "+str(vlan.number)+"\n"
                text += "name "+vlan.name+"\n"
            text += "exit\n"
            text += "exit\n\n"
            
            text += "show vlan brief\n"
            text += "configure terminal\n"
            for vlan in switch.vlans:
                if vlan.gigaethernet == False:
                    text += "interface range fastethernet0/"+str(vlan.fastethernetRangeIn)+"-"+str(vlan.fastethernetRangeFin)+"\n"
                    text += "switchport access vlan "+str(vlan.number)+"\n"
                    text += "no shutdown\n"
                    text += "exit\n"
            
            """ buscar si un este swich esta conectado a otro switch """
            for port in switch.portsConected():
                if type(port.actualDevice()) == SwitchDevice  and type(port.conectedDevice()) == SwitchDevice: 
                    text += "\ninterface vlan "+str(gigaethernet.number)+"\n"
                    text += "ip address "+str(port.ipActual())+" "+str(port.ipActual().getMaskIp())+"\n"
                    text += "no shutdown\n"
                    break

            
            text += "\nconfigure terminal\n"
            text += "interface range fastethernet0/"+str(gigaethernet.fastethernetRangeIn)+"-"+str(gigaethernet.fastethernetRangeFin)+"\n"
            text += "switchport mode trunk\n"
            text += "switchport trunk native vlan "+str(gigaethernet.number)+"\n"
            text += "no shutdown\n"
            text += "exit\n"
            
        return text
            
            
        
            
            
            
            
            
            

