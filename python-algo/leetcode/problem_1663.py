"""1663. Smallest String With A Given Numeric Value
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z, rem = divmod(k, 26)
        ans = ['z'] * z
        if rem > 0:
            ans.insert(0, chr(96 + rem))
        if len(ans) == n:
            return ''.join(ans)
        diff = n - len(ans)
        prefix = ''
        i = 0
        while diff > 0:
            x = min(ord(ans[i]) - 97, diff)
            ans[i] = chr(ord(ans[i]) - x)
            prefix += 'a' * x
            diff -= x
            i += 1
        return prefix + ''.join(ans)
