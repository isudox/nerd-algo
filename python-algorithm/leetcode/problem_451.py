"""451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/
"""
import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        cnt_list = [0] * (len(s) + 1)
        cnt_value_map = collections.defaultdict(list)
        for char, cnt in counter.items():
            cnt_value_map[cnt].append(char)
            cnt_list[cnt] = 1
        ans = ''
        for cnt in range(len(s), -1, -1):
            if cnt_list[cnt] == 1:
                for char in cnt_value_map[cnt]:
                    ans += char * cnt
        return ans
