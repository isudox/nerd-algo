"""338. Counting Bits
https://leetcode.com/problems/counting-bits/

Given a non negative integer number num. For every numbers i in the range
0 ≤ i ≤ num calculate the number of 1's in their binary representation and
return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like
__builtin_popcount in c++ or in any other language.
"""
from typing import List


class Solution:
    def count_bits(self, num: int) -> List[int]:
        """
        time complexity:
        space complexity:
        """
        binary, n = 1, 0
        while binary <= num:
            binary *= 2
            n += 1
        binary /= 2
        n -= 1
        ans = [0]
        for i in range(1, n + 1):
            temp = [x + 1 for x in ans]
            ans.extend(temp)
        idx = 0
        temp = []
        while binary <= num:
            temp.append(ans[idx] + 1)
            binary += 1
            idx += 1
        ans.extend(temp)
        return ans

    def count_bits_2(self, num: int) -> List[int]:
        ans = [0]
        step = 1
        while len(ans) < num + 1:
            n = min(step, num + 1 - len(ans))
            for i in range(n):
                ans.append(ans[i] + 1)
            step *= 2
        return ans
