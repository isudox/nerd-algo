"""438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p,
find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of
both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from typing import List


class Solution:
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
