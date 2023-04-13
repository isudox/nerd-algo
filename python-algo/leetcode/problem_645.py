"""645. Set Mismatch
https://leetcode.com/problems/set-mismatch/
"""
from typ import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff = (1 + n) * n // 2
        seen = [0] * (n + 1)
        found = False
        ans = []
        for num in nums:
            diff -= num
            if not found:
                if seen[num]:
                    ans.append(num)
                else:
                    seen[num] = 1
        ans.append(ans[0] + diff)
        return ans
