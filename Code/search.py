#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item) -> int:
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found


def linear_search_recursive(array, item, index=0) -> None or int:
    if index > len(array) - 1:
        return None

    if item == array[index]:
        return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    return binary_search_iterative(array, item)


def binary_search_iterative(array, item) -> None or int:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if item == array[mid]:
            return mid  # position of the item in the array
        elif item < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


def main():
    heroes = sorted(['Iron Man', 'Thor', 'Batman', 'Deadpool', 'Hawkeye'])
    print(heroes)
    # print(linear_search(heroes, 'Thor'))
    print(binary_search(heroes, 'Thor'))


if __name__ == '__main__':
    main()
