"""
    Bubble sort iterative
    - Time complexity of O(n^2)
    - Best case time complexity O(n) if presorted
    - Space complexity of O(1)

"""


def bubble_sort(to_sort):

    if not to_sort:
        return to_sort
    try:
        len(to_sort)
    except TypeError:
        return to_sort
    if len(to_sort) == 1:
        return to_sort

    for outer in range(len(to_sort) - 1):
        pre_sorted = True
        for inner in range(len(to_sort) - 1 - outer):
            if to_sort[inner] > to_sort[inner + 1]:

                to_sort[inner], to_sort[inner + 1] = \
                    to_sort[inner + 1], to_sort[inner]
                pre_sorted = False

        if pre_sorted:
            break

    return to_sort
