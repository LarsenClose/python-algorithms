"""
    Bubble sort recursive
    - Time complexity of O(n^2)
    - Space complexity of O(n) (due to call the call stack)
    - No presorted exit

"""


def bubble_sort(to_sort):

    if not to_sort:
        return to_sort

    try:
        index = len(to_sort)
    except TypeError:
        return to_sort
    return _bubble_sort(to_sort, index)


def _bubble_sort(to_sort, index):

    if index == 1:
        return to_sort

    for item in range(0, index - 1):
        if to_sort[item] > to_sort[item + 1]:

            to_sort[item], to_sort[item + 1] = \
                to_sort[item + 1], to_sort[item]

    return _bubble_sort(to_sort, index - 1)


if __name__ == '__main__':
    my_list = [9, 4, 1, 7, 3, 0, 6, 8, 2, 5]

    print(bubble_sort(my_list))
