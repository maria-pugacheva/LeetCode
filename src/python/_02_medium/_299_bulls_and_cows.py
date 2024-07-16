import doctest


# ---------------------------------------------------------------------
# Approach 1: Frequency Counter. Time: O(n). Space: O(1)              !
# ---------------------------------------------------------------------
def solution_one(secret: str, guess: str) -> str:
    """You are playing the Bulls and Cows game with your friend. Given
    the secret number secret and your friend's guess guess, return a
    hint for your friend's guess. The hint should be formatted as "xAyB",
    where x is the number of bulls and y is the number of cows.

    Preconditions:
        1 <= len(secret), len(guess) <= 1000
        len(secret) == len(guess)
        secret and guess consist of digits only (may contain duplicates)

    Examples:
        >>> solution_one('1', '0')
        '0A0B'
        >>> solution_one('1', '1')
        '1A0B'
        >>> solution_one('1807', '7810')
        '1A3B'
        >>> solution_one('1123', '0111')
        '1A1B'
    """
    bulls = cows = 0
    cnt = [0] * 10
    for i in range(len(secret)):
        s, g = int(secret[i]), int(guess[i])
        if s == g:
            bulls += 1
        else:
            if cnt[s] < 0:
                cows += 1
            if cnt[g] > 0:
                cows += 1
        cnt[s] += 1
        cnt[g] -= 1
    return str(bulls) + 'A' + str(cows) + 'B'


if __name__ == '__main__':
    doctest.testmod()
