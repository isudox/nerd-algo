"""789. Escape The Ghosts
https://leetcode.com/problems/escape-the-ghosts/
"""
from typing import List


class Solution:
    def escape_ghosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        cnt = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            if abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) <= cnt:
                return False
        return True
