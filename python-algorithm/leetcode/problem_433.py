"""433. Minimum Genetic Mutation
https://leetcode.com/problems/minimum-genetic-mutation/
"""
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank = set(bank)
        if end not in bank:
            return -1
        q1, q2 = [start], [end]
        ans = 0
        while q1:
            ans += 1
            n = len(q1)
            for i in range(n):
                cur = q1.pop(0)
                for j in range(len(cur)):
                    for ch in ['A', 'C', 'G', 'T']:
                        nxt = cur[:j] + ch + cur[j + 1:]
                        if nxt in q2:
                            return ans
                        if nxt != cur and nxt in bank:
                            bank.remove(nxt)
                            q1.append(nxt)
            if len(q1) > len(q2):
                q1, q2 = q2, q1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minMutation("AACCTTGG",
                          "AATTCCGG",
                          ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]))
