"""
    Insert sort
    - Worst case time complexity of O(n^2)
    - Best case time complexity O(n) if presorted
    - Space complexity of O(1) for iterative and O(n) for recursive
"""


def insert_sort(to_sort):

    if not to_sort:
        return to_sort
    try:
        length = len(to_sort)
    except TypeError:
        return to_sort
    if len(to_sort) == 1:
        return to_sort

    for index in range(length):

        inserting = to_sort[index]
        inner_index = index - 1

        while inner_index >= 0 and inserting < to_sort[inner_index]:
            to_sort[inner_index + 1] = to_sort[inner_index]
            inner_index -= 1
            to_sort[inner_index + 1] = inserting

    return to_sort
