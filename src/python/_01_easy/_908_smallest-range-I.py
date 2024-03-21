import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Max and Min. Time: O(n)                               ***
# ---------------------------------------------------------------------
def solution(nums: List[int], k: int) -> int:
    """Choose any index i where 0 <= i < len(nums) and change nums[i]
    to nums[i] + x where x is an integer from the range [-k, k]. You can
    apply this operation at most once for each index i. The score of
    nums is the difference between the maximum and minimum elements in
    nums. Return the minimum score of nums after applying the mentioned
    operation at most once for each index in nums.

    Examples:
        >>> solution([1], 0)
        0
        >>> solution([0, 10], 2)
        6
        >>> solution([1, 3, 6], 3)
        0
    """
    diff = (max(nums) - k) - (min(nums) + k)
    return diff if diff > 0 else 0


if __name__ == '__main__':
    doctest.testmod()
