"""2047. Number of Valid Words in a Sentence
https://leetcode.com/problems/number-of-valid-words-in-a-sentence/
"""


def count_valid_words(sentence: str) -> int:
    def helper(w: str) -> bool:
        if w == '':
            return False
        cnt_ = 0
        cnt_sig = 0
        for i, ch in enumerate(w):
            if not ('a' <= ch <= 'z' or ch in {'-', '!', '.', ','}):
                return False
            if ch == '-':
                cnt_ += 1
                if cnt_ > 1:
                    return False
                if i == 0 or i == len(w) - 1:
                    return False
                if w[i - 1] < 'a' or w[i - 1] > 'z' or w[i + 1] < 'a' or w[i + 1] > 'z':
                    return False
            elif ch in {'!', '.', ','}:
                cnt_sig += 1
                if cnt_sig > 1:
                    return False
                if i != len(w) - 1:
                    return False
        return True

    words = sentence.split(' ')
    ans = 0
    for word in words:
        if helper(word):
            ans += 1
    return ans
