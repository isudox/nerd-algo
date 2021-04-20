"""28. Implement strStr()
https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great
question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:

0 <= haystack.length, needle.length <= 5 * 10^4
haystack and needle consist of only lower-case English characters.
"""


class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        """
        a little optimization than brute force.
        """
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if n < m:
            return -1
        store1, store2 = [0] * 26, [0] * 26
        for i in range(m):
            store1[ord(haystack[i]) - 97] += 1
            store2[ord(needle[i]) - 97] += 1
        for i in range(n - m + 1):
            if store1 == store2 and haystack[i: i + m] == needle:
                return i
            if i == n - m:
                return -1
            store1[ord(haystack[i]) - 97] -= 1
            store1[ord(haystack[i + m]) - 97] += 1
        return -1

    def str_str_2(self, haystack: str, needle: str) -> int:
        """
        brute force
        """
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
            if j == len(needle):
                return i - j
        return -1

    def str_str_kmp(self, haystack: str, needle: str) -> int:
        """
        KMP
        """
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        # partial match table
        pmt = [0] * len(needle)
        j = 0
        # phase1: build the partial match table.
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = pmt[j - 1]
            if needle[i] == needle[j]:
                j += 1
            pmt[i] = j
        j = 0
        # phase2: match string by using partial match table.
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = pmt[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1
        return -1
