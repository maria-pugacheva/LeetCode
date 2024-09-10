import doctest
from typing import List
import heapq


# ---------------------------------------------------------------------
# Approach 1: Max Heap. Time: O(n log n)                            ***
# ---------------------------------------------------------------------
def solution(stones: List[int]) -> int:
    """Given an array stones where each element represents a stone's
    weight, repeatedly smash the two heaviest stones together. If their
    weights are equal, both stones are destroyed; if one stone is
    heavier, the two stones are replaced with the difference between
    their weights. Return the weight of the last remaining stone, or 0
    if no stones are left.

    Examples:
        >>> solution([1])
        1
        >>> solution([2, 2])
        0
        >>> solution([2, 7, 4, 1, 8, 1])
        1
    """
    maxHeap = [-s for s in stones]
    heapq.heapify(maxHeap)
    while len(maxHeap) > 1:
        y = -1 * heapq.heappop(maxHeap)
        x = -1 * heapq.heappop(maxHeap)
        if y != x:
            heapq.heappush(maxHeap, -1 * (y - x))
    return 0 if not maxHeap else -1 * maxHeap[0]


if __name__ == '__main__':
    doctest.testmod()
