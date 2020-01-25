#!python

import string
from utils import time_it
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def digit_to_number(d=str) -> int:
    '''Based off Sahil Shelangia implementation'''
    if d >= 'A' and d <= 'F':
        # Unicode: 65 = 'A' + 10 because A = '10' in Hex
        #   - If 'B' was passed in 66 - 65 = 1 + 10 = 11
        return ord(d) - 65 + 10
    return int(d)


@time_it
def decode(digits=str, base=int) -> int:
    '''Decode given digits in given base to number in base 10'''
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    conv_digits = 0
    for i, value in enumerate(digits[::-1]):
        conv_digits = conv_digits + digit_to_number(value) * (base ** i)
    return conv_digits

    # schema = list(digits)[::-1]
    # print(f'Schema = {schema}')

    # if base == 2:
    #     # for i, value in enumerate(digits[::-1]):
    #     #     if value == '1':
    #     #         conv_digits = conv_digits + int(value) * (base ** i)

    #     # return conv_digits

    #     # ! Test the difference
    #     for i in range(len(schema)):
    #         if schema[i] == '1':
    #             conv_digits = conv_digits + int(schema[i]) * (base ** i)
    #     return conv_digits


def encode(number=int, base=int) -> str:
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 3:
        digits = args[0].capitalize()
        base1 = int(args[1])
        base2 = int(args[2])

        decode_result = decode(digits, base1)
        print(f'Decoded {digits} from base {base1} to: {decode_result}')

        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, +
                                                      base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
