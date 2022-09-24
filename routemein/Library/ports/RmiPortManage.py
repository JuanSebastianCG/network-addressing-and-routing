
import imp
import string

class Port:
    def __init__(self, name: string, isFree: bool = True):
        self.name = name
        self.isFree = isFree
    def __str__(self) -> string:
        text = "    Port Name: " + self.name +"  "+ str(self.isFree)+"\n"

        return  text