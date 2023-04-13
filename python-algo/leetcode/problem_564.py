"""564. Find the Closest Palindrome
https://leetcode.com/problems/find-the-closest-palindrome/
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]
        selfPrefix = int(n[:(m + 1) // 2])
        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)

        ans = -1
        selfNumber = int(n)
        for candidate in candidates:
            if candidate != selfNumber:
                if ans == -1 or \
                    abs(candidate - selfNumber) < abs(ans - selfNumber) or \
                    abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans:
                    ans = candidate
        return str(ans)
