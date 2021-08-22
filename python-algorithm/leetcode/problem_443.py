"""443. String Compression
https://leetcode.com/problems/string-compression/
"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = ''
        cnt = 0
        store = []
        for char in chars:
            if char == prev:
                cnt += 1
            else:
                if prev:
                    store.append(prev)
                    if cnt > 1:
                        for digit in str(cnt):
                            store.append(digit)
                cnt = 1
                prev = char
        store.append(prev)
        if cnt > 1:
            for digit in str(cnt):
                store.append(digit)
        for i in range(len(store)):
            chars[i] = store[i]
        chars = chars[:len(store)]
        return len(chars)
