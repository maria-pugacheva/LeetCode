import doctest


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(1)                                    ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Return the latest valid time by replacing the hidden digits in s.

    Preconditions:
        s is in the format hh:mm

    Examples:
        >>> solution('?4:??')
        '14:59'
        >>> solution('0?:3?')
        '09:39'
        >>> solution('??:??')
        '23:59'
    """
    time = [ch for ch in s]
    if time[0] == '?':
        time[0] = '2' if (time[1] == '?' or time[1] < '4') else '1'
    if time[1] == '?':
        time[1] = '3' if time[0] == '2' else '9'
    if time[3] == '?':
        time[3] = '5'
    if time[4] == '?':
        time[4] = '9'
    return ''.join(time)


if __name__ == '__main__':
    doctest.testmod()
