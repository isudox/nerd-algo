from collections import Counter
from typing import List
from sortedcontainers import SortedList


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def get_key(cnt) -> str:
            ret = ''
            for i in range(26):
                ch = chr(97 + i)
                if cnt[ch]:
                    ret += ch + str(cnt[ch])
            return ret

        store = {}
        for word in words:
            counter = Counter(word)
            store[word] = get_key(counter)
        stack = []
        for i, word in enumerate(words):
            if not stack:
                stack.append(word)
                continue
            pre_key = store[stack[-1]]
            cur_key = store[word]
            if pre_key == cur_key:
                continue
            else:
                stack.append(word)
        return stack

    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        ans = 0
        special.sort()
        for i in range(len(special) - 1):
            tmp = special[i + 1] - special[i] - 1
            if tmp > ans:
                ans = tmp
        left = special[0] - bottom
        right = top - special[-1]
        ans = max(ans, left, right)
        return ans

    def largestCombination(self, candidates: List[int]) -> int:
        def helper(x: int) -> bool:
            for i in range(25):
                cnt1 = 0
                for num in candidates:
                    bit = (num >> i) & 1
                    if bit == 1:
                        cnt1 += 1
                        if cnt1 >= x:
                            return True
            return False

        lo, hi = 1, len(candidates),
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if helper(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo


class CountIntervals:
    def __init__(self):
        self.segments = SortedList()
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        k = self.segments.bisect_left((left, right))
        while k < len(self.segments) and self.segments[k][0] <= right:
            l, r = self.segments.pop(k)
            self.cnt -= r - l + 1
            right = max(right, r)
        if k and left <= self.segments[k - 1][1]:
            l, r = self.segments.pop(k - 1)
            self.cnt -= r - l + 1
            left = l
            right = max(right, r)
        self.cnt += right - left + 1
        self.segments.add((left, right))

    def count(self) -> int:
        return self.cnt
