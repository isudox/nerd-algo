"""728. Self Dividing Numbers
https://leetcode.com/problems/self-dividing-numbers/
"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(num: int) -> bool:
            mod = num
            while mod:
                mod, rem = divmod(mod, 10)
                if rem == 0 or num % rem != 0:
                    return False
            return True

        ans = []
        for num in range(left, right + 1):
            if check(num):
                ans.append(num)
        return ans
