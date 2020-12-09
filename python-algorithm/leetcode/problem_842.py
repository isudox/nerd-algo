"""842. Split Array into Fibonacci Sequence
https://leetcode.com/problems/split-array-into-fibonacci-sequence/

Given a string S of digits, such as S = "123456579", we can split it into
a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces,each piece must not
have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]

Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]

Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.

Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:

1 <= S.length <= 200
S contains only digits.
"""
from typing import List


class Solution:
    def split_into_fibonacci(self, s: str) -> List[int]:
        def backtrack(prev: List[int], idx: int) -> bool:
            if idx == n:
                return True
            target = prev[-1] + prev[-2]
            if target > max_int:
                return False
            size = len(str(target))
            if n - idx < size:
                return False
            if str(target) != s[idx: idx + size]:
                return False
            prev.append(target)
            return backtrack(prev, idx + size)

        n = len(s)
        if n < 3:
            return []
        max_int = 2 ** 31 - 1
        i_end = 2 if s[0] == '0' else n - 1
        for i in range(1, i_end):
            num1 = int(s[:i])
            if num1 > max_int:
                break
            for j in range(i + 1, n):
                num2 = int(s[i:j])
                if num2 > max_int:
                    break
                ans = [num1, num2]
                if backtrack(ans, j):
                    return ans
                if ans[1] == '0':
                    break
        return []
