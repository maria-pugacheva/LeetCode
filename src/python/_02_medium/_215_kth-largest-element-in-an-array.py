import doctest
from typing import List
import heapq


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n). Space: O(1)                ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], k: int) -> int:
    """Given an integer array nums and an integer k, return the k-th
    largest element in the array, where k refers to the k-th largest
    element in sorted order, not the k-th distinct element.

    Examples:
        >>> solution_one([1], 1)
        1
        >>> solution_one([2, 2], 2)
        2
        >>> solution_one([2, 7, 4, 1, 8, 1], 5)
        1
        >>> solution_one([3, 2, 1, 5, 6, 4], 2)
        5
        >>> solution_one([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4
    """
    nums.sort()
    return nums[len(nums) - k]


# ---------------------------------------------------------------------
# Approach 2: Min Heap. Time: O(n log k). Space: O(k)               ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int], k: int) -> int:
    """Given an integer array nums and an integer k, return the k-th
    largest element in the array, where k refers to the k-th largest
    element in sorted order, not the k-th distinct element.

    Examples:
        >>> solution_two([1], 1)
        1
        >>> solution_two([2, 2], 2)
        2
        >>> solution_two([2, 7, 4, 1, 8, 1], 5)
        1
        >>> solution_two([3, 2, 1, 5, 6, 4], 2)
        5
        >>> solution_two([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4
    """
    minHeap = []
    cnt = 0
    for n in nums:
        heapq.heappush(minHeap, n)
        cnt += 1
        if cnt > k:
            heapq.heappop(minHeap)
            cnt -= 1
    return minHeap[0]


if __name__ == '__main__':
    doctest.testmod()
