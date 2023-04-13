"""1422. Maximum Score After Splitting a String
https://leetcode.com/problems/maximum-score-after-splitting-a-string/
"""


class Solution:
    def max_score(self, s: str) -> int:
        ans = 0
        cnt_0, cnt_1 = 0, s.count('1')
        for i in range(len(s) - 1):
            if s[i] == '0':
                cnt_0 += 1
            else:
                cnt_1 -= 1
            ans = max(ans, cnt_1 + cnt_0)
        return ans
