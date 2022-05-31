"""1461. Check If a String Contains All Binary Codes of Size K
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        n = 2 ** k
        seen = [False] * n
        num = 0
        for i in range(k):
            num = (num << 1) + int(s[i])
        seen[num] = True
        for i in range(1, len(s) - k + 1):
            num = num & (((1 << k) - 1) - (1 << (k - 1)))
            num = (num << 1) + int(s[i + k - 1])
            seen[num] = True
        for v in seen:
            if not v:
                return False
        return True
