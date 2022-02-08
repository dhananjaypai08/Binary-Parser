![Python] (https://img.shields.io/pypi/pyversions/price-parser.svg)
### A python module where a number can be converted to it's binary bits and binary bits to number. ###
** Note: binary bits which will be recieved and provided will be in string format for early releases. **
`binary_parser` is a simple python library where users can convert an integer to its bit string and vice versa.

### Installation
`pip install binary_parser`
binary_parser requires python 3.9

### Usage
The library provides the following common use cases.

#### Converting a binary string to an integer
```
>>> import binary_parser
>>> binary_parser.parse_to_num('1011')
'11'
>>> binary_parser.parse_to_num('000')
'0'
>>> binary_parser.parse_to_num('01')
'1'
```

#### Converting an integer to its binary format
Arguments passed can be a string or an integer type.
```
>>> import binary_parser
>>> binary_parser.parse_to_binary('7')
'111'
>>> binary_parser.parse_to_binary(1)
'1'
>>> binary_parser.parse_to_binary('0')
'0'
```

#### Checking if given string is binary or integer
```
>>> import binary_parser
>>> binary_parser.which_parser('1010')
'Input 1010 could be either binary or a number'
'binary string: 1010 number: 10'
>>> binary_parser.which_parser(12)
'Input 12 is a number'
'number: 12'
>>> binary_parser.which_parser('00101')
'Input 00101 could be either binary or a number'
'binary string: 00101 number: 101'
```

