#!pythonk
import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text=str):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def clean_text(text=str) -> str:
    return ''.join(filter(str.isalnum, text.lower()))


def is_palindrome_iterative(text=str) -> bool:
    # text = text.lower()
    text = clean_text(text)
    low, high = 0, len(text) - 1

    # while low < high:
    #     while not text[low].isalnum():
    #         low += 1
    #     while not text[high].isalnum():
    #         high -= 1
    #     if text[low] != text[high]:
    #         return False
    #     low += 1
    #     high -= 1
    # return True
    while low < high:
        # if not text[high].isalnum():
        #     high -= 1
        #     continue
        # if not text[low].isalnum():
        #     low += 1
        #     continue
        if text[low] != text[high]:
            return False
        high -= 1
        low += 1
    return True


def is_palindrome_recursive(text=str, low=None, high=None):
    text = clean_text(text)
    if low is None and high is None:
        low, high = 0, len(text) - 1
    if low > high:
        return True
    # if not text[high].isalnum():
    #     return is_palindrome_recursive(text, low, high - 1)
    # if not text[low].isalnum():
    #     return is_palindrome_recursive(text, low + 1, high)
    if text[low] != text[high]:
        return False
    return is_palindrome_recursive(text, low + 1, high - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
