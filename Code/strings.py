#!python


def contains(text=str, pattern=str) -> bool:
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # for i in range(len(text) - len(pattern) + 1):
    #     if not pattern:
    #         return True
    #     if text[i] == pattern[0]:
    #         if text[i:(i + len(pattern))] == pattern:
    #             return True
    # return False

    return True if find_all_indexes(text, pattern) else False


def find_index(text=str, pattern=str) -> None or int:
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Pattern: KLMNOPZ
    # ABCDEFGHIJKLMNOPQRSTUVWX
    # ABCDEFGHIJKLMNOPQR      STUVWX
    # \\ Utilizes string slicing //
    # for i in range(len(text) - len(pattern) + 1):
    #     if not pattern:
    #         return i
    #     if text[i] == pattern[0]:
    #         if text[i:(i + len(pattern))] == pattern:
    #             return i
    # return None

    # i = 0
    # j = 0
    # if text[0] = pattern[0]
    # if e is c
    # print(text[i], text[i+j], pattern[j])

    # \\ Does not utilize string slicing //
    # for i in range(len(text) - (len(pattern) - 1)):
    #     match = True
    #     if not pattern:
    #         return None
    #     for j in range(len(pattern)):
    #         if text[i+j] != pattern[j]:
    #             match = False
    #             break
    #     if match:
    #         return i

    first_index = find_all_indexes(text, pattern)
    return first_index[0] if first_index else None


def find_all_indexes(text=str, pattern=str) -> list:
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if not pattern:
        return [i for i in range(len(text))]

    index_pos = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:(i + len(pattern))] == pattern:
            index_pos.append(i)
            continue
    return index_pos


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
