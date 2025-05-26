import doctest
from typing import List
from collections import Counter
import heapq


# ---------------------------------------------------------------------
# Approach 1: Heap. Time: O(n log k). Space: O(n)                     !
# ---------------------------------------------------------------------
# Complexity Analysis: Each heappush and heappop operation is O(log k)
# because the heap size is maintained at most k + 1, then reduced back
# to k.
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

    minHeap, i = [], 0
    heapq.heapify(minHeap)
    for key, val in cnt.items():
        heapq.heappush(minHeap, [val, key])
        i += 1
        if i > k:
            heapq.heappop(minHeap)
            i -= 1

    return [key for val, key in minHeap]


# ---------------------------------------------------------------------
# Approach 2: Bucket Sort. Time: O(n). Space: O(n)                    !
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
    for key, val in cnt.items():
        buckets[val].append(key)

    res = []
    for i in range(len(buckets) - 1, 0, -1):
        res.extend(buckets[i])
        if len(res) == k:
            break
    return res


if __name__ == '__main__':
    doctest.testmod()
