"""1738. Find Kth Largest XOR Coordinate Value
https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

You are given a 2D matrix of size m x n, consisting of non-negative integers.
You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j]
where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the k^th largest value (1-indexed) of all the coordinates of matrix.

Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the
largest value.

Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest
value.

Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd
largest value.

Example 4:

Input: matrix = [[5,2],[1,6]], k = 4
Output: 0
Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which
is the 4th largest value.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 10^6
1 <= k <= m * n
"""
from typing import List
import heapq


class Solution:
    def kth_largest_value(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre_xor = [[0] for _ in range(m)]
        store = []
        heapq.heapify(store)
        for i in range(m):
            for j in range(n):
                cur = pre_xor[i][-1] ^ matrix[i][j]
                if i > 0:
                    cur ^= pre_xor[i - 1][j + 1] ^ pre_xor[i - 1][j]
                pre_xor[i].append(cur)
                heapq.heappush(store, cur)
        return heapq.nlargest(k, store)[-1]

    def kth_largest_value2(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre_xor, cur_xor = [0] * (n + 1), [0] * (n + 1)
        store = []
        heapq.heapify(store)
        for i in range(m):
            for j in range(n):
                cur_xor[j + 1] = cur_xor[j] ^ matrix[i][j] ^ pre_xor[j + 1] ^ pre_xor[j]
                if len(store) < k:
                    heapq.heappush(store, cur_xor[j + 1])
                elif cur_xor[j + 1] > store[0]:
                    heapq.heappop(store)
                    heapq.heappush(store, cur_xor[j + 1])
            pre_xor, cur_xor = cur_xor, [0] * (n + 1)
        return store[0]
