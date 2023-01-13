"""1806. Minimum Number of Operations to Reinitialize a Permutation
https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
"""


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        ans = 0
        perm = list(range(n))
        arr = [0] * n
        while True:
            flag = True
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
                if arr[i] != i:
                    flag = False
            ans += 1
            perm = arr[:]
            if flag:
                break
        return ans
