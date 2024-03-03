import doctest


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(moves: str) -> int:
    """Return the distance from the origin of the furthest point you
    can get to after making n moves.

    In the i-th move, you can choose one of the following directions:
        - move to the left if moves[i] = 'L' or moves[i] = '_'
        - move to the right if moves[i] = 'R' or moves[i] = '_'

    Examples:
        >>> solution('R')
        1
        >>> solution('RR')
        2
        >>> solution('L_RL__R')
        3
        >>> solution('_R__LL_')
        5
        >>> solution('_______')
        7
    """
    cnt = empty = 0
    for m in moves:
        if m == 'L':
            cnt += 1
        elif m == 'R':
            cnt -= 1
        else:
            empty += 1
    return abs(cnt) + empty


if __name__ == '__main__':
    doctest.testmod()
