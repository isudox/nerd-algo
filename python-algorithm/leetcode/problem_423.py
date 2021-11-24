"""423. Reconstruct Original Digits from English
https://leetcode.com/problems/reconstruct-original-digits-from-english/

zero,one,two,three,four,five,six,seven,eight,nine
"""
import collections


class Solution:
    def original_digits(self, s: str) -> str:
        counter = collections.Counter(s)
        cnt = [0] * 10
        cnt[0] = counter['z']
        cnt[2] = counter['w']
        cnt[6] = counter['x']
        cnt[8] = counter['g']
        cnt[4] = counter['u']
        cnt[3] = counter['r'] - cnt[0] - cnt[4]
        cnt[1] = counter['o'] - cnt[2] - cnt[4] - cnt[0]
        cnt[5] = counter['f'] - cnt[4]
        cnt[7] = counter['v'] - cnt[5]
        cnt[9] = counter['i'] - cnt[5] - cnt[6] - cnt[8]
        ans = ''
        for i, c in enumerate(cnt):
            if c > 0:
                ans += str(i) * c
        return ans
