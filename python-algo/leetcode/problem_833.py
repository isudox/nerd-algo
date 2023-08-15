"""833. Find And Replace in String
https://leetcode.com/problems/find-and-replace-in-string
"""
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        m, n = len(indices), len(s),
        ops = list(range(m))
        ops.sort(key=lambda x: indices[x])
        ans = []
        i = j = 0
        while i < n:
            while j < m and indices[ops[j]] < i:
                j += 1
            ok = False
            while j < m and indices[ops[j]] == i:
                if s[i:i+len(sources[ops[j]])] == sources[ops[j]]:
                    ok = True
                    break
                j += 1
            if ok:
                ans.append(targets[ops[j]])
                i += len(sources[ops[j]])
            else:
                ans.append((s[i]))
                i += 1
        return ''.join(ans)
