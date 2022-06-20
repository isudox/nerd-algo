"""820. Short Encoding of Words
https://leetcode.com/problems/short-encoding-of-words/
"""
from typing import List

"""
Input: words = ["time", "me", "bell"] Output: 10
Explanation: A valid encoding would be s =
"time#bell#" and indices = [0, 2, 5]
"""
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ans = words[0] + '#'
        for i in range(1, len(words)):
            word = words[i]
            
        return 0
