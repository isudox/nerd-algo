"""2337. Move Pieces to Obtain a String

"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def helper(s: str) -> str:
            ret = ''
            for c in s:
                if c != '_':
                    ret += c
            return ret

        if helper(start) != helper(target):
            return False
        j = 0
        n = len(start)
        for i in range(n):
            if start[i] == '_':
                continue
            while target[j] == '_':
                j += 1
            if i < j and start[i] == 'L':
                return False
            if i > j and j < n and target[j] == 'R':
                return False
            j += 1
        return True
