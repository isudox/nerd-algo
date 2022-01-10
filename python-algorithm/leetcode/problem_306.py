"""306. Additive Number
https://leetcode.com/problems/additive-number/
"""
import functools


def is_additive_number(num: str) -> bool:
    @functools.lru_cache(None)
    def dfs(x: int, y: int, pos: int) -> bool:
        if pos >= len(num):
            return True
        if num[pos] == '0':
            if x + y != 0:
                return False
            return dfs(0, 0, pos + 1)
        z = str(x + y)
        if len(z) > n - pos:
            return False
        if num[pos:].startswith(z):
            return dfs(y, x + y, pos + len(z))
        return False

    n = len(num)
    for i in range(1, n - 1):
        x = int(num[:i])
        if len(str(x)) != i:
            break
        for j in range(i + 1, n):
            if num[i] == '0':
                if dfs(x, 0, j):
                    return True
                break
            y = int(num[i:j])
            if dfs(x, y, j):
                return True
    return False
