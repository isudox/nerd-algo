"""345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
"""


class Solution:
    def reverse_vowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        ans = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if ans[i] not in vowels:
                i += 1
            if ans[j] not in vowels:
                j -= 1
            if ans[i] in vowels and ans[j] in vowels:
                ans[i], ans[j] = ans[j], ans[i]
                i += 1
                j -= 1
        return ''.join(ans)
