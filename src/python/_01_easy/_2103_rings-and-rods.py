import doctest


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(rings: str) -> int:
    """Return the number of rods that have all three colors of rings
    on them.

    Examples:
        >>> solution('G4')
        0
        >>> solution('B0B6G0R6R0R6G9')
        1
        >>> solution('B0R0G0R9R0B0G0')
        1
    """
    rods = [[0 for i in range(3)] for _ in range(10)]
    colors = {'B': 0, 'G': 1, 'R': 2}
    cnt = 0
    for i in range(1, len(rings), 2):
        if rods[int(rings[i])][0] != -1:
            rods[int(rings[i])][int(colors[rings[i-1]])] = 1
            if sum(rods[int(rings[i])]) == 3:
                cnt += 1
                rods[int(rings[i])][0] = -1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
