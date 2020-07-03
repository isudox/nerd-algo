"""

"""
from typing import List


class Solution:
    def find_substring(self, s: str, words: List[str]) -> List[int]:
        def is_valid(start: int, end: int, word_list: List[str], length: int) -> bool:
            l = []
            for i in range((end - start) // length):
                string = s[start + i * length:start + (i + 1) * length]
                l.append(string)
            for word in word_list:
                if word in l:
                    l.remove(word)
                else:
                    return False
            return True

        result = []
        if len(words) == 0:
            return result
        length = len(words[0])
        s_len = len(s)
        if length > s_len:
            return result
        words_len = length * len(words)
        for i in range(s_len - words_len + 1):
            word = s[i:i + length]
            if word in words:
                if is_valid(i, i + words_len, words, length):
                    result.append(i)
        return result
