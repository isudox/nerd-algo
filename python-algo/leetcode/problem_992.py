"""992. Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/

Given an array A of positive integers, call a (contiguous, not necessarily distinct)
subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers:
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers:
[1,2,1,3], [2,1,3], [1,3,4].

Note:

    1 <= A.length <= 20000
    1 <= A[i] <= A.length
    1 <= K <= A.length
"""
from typing import List


class Solution:
    def subarrays_with_k_distinct(self, a: List[int], k: int) -> int:
        def helper(limit: int) -> int:
            i, j, n = 0, 0, len(a)
            visited = [0] * (n + 1)
            count = 0
            ans = 0
            while j < n:
                if visited[a[j]] == 0:
                    count += 1
                visited[a[j]] += 1
                j += 1
                while count > limit:
                    visited[a[i]] -= 1
                    if visited[a[i]] == 0:
                        count -= 1
                    i += 1
                ans += j - i
            return ans

        return helper(k) - helper(k - 1)
