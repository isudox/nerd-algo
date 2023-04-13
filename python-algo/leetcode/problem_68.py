"""68. Text Justification
https://leetcode.com/problems/text-justification
"""
from typing import List


class Solution:
    def full_justify(self, words: List[str], max_width: int) -> List[str]:
        def helper(start: int, end: int, cur_cnt: int) -> str:
            remain_cnt = max_width - cur_cnt - (end - start)
            if end == start:  # only one word
                return words[start] + ' ' * remain_cnt
            spaces = [' '] * (end - start)
            for _ in range(remain_cnt):
                spaces[_ % len(spaces)] += ' '
            ret = ''
            for space in spaces:
                ret += words[start] + space
                start += 1
            ret += words[end]
            return ret

        ans = []
        left, right, cnt = 0, 0, 0
        while right < len(words):
            size = len(words[right])
            if cnt + size + (right - left) > max_width:
                ans.append(helper(left, right - 1, cnt))
                left = right
                cnt = 0
            else:
                cnt += size
                right += 1
        if cnt > 0:  # last line
            last_line = ''
            for i in range(left, right):
                last_line += words[i]
                if i != right - 1:
                    last_line += ' '
            last_line += ' ' * (max_width - len(last_line))
            ans.append(last_line)
        return ans
