"""1816. Truncate Sentence
https://leetcode.com/problems/truncate-sentence/
"""


def truncate_sentence(self, s: str, k: int) -> str:
    s += ' '
    i = 0
    while k > 0:
        if s[i] == ' ':
            k -= 1
        i += 1
    return s[:i - 1]
