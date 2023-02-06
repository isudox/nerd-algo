"""438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p),
        if n < m:
            return []
        ans = []
        counter = collections.Counter(p)
        for i in range(n):
            if s[i] in counter:
                counter[s[i]] -= 1
            if i >= m and s[i - m] in counter:
                counter[s[i - m]] += 1
            if i >= m - 1:
                for cnt in counter.values():
                    if cnt > 0:
                        break
                else:
                    ans.append(i - m + 1)
        return ans

    def find_anagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        ans = []
        store = {}
        temp = {}
        for i in range(np):
            store[p[i]] = (store[p[i]] + 1) if p[i] in store else 1
            temp[s[i]] = (temp[s[i]] + 1) if s[i] in temp else 1
        i, j = 0, np - 1
        while j < ns:
            if store == temp:
                ans.append(i)
            if j == ns - 1:
                break
            if temp[s[i]] == 1:
                del temp[s[i]]
            else:
                temp[s[i]] = temp[s[i]] - 1
            temp[s[j + 1]] = (temp[s[j + 1]] + 1) if s[j + 1] in temp else 1
            i += 1
            j += 1

        return ans
