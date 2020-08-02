"""76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the
empty string "".
If there is such window, you are guaranteed that there will always be only
one unique minimum window in S.
"""


class Solution:
    def min_window(self, s: str, t: str) -> str:
        def is_valid(d: dict):
            for v in d.values():
                if v > 0:
                    return False
            return True

        store = {}
        for c in t:
            if c not in store:
                store[c] = 1
            else:
                store[c] = store[c] + 1
        min_head = min_tail = 0
        head = tail = -1
        min_len = len(s) + 1
        not_found = True
        while head <= tail:
            if not_found:
                # if not found, move the cur_tail pointer.
                if tail == len(s) - 1:
                    break
                tail += 1
                cur_char = s[tail]
                if cur_char in store:
                    store[cur_char] = store[cur_char] - 1
                    if is_valid(store):
                        not_found = False
                        cur_len = tail - head
                        if cur_len < min_len:
                            min_head, min_tail, min_len = head, tail, cur_len
            else:
                # already found, move the cur_head pointer.
                head += 1
                cur_char = s[head]
                cur_len = tail - head
                if cur_char in store:
                    store[cur_char] = store[cur_char] + 1
                    if not is_valid(store):
                        not_found = True
                    else:
                        if cur_len < min_len:
                            min_head, min_tail, min_len = head, tail, cur_len
                else:
                    if cur_len < min_len:
                        min_head, min_tail, min_len = head, tail, cur_len
        return s[min_head + 1:min_tail + 1]
