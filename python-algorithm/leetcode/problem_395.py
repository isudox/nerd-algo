"""395. Longest Substring with At Least K Repeating Characters
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Given a string s and an integer k, return the length of the longest substring
of s such that the frequency of each character in this substring is greater
than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and
'b' is repeated 3 times.

Constraints:
1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^5
"""


class Solution:
    def longest_substring(self, s: str, k: int) -> int:
        store = [0] * 26
        ans = 0
        for c in s:
            store[ord(c) - ord('a')] += 1
        blacklist = []
        for i, count in enumerate(store):
            if 0 < count < k:
                blacklist.append(chr(ord('a') + i))
        if not blacklist:
            return len(s)
        i = j = 0
        while j < len(s):
            if s[j] in blacklist:
                ret = self.longest_substring(s[i:j], k)
                ans = max(ans, ret)
                i = j + 1
            j += 1
        return max(ans, self.longest_substring(s[i:j], k))
