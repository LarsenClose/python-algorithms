"""
    Quick sort with randomized pivot
    - Time complexity O(nlog(n)) for any input size n
    - no worst case input

"""

import random


def quick_sort(to_sort):
    if not to_sort:
        return to_sort
    try:
        len(to_sort)
    except TypeError:
        return to_sort
    if len(to_sort) == 1:
        return to_sort

    return _quick_sort(to_sort, 0, len(to_sort) - 1)


def _quick_sort(to_sort, low, high):
    if low < high:
        pivot = randomize_pivot(to_sort, low, high)
        _quick_sort(to_sort, low, pivot)
        _quick_sort(to_sort, pivot + 1, high)


def randomize_pivot(to_sort, start, stop):
    pivot = random.randrange(start, stop)
    to_sort[start], to_sort[pivot] = to_sort[pivot], to_sort[start]

    return partition(to_sort, start, stop)


def partition(to_sort, low, high):
    """partition utilizing Hoare's scheme"""

    pivot = to_sort[low]
    i, j = low, high

    while True:
        # Swap elements lower than pivot with elements great than pivot
        while to_sort[i] < pivot:
            i += 1
        while to_sort[j] > pivot:
            j -= 1

        # Once high and low swap points meet we have the index j
        # everything above j is higher, everything below j is lower
        if i >= j:
            return j

        to_sort[i], to_sort[j] = to_sort[j], to_sort[i]


if __name__ == '__main__':
    my_list = [9, 4, 1, 7, 3, 0, 6, 8, 2, 5]
    quick_sort(my_list)
    print(my_list)
