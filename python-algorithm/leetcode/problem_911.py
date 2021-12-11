"""911. Online Election
https://leetcode.com/problems/online-election/
"""
import collections


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.stack = []
        self.times = times
        counter = collections.defaultdict(int)
        counter[-1] = -1
        top = -1
        for p in persons:
            counter[p] += 1
            if counter[p] >= counter[top]:
                top = p
            self.stack.append(top)

    def q(self, t: int) -> int:
        lo, hi = 0, len(self.times) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if self.times[mid] <= t:
                lo = mid
            else:
                hi = mid - 1
        return self.stack[lo]