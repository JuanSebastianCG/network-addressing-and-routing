import imp
import string

class binaryNumbersHandler:
    
    zeros='00000000'
    zerosIp ='00000000000000000000000000000000'


    """Adds two numbers in binary."""
    @staticmethod
    def sum(num1: str, num2: str) -> str:
        return binaryNumbersHandler.int_to_bin(int(num1,2)+int(num2,2))
    
    
    @staticmethod
    def int_to_bin(num: int) -> string:
        res = bin(num)[2:]
        if len(res) < 8:
            res=binaryNumbersHandler.zeros[0:8-len(res)]+res
        return res
    
    @staticmethod
    def bin_to_int(bin: string) -> int:
        return int(bin, 2)
    
    

