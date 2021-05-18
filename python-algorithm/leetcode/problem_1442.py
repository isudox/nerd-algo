"""1442. Count Triplets That Can Form Two Arrays of Equal XOR
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

Given an array of integers arr.

We want to select three indices i, j and k where
(0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:

Input: arr = [1,1,1,1,1]
Output: 10

Example 3:

Input: arr = [2,3]
Output: 0

Example 4:

Input: arr = [1,3,5,7,9]
Output: 3

Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 10^8
"""
from typing import List
from collections import Counter


class Solution:
    def count_triplets(self, arr: List[int]) -> int:
        pre_xor = [0]
        for num in arr:
            pre_xor.append(pre_xor[-1] ^ num)
        ans = 0
        for i in range(len(arr)):
            for k in range(i + 1, len(arr)):
                if pre_xor[i] == pre_xor[k + 1]:
                    ans += k - i
        return ans

    def count_triplets2(self, arr: List[int]) -> int:
        pre_xor = [0]
        for num in arr:
            pre_xor.append(pre_xor[-1] ^ num)
        ans = 0
        cnt, total = Counter(), Counter()
        for k in range(len(arr)):
            if pre_xor[k + 1] in cnt:
                ans += cnt[pre_xor[k + 1]] * k - total[pre_xor[k + 1]]
            cnt[pre_xor[k]] += 1
            total[pre_xor[k]] += k
        return ans
