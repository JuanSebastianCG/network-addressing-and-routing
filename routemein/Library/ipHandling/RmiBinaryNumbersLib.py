import imp
import string

class binaryNumbersHandler:
    
    zeros='00000000'
    ones='11111111'
    zerosIp ='00000000000000000000000000000000'


    """Adds two numbers in binary."""
    @staticmethod
    def sum(num1: str, num2: str) -> str:
        return binaryNumbersHandler.int_to_bin_Ip(int(num1,2)+int(num2,2))
    
    """ convert a number to an octet of binary """
    @staticmethod
    def int_to_bin(num: int) -> string:
        res = bin(num)[2:]
        if len(res) < 8:
            res=binaryNumbersHandler.zeros[0:8-len(res)]+res
        return res
    
    """ convert a full number to an ip """
    @staticmethod
    def int_to_bin_Ip(num: int) -> string:
        res = bin(num)[2:]
        if len(res) < 32:
            res=binaryNumbersHandler.zerosIp[0:32-len(res)]+res
        return res
    
    """convert a binary number to an integer"""
    @staticmethod
    def bin_to_int(bin: string) -> int:
        return int(bin, 2)
    
    

