import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Dictionary. Time: O(n)                            ***
# ---------------------------------------------------------------------
def solution(nums1: List[int], nums2: List[int], nums3: List[int]) \
        -> List[int]:
    """Return a list containing all the distinct values that are
    present in at least two out of the three given lists. The values
    can be returned in any order.

    Preconditions:
        - 1 <= len(nums1), len(nums2), len(nums3) <= 100
        - 1 <= nums1[i], nums2[j], nums3[k] <= 100

    Examples:
        >>> solution([1, 1, 3, 2], [2, 3], [3])
        [2, 3]
        >>> solution([3, 1], [2, 3], [1, 2, 1, 1])
        [3, 1, 2]
        >>> solution([1, 2, 2], [4, 3, 3], [5, 5])
        []
    """
    res = []
    d = {}
    for i in nums1:
        d[i] = 1
    for j in nums2:
        if j not in d:
            d[j] = 2
        elif d[j] == 1:
            res.append(j)
            d[j] = -1
    for k in nums3:
        if k in d and d[k] != -1:
            res.append(k)
            d[k] = -1
    return res


# ---------------------------------------------------------------------
# Approach 2: Three Count Lists. Time: O(n)                         ***
# ---------------------------------------------------------------------
def solution_two(nums1: List[int], nums2: List[int], nums3: List[int]) \
        -> List[int]:
    """Return a list containing all the distinct values that are
    present in at least two out of the three given lists. The values
    can be returned in any order.

    Preconditions:
        - 1 <= len(nums1), len(nums2), len(nums3) <= 100
        - 1 <= nums1[i], nums2[j], nums3[k] <= 100

    Examples:
        >>> solution_two([1, 1, 3, 2], [2, 3], [3])
        [2, 3]
        >>> solution_two([3, 1], [2, 3], [1, 2, 1, 1])
        [1, 2, 3]
        >>> solution_two([1, 2, 2], [4, 3, 3], [5, 5])
        []
    """
    res = []
    cnt = [[False for i in range(101)] for _ in range(3)]
    for i in nums1:
        cnt[0][i] = True
    for j in nums2:
        cnt[1][j] = True
    for k in nums3:
        cnt[2][k] = True
    for c in range(101):
        if cnt[0][c] + cnt[1][c] + cnt[2][c] >= 2:
            res.append(c)
    return res


if __name__ == '__main__':
    doctest.testmod()


# ---------------------------------------------------------------------
# Follow-Up: How can the solution above be adapted for any number of
# input arrays?
# ---------------------------------------------------------------------
