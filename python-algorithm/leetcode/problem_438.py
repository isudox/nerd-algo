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
        ans = []
        n, m = len(s), len(p)
        if n < m:
            return []
        store, temp = {}, {}
        for c in p:
            store[c] = store[c] + 1 if c in store else 1
        found_start = False
        i = 0
        while i <= n - m:
            if s[i] not in store:
                i += 1
                continue
            if not found_start:
                found_start = True
                for j in range(i, i + m):
                    if s[j] not in store:
                        found_start = False
                        i = j + 1
                        temp.clear()
                        break
                    else:
                        temp[s[j]] = temp[s[j]] + 1 if s[j] in temp else 1
                if j - i + 1 == m and temp == store:
                    ans.append(i)
            
            i += 1
            found_start = False
            temp.clear()
        return ans


if __name__ == "__main__":
    sol = Solution()
    a = "a" * 21
    b = "a" * 10
    print(len(a))
    print(len(b))
    print(sol.find_anagrams(a, b))
