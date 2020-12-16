"""738. Monotone Increasing Digits
https://leetcode.com/problems/monotone-increasing-digits/

Given a non-negative integer N, find the largest number that is less than
or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if
each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9

Example 2:
Input: N = 1234
Output: 1234

Example 3:
Input: N = 332
Output: 299

Note: N is an integer in the range [0, 10^9].
"""


class Solution:
    def monotone_increasing_digits(self, n: int) -> int:
        """
        greedy.
        time complexity:
        space complexity:
        """
        str_num = str(n)
        size = len(str_num)
        for i in range(size - 1, 0, -1):
            if str_num[i] < str_num[i - 1]:
                str_num = str_num[:i - 1] + str(int(str_num[i - 1]) - 1) + '9' * (size - i)
        return int(str_num)

