import re
import unicodedata

class BinaryParsers:
    def binaryTonum(input_string):
        """ Convert a binary string to a number """

        if not input_string:
            raise ValueError("Input must contain binary string")
        for char in input_string:
            if char!='0' and char!='1':
                raise ValueError(f"your string {input_string} must contain only 0's and 1's")
        val = 0
        ans = 0
        for i in range(len(input_string)-1,-1,-1):
            ans += int(input_string[i])*(2**val)
            val += 1
        return ans

    def numTobinary(input_string):
        """ Convert a number to its binary string """
        
        try:
            input_num = int(input_string)
        except:
            raise ValueError("input string must of type int")
        # isnumeric() is more recommended but the input here can be string or integer.
        if input_num==0: return '0'
        ans = ''
        while input_num:
            if input_num%2:
                ans += '1'
            else:
                ans += '0'
            input_num = input_num//2
        return ans[::-1]
    
    def check_parsing(self, input_string):
        """ Check which conversion to apply for the given input string """
        pass 
