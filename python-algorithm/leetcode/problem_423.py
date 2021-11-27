"""423. Reconstruct Original Digits from English
https://leetcode.com/problems/reconstruct-original-digits-from-english/
"""
import collections


class Solution:
    def original_digits(self, s: str) -> str:
        nums = [{'z': 1, 'e': 1, 'r': 1, 'o': 1},  # zero
                {'o': 1, 'n': 1, 'e': 1},  # one
                {'t': 1, 'w': 1, 'o': 1},  # two
                {'t': 1, 'h': 1, 'r': 1, 'e': 2},  # three
                {'f': 1, 'o': 1, 'u': 1, 'r': 1},  # four
                {'f': 1, 'i': 1, 'v': 1, 'e': 1},  # five
                {'s': 1, 'i': 1, 'x': 1},  # six
                {'s': 1, 'e': 2, 'v': 1, 'n': 1},  # seven
                {'e': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1},  # eight
                {'n': 2, 'i': 1, 'e': 1},  # nine
                ]
        counter = collections.Counter(s)
        ans = ''
        i = 0
        while i < 10:
            num = nums[i]
            flag = True
            for ch, cnt in num.items():
                if counter[ch] < cnt:
                    flag = False
                    break
            if flag:
                ans += str(i)
                for ch, cnt in num.items():
                    counter[ch] -= cnt
            else:
                i += 1
        return ans
