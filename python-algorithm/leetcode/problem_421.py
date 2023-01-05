"""421. Maximum XOR of Two Numbers in an Array
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
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
