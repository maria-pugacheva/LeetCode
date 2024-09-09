from typing import List
import heapq


class KthLargest:
    """A class that, for a given integer k, maintains a stream of test
    scores and continuously returns the k-th highest test score after
    each new score is submitted.
    """
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]  # the min value is stored in the 0th ind


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3) == 4)
print(obj.add(5) == 5)
print(obj.add(10) == 5)
print(obj.add(9) == 8)
print(obj.add(4) == 8)
