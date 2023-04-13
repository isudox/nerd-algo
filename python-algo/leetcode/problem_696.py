"""696. Count Binary Substrings
https://leetcode.com/problems/count-binary-substrings/

Give a string s, count the number of non-empty (contiguous) substrings
that have the same number of 0's and 1's, and all the 0's and all the 1's in
these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive
1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number
of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are
not grouped together.

Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
"""


class Solution:
    def count_binary_substrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 1
        i = 0
        ans = 0
        while i < n:
            count = [1, 0] if s[i] == '0' else [0, 1]
            j = i + 1
            while j < n and s[j] == s[i]:
                count[int(s[j])] += 1
                j += 1
            k = j
            while k < n and s[k] != s[i]:
                count[int(s[k])] += 1
                k += 1
            ans += min(count)
            i = j

        return ans
