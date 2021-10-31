"""500. Keyboard Row
https://leetcode.com/problems/keyboard-row/
"""
from typing import List


class Solution:
    def find_words(self, words: List[str]) -> List[str]:
        keyboards = [
            {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
            {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm'}]
        ans = []
        for word in words:
            lower_word = word.lower()
            line = -1
            flag = True
            for ch in lower_word:
                for i, keyboard in enumerate(keyboards):
                    if ch in keyboard:
                        if line == -1:
                            line = i
                        elif line != i:
                            flag = False
                            break
                if not flag:
                    break
            if flag:
                ans.append(word)
        return ans
