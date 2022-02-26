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
        
        if not input_string:
            raise ValueError("Input must contain some integer")
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
        return ans[::-1].encode('utf-8')
    
    def check_parsing(input_string):
        """ Check which conversion to apply for the given input string """

        # binary check
        bin, num = 1, 1
        if not input_string:
            raise ValueError("Input must contain some integer or some string")

        try:
            print(isinstance(input_string, bytes))
            if isinstance(input_string, bytes):
                input_string_enc = input_string.decode()
            print(input_string)
            for char in input_string_enc:
                if char!='0' and char!='1':
                    bin = 0
                    break
        except:
            bin = 0
        
        # integer check
        try:
            if isinstance(input_string, bytes):
                num = 0
            else:
                input_num = int(input_string)
        except:
            num = 0

        if bin == 1 and num==1:
            print(f"Input {input_string} could be either binary or a number")
            return f"binary string: {input_string} number: {input_num}"
        elif bin==1:
            print(f"Input {input_string} is a binary string")
            return f"binary string: {input_string}"
        elif num==1:
            print(f"Input {input_string} is a number")
            return f"number: {input_num}"
        else:
            return f"Input is neither binary nor a number"