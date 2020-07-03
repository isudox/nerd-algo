"""43. Multiply Strings
https://leetcode.com/problems/multiply-strings/description/

Given two non-negative integers num1 and num2 represented as strings, return
the product of num1 and num2, also represented as a string.

Example 1:


Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:


Input: num1 = "123", num2 = "456"
Output: "56088"


Note:


The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0
itself.
You must not use any built-in BigInteger library or convert the inputs to
integer directly.
"""


class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        len3 = len1 + len2
        product = ["0"] * len3
        ans = ""

        for i in range(len1):
            for j in range(len2):
                temp = str(int(num1[i]) * int(num2[j]))
                # how many zeros are after temp
                zeros = len1 - i - 1 + len2 - j - 1
                for k in range(len(temp) - 1, -1, -1):
                    # do the sum from with reverse
                    pos = zeros + (len(temp) - k)
                    temp_sum = int(product[len3 - pos]) + int(temp[k])
                    gte_ten = temp_sum >= 10
                    l = 1

                    while gte_ten:
                        # remind this case, it might be '999...9 + 1'
                        next_sum = int(product[len3 - pos - l]) + 1
                        gte_ten = next_sum >= 10
                        product[len3 - pos - l] = str(next_sum)[-1]
                        l += 1
                    product[len3 - pos] = str(temp_sum)[-1]

        find_first_non_zero = False
        for c in product:
            if c == "0" and not find_first_non_zero:
                continue
            if c != "0":
                find_first_non_zero = True
            ans += c
        if not find_first_non_zero:
            return "0"
        return ans
