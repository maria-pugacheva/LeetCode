import doctest


# ---------------------------------------------------------------------
# Approach 1: Append. Time: O(n)                                    ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Convert s to Goat Latin.

    Examples:
        >>> solution('I am fine')
        'Imaa ammaaa inefmaaaa'
        >>> solution('I speak Goat Latin')
        'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
        >>> solution('The quick brown fox')
        'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa'
    """
    res, v, cnt, ch = [], {'a', 'o', 'u', 'i', 'e'}, 1, ''
    for i in range(len(s)):
        if s[i] == ' ' or i == len(s) - 1:
            if i == len(s) - 1:
                res.append(s[i])
            if ch:
                res.append(ch)
                ch = ''
            res.append('ma' + 'a' * cnt)
            if s[i] == ' ':
                res.append(' ')
            cnt += 1
        elif (i == 0 or s[i - 1] == ' ') and s[i].lower() not in v:
            ch = s[i]
        else:
            res.append(s[i])
    return ''.join(res)


# ---------------------------------------------------------------------
# Approach 2: Split. Time: O(n)                                     ^**
# ---------------------------------------------------------------------
def solution_two(s: str) -> str:
    """Convert s to Goat Latin.

    Examples:
        >>> solution_two('I am fine')
        'Imaa ammaaa inefmaaaa'
        >>> solution_two('I speak Goat Latin')
        'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
        >>> solution_two('The quick brown fox')
        'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa'
    """
    res, v, cnt = s.split(), {'a', 'o', 'u', 'i', 'e'}, 1
    for i in range(len(res)):
        if res[i][0].lower() not in v:
            t = res[i][0]
            res[i] = res[i][1:] + t
        res[i] += ('ma' + 'a' * cnt)
        cnt += 1
    return ' '.join(res)


if __name__ == '__main__':
    doctest.testmod()
