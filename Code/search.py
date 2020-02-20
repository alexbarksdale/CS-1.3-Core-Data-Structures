#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    return linear_search_recursive(array, item)

def linear_search_iterative(array, item) -> int:
    """
    Best case: O(1) if the the value is the first item in the array
    Worst case: O(N) if we need to search through the entire array
    """
    for index, value in enumerate(array):
        if item == value:
            return index  # found


def linear_search_recursive(array, item, index=0) -> None or int:
    """
    Best case: O(1) if the the value is the first item in the array
    Worst case: O(N) if we need to search through the entire array
    """

    if index > len(array) - 1:
        return None

    if item == array[index]:
        return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item) -> None or int:
    """
    Best case: O(1) if the the item is the middle in the array
    Worst case: O(log n) because you narrow the search by two operations every time
    """

    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2  # finds the middle item
        if item == array[mid]:
            return mid  # position of the item in the array
        elif item < array[mid]:
            # moves the high position if the item is less than the middle
            high = mid - 1
        else:
            # moves the low position if the item is greater than the middle
            low = mid + 1
    return None


def binary_search_recursive(array, item, low=None, high=None) -> None or int:
    """
    Best case: O(1) if the the item is the middle in the array
    Worst case: O(log n) because you narrow the search by two operations every time
    """
    # sets initial values
    if low is None and high is None:
        low, high = 0, len(array) - 1

    if low > high:
        return None

    mid = (low + high) // 2  # finds the middle item
    if item == array[mid]:
        return mid
    if item < array[mid]:
        # moves the high position if the item is less than the middle
        return binary_search_recursive(array, item, low, mid - 1)
    # moves the low position if the item is greater than the middle
    return binary_search_recursive(array, item, mid + 1, high)


def main():
    heroes = sorted(['Iron Man', 'Thor', 'Batman', 'Deadpool', 'Hawkeye'])
    print(heroes)
    # print(linear_search(heroes, 'Thor'))
    print(binary_search(heroes, 'Thor'))


if __name__ == '__main__':
    main()
