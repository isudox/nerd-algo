"""1286. Iterator for Combination
https://leetcode.com/problems/iterator-for-combination/
"""


class CombinationIterator:

    def __init__(self, characters: str, length: int):
        self.characters = characters
        self.n = length
        self.cur = ""
        self.index = dict()
        for idx, ch in enumerate(characters):
            self.index[ch] = idx

    def next(self) -> str:
        if self.cur == "":
            self.cur = self.characters[:self.n]
        else:
            for i in range(self.n - 1, -1, -1):
                ch = self.cur[i]
                idx = self.index[ch]
                if idx == len(self.characters) - 1 - (self.n - 1 - i):
                    continue
                self.cur = self.cur[:i] + self.characters[idx + 1:idx + 1 + (self.n - i)]
                break
        return self.cur

    def hasNext(self) -> bool:
        return self.cur != self.characters[len(self.characters) - self.n:]
