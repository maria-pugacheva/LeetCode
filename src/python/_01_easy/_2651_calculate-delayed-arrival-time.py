import doctest


# ---------------------------------------------------------------------
# Approach 1: Modulo. Time: O(1)                                    ***
# ---------------------------------------------------------------------
def solution_one(arrival_time: int, delayed_time: int) -> int:
    """Return the time when the train will arrive at the station.

    Examples:
        >>> solution_one(15, 5)
        20
        >>> solution_one(13, 11)
        0
        >>> solution_one(15, 15)
        6
    """
    return (arrival_time + delayed_time) % 24


# ---------------------------------------------------------------------
# Approach 2: Subtraction. Time: O(1)                               ***
# ---------------------------------------------------------------------
def solution_two(arrival_time: int, delayed_time: int) -> int:
    """Return the time when the train will arrive at the station.

    Examples:
        >>> solution_two(15, 5)
        20
        >>> solution_two(13, 11)
        0
        >>> solution_two(15, 15)
        6
    """
    t = arrival_time + delayed_time
    return t if t < 24 else t - 24


if __name__ == '__main__':
    doctest.testmod()
