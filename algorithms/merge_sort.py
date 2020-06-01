"""
    Merge sort
    - Time complexity O(nlog(n))
    - Space complexity O(n)
    - My implementation here based off CS2 with Dr. Beaty
    - professor at MSU Denver
"""


def merge_sort(to_sort):
    if not to_sort:
        return to_sort
    try:
        len(to_sort)
    except TypeError:
        return to_sort
    if len(to_sort) == 1:
        return to_sort

    return sort(to_sort)


def sort(to_sort):
    if len(to_sort) == 1:
        return to_sort
    middle = len(to_sort) // 2
    return merge(sort(to_sort[:middle]), sort(to_sort[middle:]))


def merge(one, two):
    if not one:
        return two
    if not one:
        return two

    first = list(one)
    second = list(two)

    result = []
    while first and second:
        if first[0] < second[0]:
            result.append(first.pop(0))
        else:
            result.append(second.pop(0))

    if not first:
        result.extend(second)
    if not second:
        result.extend(first)

    return result


if __name__ == '__main__':
    merge_sort([9, 4, 1, 7, 3, 0, 6, 8, 2, 5])
