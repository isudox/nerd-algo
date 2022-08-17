"""804. Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words
"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        store = set()
        for word in words:
            cur = ''
            for ch in word:
                cur += codes[ord(ch) - 97]
            store.add(cur)
        return len(store)
