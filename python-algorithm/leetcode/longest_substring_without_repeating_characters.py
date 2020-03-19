"""Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating
characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring,
             "pwke" is a subsequence and not a substring
"""


class Solution:
    def length_of_longest_substring_1(self, s: str) -> int:
        """
        time complexity: O(N^2)
        space complexity: O(N)
        """
        n = len(s)
        store = {}
        max_len = 0
        for i in range(n):
            if n - i <= max_len:
                break
            cur_len = 0
            for j in range(i, n):
                key = s[j]
                if key in store:
                    store.clear()
                    break
                store[key] = 1
                cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len

    def length_of_longest_substring_2(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            if n - i <= max_len:
                break
            store = ''
            for j in range(i, n):
                if s[j] in store:
                    break
                store += s[j]
                max_len = max(max_len, len(store))
        return max_len

    def length_of_longest_substring_3(self, s: str) -> int:
        i, n = 0, len(s)
        if n <= 1:
            return n
        store = {}
        max_len = 0
        while i < n - 1:
            j = i
            while j < n and s[j] not in store:
                store[s[j]] = j
                j += 1
            max_len = max(max_len, j - i)
            if j == n:
                break
            i = store[s[j]] + 1
            store.clear()

        return max_len

    def length_of_longest_substring_4(self, s: str) -> int:
        store = []
        max_len = 0
        i, j, n = 0, 0, len(s)
        while i < n and j < n:
            if s[j] not in store:
                store.append(s[j])
                j += 1
                max_len = max(max_len, j - i)
            else:
                store.remove(s[i])
                i += 1
        return max_len

    def length_of_longest_substring_5(self, s: str) -> int:
        store = {}
        i, j, n, max_len = 0, 0, len(s), 0
        while i < n and j < n:
            if s[j] not in store:
                store[s[j]] = j
                j += 1
                max_len = max(max_len, j - i)
            else:
                temp = store[s[j]] + 1
                for k in range(i, temp):
                    store.pop(s[k])
                i = temp
        return max_len
