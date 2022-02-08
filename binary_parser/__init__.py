from binary_parser.parser import BinaryParsers

def which_parser(input_string=None):
    if input_string is None: raise ValueError("Input must contain some integer or some string") 
    return BinaryParsers.check_parsing(input_string)

def parse_to_binary(input_string=None):
    if input_string is None: raise ValueError("Input must contain some integer")
    return BinaryParsers.numTobinary(input_string)

def parse_to_num(input_string=None):
    if input_string is None: raise ValueError("Input must contain binary string")
    return BinaryParsers.binaryTonum(input_string)