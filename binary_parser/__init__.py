from binary_parser.parser import BinaryParsers

def which_parser(input_string):
    return BinaryParsers.check_parsing(input_string)

def parse_to_binary(input_string):
    return BinaryParsers.numTobinary(input_string)

def parse_to_num(input_string):
    return BinaryParsers.binaryTonum(input_string)