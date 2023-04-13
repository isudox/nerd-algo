"""609. Find Duplicate File in System
https://leetcode.com/problems/find-duplicate-file-in-system/
"""
from typing import List
import collections


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = collections.defaultdict(list)
        for path in paths:
            segments = path.split(' ')
            filepath = segments[0]
            for file in segments[1:]:
                splits = file.split('(')
                filename, content = splits[0], splits[1][:-1]
                store[content].append(filepath + '/' + filename)
        ans = []
        for k, v in store.items():
            if len(v) > 1:
                ans.append(v)
        return ans
