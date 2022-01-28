"""421. Maximum XOR of Two Numbers in an Array
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

Given an integer array nums, return the maximum result of nums[i] XOR
nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:

Input: nums = [0]
Output: 0

Example 3:

Input: nums = [2,4]
Output: 6

Example 4:

Input: nums = [8,10,2]
Output: 10

Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

Constraints:

1 <= nums.length <= 2 * 10^4
0 <= nums[i] <= 2^31 - 1
"""
from typing import List


def find_maximum_xor(nums: List[int]) -> int:
    ans = 0
    for i in range(30, -1, -1):
        visited = set()
        for num in nums:
            visited.add(num >> i)
        temp = (ans << 1) + 1
        found = False
        for num in nums:
            if temp ^ (num >> i) in visited:
                found = True
                break
        if found:
            ans = temp
        else:
            ans = temp - 1
    return ans


def find_maximum_xor2(nums: List[int]) -> int:
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

    def check(num: int) -> int:
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

    root = Trie()
    ans = 0
    for i in range(1, len(nums)):
        add(nums[i - 1])
        ans = max(ans, check(nums[i]))
    return ans


class Trie:
    def __init__(self):
        self.left = None
        self.right = None
