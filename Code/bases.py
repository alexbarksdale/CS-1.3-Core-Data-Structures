#!python

import string
# string.digits is '0123456789'
# string.hexdigits is ''0123456789abcdefABCDEF''
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def digit_to_char(remainder=int) -> str:
    '''Converts a digit to a character value.'''
    return string.printable[remainder]


def decode(digits=str, base=int) -> int:
    '''Decode given digits in given base to number in base 10.'''
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    decoded_digits = 0
    for i, value in enumerate(digits[::-1]):
        decoded_digits = decoded_digits + int(value, base) * (base**i)
    return decoded_digits


def encode(number=int, base=int) -> str:
    '''Encode given number in base 10 to digits in given base.'''
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    encoded_numbers = ''
    while number > 0:
        remainder = number % base
        number = number // base
        encoded_numbers += digit_to_char(remainder)

    return encoded_numbers[::-1]


def convert(digits=str, base1=int, base2=int) -> str:
    '''Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)'''
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(decode(digits, base1), base2)


def main():
    '''Read command-line arguments and convert given digits between bases.'''
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])

        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, +
                                                      base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
