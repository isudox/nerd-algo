"""504. Base 7
https://leetcode.com/problems/base-7/
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            return '-' + self.convertToBase7(-num)
        ans = ''
        while num:
            num, rem = divmod(num, 7)
            ans = str(rem) + ans
        return ans
