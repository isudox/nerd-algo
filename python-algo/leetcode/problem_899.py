"""899. Orderly Queue
https://leetcode.com/problems/orderly-queue/
"""


class Solution:
    def orderly_queue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return ''.join(sorted(s))
