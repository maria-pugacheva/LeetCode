import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n + m). Space: O(1)             **!
# ---------------------------------------------------------------------
def solution(word: str, abbr: str) -> bool:
    """Given a string word and an abbreviation abbr, return whether the
    string matches the given abbreviation. A string can be abbreviated
    by replacing any number of non-adjacent, non-empty substrings with
    their lengths. The lengths should not have leading zeros.

    Examples:
        >>> solution('apple', 'a2e')
        False
        >>> solution('substitution', 's55n')
        False
        >>> solution('substitution', 's010n')
        False
        >>> solution('substitution', 's0ubstitution')
        False
        >>> solution('internationalization', 'i12iz4n')
        True
    """
    n1, n2 = len(word), len(abbr)
    i, j = 0, 0
    while j < n2:
        if abbr[j] == '0':
            return False
        if abbr[j].isnumeric():
            n = 0
            while j < n2 and abbr[j].isnumeric():
                n = n * 10 + int(abbr[j])
                j += 1
            i += n
        else:
            if i < n1 and word[i] != abbr[j]:
                return False
            i += 1
            j += 1
    return i == n1 and j == n2


if __name__ == '__main__':
    doctest.testmod()
