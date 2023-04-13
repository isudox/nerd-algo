"""1707. Maximum XOR With an Element From Array
https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

You are given an array nums consisting of non-negative integers. You are also
given a queries array, where queries[i] = [xi, mi].

The answer to the i^th query is the maximum bitwise XOR value of xi and any
element of nums that does not exceed mi. In other words, the answer is
max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in
nums are larger than mi, then the answer is -1.

Return an integer array answer where answer.length == queries.length and
answer[i] is the answer to the i^th query.

Example 1:

Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
Explanation:
1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1
XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

Example 2:

Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
Output: [15,-1,5]

Constraints:

1 <= nums.length, queries.length <= 10^5
queries[i].length == 2
0 <= nums[j], xi, mi <= 10^9
"""
from typing import List


class Trie:
    def __init__(self) -> None:
        self.left = None
        self.right = None


class Solution:
    def maximize_xor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def add(num: int):
            cur = root
            for k in range(30, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right

        def cal(num: int) -> int:
            if not root.left and not root.right:
                return -1
            cur = root
            ret = 0
            for k in range(30, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if cur.right:
                        cur = cur.right
                        ret = (ret << 1) + 1
                    else:
                        cur = cur.left
                        ret = ret << 1
                else:
                    if cur.left:
                        cur = cur.left
                        ret = (ret << 1) + 1
                    else:
                        cur = cur.right
                        ret = ret << 1
            return ret

        nums.sort()
        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            query.append(i)
        queries.sort(key=lambda x: x[1])
        root = Trie()
        j = 0
        for x, m, i in queries:
            while j < len(nums):
                if nums[j] <= m:
                    add(nums[j])
                    j += 1
                else:
                    break
            ans[i] = cal(x)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximize_xor([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]))
