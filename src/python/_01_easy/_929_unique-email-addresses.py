import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n + m). Space: O(n + m)                  ***
# ---------------------------------------------------------------------
def solution(emails: List[str]) -> int:
    """Given an array of strings emails where we send one email to each
    email[i], return the number of different addresses that actually
    receive e-letters. If you add periods '.' between some characters in
    the local name part of an email address, mail sent there will be
    forwarded to the same address without dots in the local name. If you
    add a plus '+' in the local name, everything after the first plus
    sign will be ignored. This allows certain emails to be filtered.
    Note that these rules do not apply to domain names.

    Examples:
        >>> solution(['test.email+alex@leetcode.com',\
                          'test.e.mail+bob.cathy@leetcode.com',\
                          'testemail+david@lee.tcode.com'])
        2
        >>> solution(['a@leetcode.com', 'b@leetcode.com',\
                          'c@leetcode.com'])
        3
        >>> solution(['test..email+a+lex@leetcode.com',\
                          'test.e..mail++bob.cathy@leetcode.com',\
                          'testemail+david@lee.tcode.com'])
        2
    """
    uniqueEmails = set()
    for e in emails:
        cleanEmail = []
        seenPlus = False
        for i in range(len(e)):
            if e[i].isalpha() and not seenPlus:
                cleanEmail.append(e[i])
            elif e[i] == '@':
                cleanEmail.append(e[i:])
            elif e[i] == '+':
                seenPlus = True
        uniqueEmails.add(''.join(cleanEmail))
    return len(uniqueEmails)


if __name__ == '__main__':
    doctest.testmod()
