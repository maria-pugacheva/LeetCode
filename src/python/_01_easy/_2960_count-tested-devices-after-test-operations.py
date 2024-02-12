import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Count. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return an integer denoting the number of devices that will be
    tested after performing the test operations mentioned below.

    You are given a 0-indexed integer array nums having length n,
    denoting the battery percentages of n 0-indexed devices. Your task
    is to test each device i in order from 0 to n - 1, by performing
    the following test operations:
        - If nums[i] is greater than 0:
            - Increment the count of tested devices
            - Decrease the battery percentage of all devices with
            indices j in the range [i + 1, n - 1] by 1, ensuring their
            battery percentage never goes below 0
            - Move to the next device
        - Otherwise, move to the next device without performing any test

    Examples:
        >>> solution_one([0, 1, 2])
        2
        >>> solution_one([1, 1, 2, 1, 3])
        3
    """
    cnt = 0
    for n in nums:
        if n - cnt > 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
