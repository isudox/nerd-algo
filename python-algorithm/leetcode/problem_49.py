"""49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_str(s: str) -> str:
            return ''.join(sorted(s))

        checked = {}
        for ele in strs:
            sorted_str = sort_str(ele)
            if sorted_str in checked:
                checked[sorted_str] += [ele]
            else:
                checked[sorted_str] = [ele]
        return list(checked.values())
