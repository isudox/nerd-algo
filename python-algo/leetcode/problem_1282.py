"""1282. Group the People Given the Group Size They Belong To
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""
import collections
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        memo = collections.defaultdict(list)
        for i, sz in enumerate(groupSizes):
            memo[sz].append(i)
            if len(memo[sz]) == sz:
                ans.append(memo[sz])
                del memo[sz]
        return ans
