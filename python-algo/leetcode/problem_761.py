"""761. Special Binary String
https://leetcode.com/problems/special-binary-string/
"""


class Solution:
    def make_largest_special(self, s: str) -> str:
        n = len(s)
        if n <= 2:
            return s
        subs = []
        cnt = 0
        left = 0
        for i in range(n):
            if s[i] == '1':
                cnt += 1
                continue
            cnt -= 1
            if cnt == 0:
                subs.append('1' + self.make_largest_special(s[left + 1:i]) + '0')
                left = i + 1
        subs.sort(reverse=True)
        return ''.join(subs)
