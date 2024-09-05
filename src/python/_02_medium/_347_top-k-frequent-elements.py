import doctest
from typing import List
from collections import Counter
import heapq


# ---------------------------------------------------------------------
# Approach 1: Max Heap. Time: O(n log n)                              !
# ---------------------------------------------------------------------
# Complexity Analysis: The heapq module implements a binary heap with
# push and pop operations both having a time complexity of O(log n).
# ---------------------------------------------------------------------
def solution_one(nums: List[int], k: int) -> List[int]:
    """Given an integer array nums and an integer k, return the k most
    frequent elements. You may return the answer in any order.

    Examples:
        >>> solution_one([1], 1)
        [1]
        >>> solution_one([1, 1, 1, 2, 2, 3], 2)
        [2, 1]
        >>> solution_one([1, 1, 1, 2, 2, 2, 3], 2)
        [1, 2]
        >>> solution_one([1, 1, 1, 2, 2, 2, 3], 3)
        [3, 2, 1]
    """
    cnt = Counter(nums)
    heap = []
    for key, v in cnt.items():
        heapq.heappush(heap, [v, key])
        if len(heap) > k:
            heapq.heappop(heap)
    return [key for v, key in heap]


# ---------------------------------------------------------------------
# Approach 2: Bucket Sort. Time: O(n)                                 !
# ---------------------------------------------------------------------
def solution_two(nums: List[int], k: int) -> List[int]:
    """Given an integer array nums and an integer k, return the k most
    frequent elements. You may return the answer in any order.

    Examples:
        >>> solution_two([1], 1)
        [1]
        >>> solution_two([1, 1, 1, 2, 2, 3], 2)
        [1, 2]
        >>> solution_two([1, 1, 1, 2, 2, 2, 3], 2)
        [1, 2]
        >>> solution_two([1, 1, 1, 2, 2, 2, 3], 3)
        [1, 2, 3]
    """
    cnt = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for key, v in cnt.items():
        buckets[v].append(key)
    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res


if __name__ == '__main__':
    doctest.testmod()
