"""869. Reordered Power of 2
https://leetcode.com/problems/reordered-power-of-2/
"""


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cnts = [0] * 10
        while n:
            cnts[n % 10] += 1
            n //= 10
        num = 1
        while num < int(1e9 + 1):
            x = num
            cur_cnts = [0] * 10
            while x:
                cur_cnts[x % 10] += 1
                x //= 10
            for i in range(10):
                if cur_cnts[i] != cnts[i]:
                    break
            else:
                return True
            num <<= 1
        return False
