import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n). Space: O(n)                 ***
# ---------------------------------------------------------------------
# 1. Add the vowels to a set.
# 2. Convert the given string to a list of characters.
# 3. Maintain two pointers to iterate over the list from both ends.
#    The left pointer starts at the beginning of the list and moves
#    right until it encounters a vowel.  The right pointer starts at the
#    end of the list and moves left until it encounters a vowel.  Once a
#    vowel for each pointer is found, swap the vowels.  Continue while
#    the left pointer is less than the right pointer.
# 4. Convert the modified list of characters to a string.
# 5. Return the new string.
# ---------------------------------------------------------------------
def solution_one(s: str) -> str:
    """Reverse the vowels in s.

    Notes:
        The letter 'Y' is not considered to be a vowel.

    Examples:
        >>> solution_one('Apple')
        'epplA'
        >>> solution_one('hello')
        'holle'
        >>> solution_one('leetcode')
        'leotcede'
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    rev = list(s)
    i = 0
    j = len(rev) - 1
    while i < j:
        if rev[i] in vowels and rev[j] in vowels:
            rev[i], rev[j] = rev[j], rev[i]
            i += 1
            j -= 1
        elif rev[i] in vowels:
            j -= 1
        else:
            i += 1
    return ''.join(rev)


if __name__ == '__main__':
    doctest.testmod()
