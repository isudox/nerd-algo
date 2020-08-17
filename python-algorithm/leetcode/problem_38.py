"""38. Count and Say
https://leetcode.com/problems/count-and-say/description/

The count-and-say sequence is the sequence of integers with the first five
terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a
string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""


class Solution:
    def count_and_say(self, n: int) -> str:
        assert 1 <= n <= 30

        if n == 1:
            return "1"

        def say(num_str: str) -> str:
            res = ""
            cur_digit = num_str[0]
            cur_digit_count = 1
            for i in range(1, len(num_str)):
                if num_str[i] == cur_digit:
                    cur_digit_count += 1
                else:
                    res += str(cur_digit_count) + cur_digit
                    cur_digit = num_str[i]
                    cur_digit_count = 1
            res += str(cur_digit_count) + cur_digit
            return res

        ans = "1"
        for i in range(1, n):
            ans = say(ans)

        return ans
