"""763. Partition Labels
https://leetcode.com/problems/partition-labels/

A string S of lowercase English letters is given.
We want to partition this string into as many parts as possible so that
each letter appears in at most one part, and return a list of integers
representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect,
because it splits S into less parts.

Note:

  S will have length in range [1, 500].
  S will consist of lowercase English letters ('a' to 'z') only.
"""
from typing import List


class Solution:
    def partition_labels(self, s: str) -> List[int]:
        n = len(s)
        last_pos = [-1] * 26
        for i in range(n):
            last_pos[ord(s[i]) - 97] = i
        ans = []
        i = 0
        while i < n:
            start = i
            end = last_pos[ord(s[i]) - 97]
            while i <= end:
                end = max(end, last_pos[ord(s[i]) - 97])
                i += 1
            ans.append(end - start + 1)
        return ans
