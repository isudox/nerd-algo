"""402. Remove K Digits
https://leetcode.com/problems/remove-k-digits/

Given a non-negative integer num represented as a string,remove k digits
from the number so that the new number is the smallest possible.

Note:

    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output
must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


class Solution:
    def remove_k_digits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        n = len(num)
        if n == k:
            return '0'
        ans = 0
        # pick (n-k) number, make it minimum.
        left, right, count = 0, k, 0
        while True:
            cur = '9'
            i, j = left, left
            while i <= right:
                if num[i] < cur:
                    cur = num[i]
                    j = i
                i += 1
            ans = 10 * ans + int(cur)
            count += 1
            if count == n - k:
                break
            left, right = j + 1, right + 1
        return str(ans)

    def remove_k_digits_2(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return '0'
        count = 0
        while count < k:
            i = 0
            while i < len(num) - 1 and num[i] <= num[i + 1]:
                i += 1
            num = num[:i] + num[i + 1:]
            count += 1
        return str(int(num))

    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return '0'
        m = n - k
        ans = ''
        pos = 0
        while k > 0 and len(ans) < m:
            min_num = num[pos]
            min_pos = pos
            for i in range(pos, pos + k + 1):
                if num[i] < min_num:
                    min_num = num[i]
                    min_pos = i
            ans += min_num
            k -= min_pos - pos
            pos = min_pos + 1

        if len(ans) < m:
            ans += num[pos:]
        i = 0
        while i < len(ans) and ans[i] == '0':
            i += 1
        ans = ans[i:]
        return ans if ans != '' else '0'
