import doctest


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(1)                                      ***
# ---------------------------------------------------------------------
def solution(n: int) -> bool:
    """You are playing the following Nim Game with your friend.
    Initially, there is a heap of stones on the table. You and your
    friend will alternate taking turns, and you go first. On each turn,
    the person whose turn it is will remove 1 to 3 stones from the heap.
    The one who removes the last stone is the winner. Given n, the
    number of stones in the heap, return True if you can win the game
    assuming both you and your friend play optimally; otherwise,
    return False.

    Examples:
        >>> solution(1)
        True
        >>> solution(2)
        True
        >>> solution(4)
        False
        >>> solution(5)
        True
    """
    return n % 4 != 0


if __name__ == '__main__':
    doctest.testmod()
