import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(log n)                           !
# ---------------------------------------------------------------------
def solution(nums: List[int], t: int) -> List[int]:
    """Given an array of integers nums sorted in non-decreasing order,
    find the starting and ending position of a given target value.

    Examples:
        >>> solution([], 0)
        [-1, -1]
        >>> solution([2, 2], 2)
        [0, 1]
        >>> solution([1, 2], 2)
        [1, 1]
        >>> solution([1, 2, 2], 2)
        [1, 2]
        >>> solution([2, 2, 3], 2)
        [0, 1]
        >>> solution([3, 3, 4], 4)
        [2, 2]
        >>> solution([5, 7, 7, 8, 8, 10], 6)
        [-1, -1]
        >>> solution([5, 7, 7, 8, 8, 10], 8)
        [3, 4]
    """
    n = len(nums)

    def findFirstOrLastPosition(l: int, r: int, isFirst: bool) -> int:
        while l <= r:
            m = (l + r) // 2
            if nums[m] == t:
                if isFirst:
                    if m == 0 or nums[m - 1] != t:
                        return m
                    r = m - 1
                else:
                    if m == n - 1 or nums[m + 1] != t:
                        return m
                    l = m + 1
            elif nums[m] < t:
                l = m + 1
            else:
                r = m - 1

    if n == 2 and nums[0] == nums[-1] == t:
        return [0, 1]
    res = [-1, -1]
    i, j = 0, n - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] == t:
            res[0] = findFirstOrLastPosition(0, mid, True)
            res[1] = findFirstOrLastPosition(mid, n - 1, False)
            break
        elif nums[mid] < t:
            i = mid + 1
        else:
            j = mid - 1

    return res


if __name__ == '__main__':
    doctest.testmod()
