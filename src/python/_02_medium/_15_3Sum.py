import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n^2)                                 !**
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> List[List[int]]:
    """Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
    and nums[i] + nums[j] + nums[k] == 0.

    Examples:
        >>> solution([0, 0, 0])
        [[0, 0, 0]]
        >>> solution([0, 0, 0, 0])
        [[0, 0, 0]]
        >>> solution([0, 1, 1])
        []
        >>> solution([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
    """
    res = []
    nums.sort()
    for k in range(len(nums) - 2):
        if k > 0 and nums[k] == nums[k-1]:
            continue
        if nums[k] > 0:
            break
        i, j = k + 1, len(nums) - 1
        while i < j:
            total = nums[k] + nums[i] + nums[j]
            if total == 0:
                res.append([nums[k], nums[i], nums[j]])
                while i < j and nums[i] == nums[i+1]:
                    i += 1
                i += 1
                j -= 1
            elif total < 0:
                i += 1
            else:
                j -= 1
    return res


if __name__ == '__main__':
    doctest.testmod()
