"""2178. Maximum Split of Positive Even Integers
https://leetcode.com/problems/maximum-split-of-positive-even-integers/
"""
import math
from typing import List


class Solution:
    def maximum_even_split(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        x = int(math.sqrt(finalSum * 4))
        if x % 2 == 1:
            x -= 1
        if x * (x + 2) // 4 > finalSum:
            x -= 2
        ans = list(range(2, x + 1, 2))
        ans[-1] += finalSum - (x + 2) * x // 4
        return ans

    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        ans = []
        num = 2
        while num < finalSum // 2:
            ans.append(num)
            finalSum -= num
            num += 2
        if finalSum:
            ans.append(finalSum)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximum_even_split(28))
    print(sol.maximumEvenSplit(28))
    print(sol.maximum_even_split(100))
    print(sol.maximumEvenSplit(100))
    print(sol.maximum_even_split(10000000000))
    print(sol.maximumEvenSplit(10000000000))
