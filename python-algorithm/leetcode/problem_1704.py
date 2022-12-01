"""1704. Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        cnt = 0
        vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
        while i < j:
            if s[i] in vowels:
                cnt += 1
            if s[j] in vowels:
                cnt -= 1
            i += 1
            j -= 1
        return cnt == 0
