"""
Problem: Write a function that returns the "pivot" index of a list of integers.
We define the pivot index as the index where the sum of the numbers on the left
is equal to the sum of the numbers on the right. Given [1, 4, 6, 3, 2], the
function should return 2, since the sum of the numbers to the left of index 2
is equal to the sum of numbers to the right of index 2 (1 + 4 = 3 + 2). If no
such index exists, it should return -1. If there are multiple pivots, you can
return the left-most pivot.
"""

def pivot(array):
    try:
        array[2]
    except IndexError:
        return -1
    total_sum = sum(array)
    rhs = total_sum - array[0] - array[1]
    lhs = array[0]
    limit = total_sum / 2
    index = 1
    if rhs == lhs:
        return index
    while lhs < limit and lhs != rhs:
        lhs += array[index]
        rhs -= array[index + 1]
        if rhs == lhs:
            return index + 1
        index += 1
    return -1
