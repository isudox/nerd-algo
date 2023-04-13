"""1510. Stone Game IV
https://leetcode.com/problems/stone-game-iv/
"""
import math


def winner_square_game(n: int) -> bool:
    if n == 1:
        return True
    dp = [False] * (n + 1)
    dp[1] = True
    dp[2] = False
    for i in range(3, n + 1):
        x = int(math.sqrt(i))
        if x * x == i:
            dp[i] = True
            continue
        for j in range(1, x + 1):
            if not dp[i - j * j]:
                dp[i] = True
                break
    return dp[n]
