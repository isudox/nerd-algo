"""752. Open the Lock
https://leetcode.com/problems/open-the-lock/
"""
from typing import List


class Solution:
    mapper = {'0': ['1', '9'],
              '1': ['2', '0'],
              '2': ['3', '1'],
              '3': ['4', '2'],
              '4': ['5', '3'],
              '5': ['6', '4'],
              '6': ['7', '5'],
              '7': ['8', '6'],
              '8': ['9', '7'],
              '9': ['0', '8']}

    def open_lock(self, deadends: List[str], target: str) -> int:
        def next(code: str) -> List[str]:
            ret = []
            for i in range(4):
                for j in range(2):
                    tmp = code[:i] + self.mapper[code[i]][j] + code[i + 1:]
                    if tmp not in visited and tmp not in deadends:
                        ret.append(tmp)
                        visited.add(tmp)
            return ret

        ans = 0
        cur = '0000'
        deadends = set(deadends)
        if cur in deadends:
            return -1
        queue = [cur]
        visited = {cur}
        while queue:
            n = len(queue)
            for i in range(n):
                code = queue.pop(0)
                if code == target:
                    return ans
                next_codes = next(code)
                queue.extend(next_codes)
            ans += 1
        return -1

    def open_lock2(self, deadends: List[str], target: str) -> int:
        def next(code: str) -> List[str]:
            ret = []
            for i in range(4):
                for j in range(2):
                    tmp = code[:i] + self.mapper[code[i]][j] + code[i + 1:]
                    if tmp not in visited1 and tmp not in deadends:
                        ret.append(tmp)
                        visited1.add(tmp)
            return ret

        cur = '0000'
        if cur == target:
            return 0
        deadends = set(deadends)
        if cur in deadends:
            return -1
        queue1 = [cur]
        queue2 = [target]
        visited1 = {cur}
        visited2 = {target}
        ans = 0
        while queue1:
            n = len(queue1)
            for i in range(n):
                code = queue1.pop(0)
                if code in queue2:
                    return ans
                next_codes = next(code)
                queue1.extend(next_codes)
            ans += 1
            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1
                visited1, visited2 = visited2, visited1
        return -1
