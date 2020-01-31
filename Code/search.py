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
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item) -> None or int:
    # [1,2,3,4,5,6,7,8,9]
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


def binary_search_recursive(array, item, low=None, high=None) -> None or int:
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1

    if low > high:
        return None

    mid = (low + high) // 2
    if item == array[mid]:
        return mid
    if item < array[mid]:
        return binary_search_recursive(array, item, low, mid - 1)
    return binary_search_recursive(array, item, mid + 1, high)


def main():
    heroes = sorted(['Iron Man', 'Thor', 'Batman', 'Deadpool', 'Hawkeye'])
    print(heroes)
    # print(linear_search(heroes, 'Thor'))
    print(binary_search(heroes, 'Thor'))


if __name__ == '__main__':
    main()
