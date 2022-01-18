"""1220. Count Vowels Permutation
https://leetcode.com/problems/count-vowels-permutation/
"""


def count_vowel_permutation(n: int) -> int:
    base = int(1e9 + 7)
    dp = [[0] * 5 for _ in range(n + 1)]
    dp[1] = [1, 1, 1, 1, 1]
    for i in range(2, n + 1):
        for j in range(5):
            if j == 0:
                # 'ea', 'ia', 'ua'
                dp[i][j] += dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
                dp[i][j] = dp[i][j] % base
            if j == 1:
                # 'ae', 'ie'
                dp[i][j] += dp[i - 1][0] + dp[i - 1][2]
                dp[i][j] = dp[i][j] % base
            if j == 2:
                # 'ei', 'oi'
                dp[i][j] += dp[i - 1][1] + dp[i - 1][3]
                dp[i][j] = dp[i][j] % base
            if j == 3:
                # 'io'
                dp[i][j] += dp[i - 1][2]
                dp[i][j] = dp[i][j] % base
            if j == 4:
                # 'iu', 'ou'
                dp[i][j] += dp[i - 1][2] + dp[i - 1][3]
                dp[i][j] = dp[i][j] % base
    return sum(dp[-1]) % base
