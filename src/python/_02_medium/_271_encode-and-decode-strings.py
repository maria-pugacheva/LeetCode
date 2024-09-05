from typing import List


# ---------------------------------------------------------------------
# Approach 1: Chunked Transfer Encoding. Time: O(n). Space: O(k)      !
# ---------------------------------------------------------------------
# Complexity Analysis: Let n denote the total number of characters
# across all strings in the input list and k denote the number of
# strings.
# ---------------------------------------------------------------------
class Solution:
    def encode(self, words: List[str]) -> str:
        return ''.join([str(len(w)) + '#' + w for w in words])

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            res.append(s[j + 1:j + 1 + n])
            i = j + 1 + n
        return res


s = Solution()
print(s.decode(s.encode(['hello', 'world'])))
print(s.decode(s.encode(['he3#llo', 'world2'])))
print(s.decode(s.encode(['he3#llo', 'world2#'])))
