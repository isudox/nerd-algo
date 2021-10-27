"""496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = dict()
        stack = list()
        for i in range(len(nums2)):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                memo[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        ans = list()
        for i in range(len(nums1)):
            if nums1[i] in memo:
                ans.append(memo[nums1[i]])
            else:
                ans.append(-1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
