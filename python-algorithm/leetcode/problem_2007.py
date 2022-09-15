"""2007. Find Original Array From Doubled Array
https://leetcode.com/problems/find-original-array-from-doubled-array/
"""
import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        ans = []
        changed.sort()
        counter = collections.Counter(changed)
        i = 0
        while i < len(changed):
            num = changed[i]
            if counter[num]:
                if counter[num * 2]:
                    ans.append(changed[i])
                    counter[num] -= 1
                    counter[num * 2] -= 1
                else:
                    return []
            i += 1
        return ans
