import doctest
from typing import List
from collections import Counter
import heapq


# ---------------------------------------------------------------------
# Approach 1: Max Heap. Time: O(n log k)                              !
# ---------------------------------------------------------------------
def solution(nums: List[int], k: int) -> List[int]:
    """Merge overlapping intervals and return an array of the
    non-overlapping intervals that cover all the intervals in the input.

    Examples:
        >>> solution([1], 1)
        [1]
        >>> solution([1, 1, 1, 2, 2, 3], 2)
        [2, 1]
    """
    cnt = Counter(nums)
    heap = []
    for key, v in cnt.items():
        heapq.heappush(heap, [v, key])
        if len(heap) > k:
            heapq.heappop(heap)
    return [key for v, key in heap]


if __name__ == '__main__':
    doctest.testmod()
