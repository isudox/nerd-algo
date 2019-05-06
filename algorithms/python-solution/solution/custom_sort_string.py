# -*- coding: utf-8 -*-
"""791. Custom Sort String
https://leetcode.com/problems/custom-sort-string/

`S` and `T` are strings composed of lowercase letters. In `S`,
no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters
of T so that they match the order that S was sorted. More specifically,
if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example 1:

Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T.
"dcba", "cdba", "cbda" are also valid outputs.

Example 2:

Input:
S = "kqep"
T = "pekeq"
Output: "kqeep"


Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""


class Solution:
    def custom_sort_string(self, s: str, t: str) -> str:
        di, li = {}, []
        for i in range(len(t)):
            c = t[i]
            if c in s:
                li.append(i)
                if c not in di:
                    di[c] = 1
                else:
                    di[c] = di[c] + 1

        ans = ""
        for c in s:
            if c in di:
                ans += c * di[c]
        for i in range(len(t)):
            if i not in li:
                ans += t[i]

        return ans
