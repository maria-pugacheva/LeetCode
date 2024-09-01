import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting + Two Pointers. T: O(n^2). S: О(n) <- sorting   !
# ---------------------------------------------------------------------
# Complexity Analysis: O(n log n + n^2) -> O(n^2)
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> List[List[int]]:
    """Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
    and the sum of the elements at these indices is zero.

    Examples:
        >>> solution_one([0, 1, 1])
        []
        >>> solution_one([0, 0, 0])
        [[0, 0, 0]]
        >>> solution_one([0, 0, 0, 0])
        [[0, 0, 0]]
        >>> solution_one([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
    """
    res = []
    nums.sort()
    for k in range(len(nums) - 2):
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        if nums[k] > 0:
            break
        i, j = k + 1, len(nums) - 1
        while i < j:
            n = nums[k] + nums[i] + nums[j]
            if n == 0:
                res.append([nums[k], nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
                j -= 1
            elif n < 0:
                i += 1
            else:
                j -= 1
    return res


# ---------------------------------------------------------------------
# Approach 2: Sorting + HashSet. T: O(n^2). S: О(n) for the set       !
# ---------------------------------------------------------------------
# Complexity Analysis: O(n log n + n^2) -> O(n^2)
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> List[List[int]]:
    """Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
    and the sum of the elements at these indices is zero.

    Examples:
        >>> solution_two([0, 1, 1])
        []
        >>> solution_two([0, 0, 0])
        [[0, 0, 0]]
        >>> solution_two([0, 0, 0, 0])
        [[0, 0, 0]]
        >>> solution_two([-1, 0, 1, 2, -1, -4]) # -4, -1, -1, 0, 1, 2
        [[-1, 0, 1], [-1, -1, 2]]
    """
    def twoSum(ans, i: int, t: int) -> List[int]:
        seen = set()
        j = i + 1
        while j < len(nums):
            c = t - nums[j]
            if c in seen:
                ans.append([nums[i], c, nums[j]])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
        return []

    res = []
    nums.sort()
    for k in range(len(nums) - 2):
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        if nums[k] > 0:
            break
        twoSum(res, k, 0 - nums[k])

    return res


# ---------------------------------------------------------------------
# Approach 3: No-Sort. Time: O(n^2). Space: О(n) for the set/map      !
# ---------------------------------------------------------------------
# This algorithm is noticeably slower than the previous approach.
# Lookups in a hash set, though requiring a constant time, are expensive
# compared to the direct memory access.
# ---------------------------------------------------------------------
# Approach #1 is recommended for interviews, while Approach #3 is
# intended to address potential follow-up questions, such as, "What if
# sorting the array is not feasible?". It is important to note that,
# although feasible, the efficiency of Approach #3 is highly dependent
# on the nature of the input. If the array is very large and contains
# numerous duplicates with only a few matching triplets, the "No-Sort"
# approach would be more memory-efficient.
# ---------------------------------------------------------------------
def solution_three(nums: List[int]) -> List[List[int]]:
    """Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
    and the sum of the elements at these indices is zero.

    Examples:
        >>> solution_three([0, 1, 1])
        []
        >>> solution_three([0, 0, 0])
        [[0, 0, 0]]
        >>> solution_three([0, 0, 0, 0])
        [[0, 0, 0]]
        >>> solution_three([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
    """
    res = set()
    dups = set()
    seen = {}
    for i, v1 in enumerate(nums):
        if v1 not in dups:
            dups.add(v1)
            for j, v2 in enumerate(nums[i + 1:]):
                c = 0 - v1 - v2
                if c in seen and seen[c] == i:
                    res.add(tuple(sorted([c, v1, v2])))
                seen[v2] = i
    return [list(x) for x in res]


if __name__ == '__main__':
    doctest.testmod()
