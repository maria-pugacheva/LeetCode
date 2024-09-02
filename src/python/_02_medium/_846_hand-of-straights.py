import doctest
from typing import List
from collections import Counter
import heapq


# ---------------------------------------------------------------------
# Approach 1: HashMap + Min Heap. T: O(n log n + n * k). S: O(n)      !
# ---------------------------------------------------------------------
# Complexity Analysis: Let k be groupSize.
# ---------------------------------------------------------------------
def solution(hand: List[int], groupSize: int) -> bool:
    """Given an array hand where hand[i] is the value on the i-th card
    and an integer groupSize, return True if the cards can be rearranged
    into groups of groupSize consecutive cards, or False otherwise.
    
    Examples:
        >>> solution([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
        True
        >>> solution([1, 2, 3, 4, 5], 4)
        False
    """
    if len(hand) % groupSize:
        return False

    cnt = Counter(hand)

    minH = list(cnt.keys())
    heapq.heapify(minH)
    while minH:
        first = minH[0]
        for n in range(first, first + groupSize):
            if n not in cnt:
                return False
            cnt[n] -= 1
            if cnt[n] == 0:
                if n != minH[0]:
                    return False
                heapq.heappop(minH)
    return True


if __name__ == '__main__':
    doctest.testmod()
