"""1239. Maximum Length of a Concatenated String with Unique Characters
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
"""
from typing import List


class Solution:
    def max_length(self, arr: List[str]) -> int:
        def check(char_set, string: str) -> bool:
            for c in string:
                if c in char_set:
                    return False
            return True

        def add(char_set, string: str) -> None:
            for c in string:
                char_set.add(c)

        def remove(char_set, string: str) -> None:
            for c in string:
                char_set.remove(c)

        def dfs(i: int, char_set) -> int:
            if i == len(arr):
                return 0
            if arr[i] == '':
                return dfs(i + 1, char_set)
            ret = 0
            if check(char_set, arr[i]):
                # option1: pick current string.
                add(char_set, arr[i])
                ret = dfs(i + 1, char_set) + len(arr[i])
                remove(char_set, arr[i])
            # option2: skip current string.
            return max(ret, dfs(i + 1, char_set))

        for i in range(len(arr)):
            if len(arr[i]) != len(set(arr[i])):
                arr[i] = ''
        return dfs(0, set())
