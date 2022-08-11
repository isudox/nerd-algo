"""1282. Group the People Given the Group Size They Belong To
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        mapper = {}
        for i, size in enumerate(groupSizes):
            if size not in mapper:
                mapper[size] = []
            mapper[size].append(i)
            if len(mapper[size]) == size:
                ans.append(mapper[size])
                del mapper[size]
        return ans
