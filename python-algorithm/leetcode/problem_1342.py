"""1342. Number of Steps to Reduce a Number to Zero
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""


def number_of_steps(num: int) -> int:
    ans = 0
    while num:
        num, b = divmod(num, 2)
        if b == 1:
            num = num << 1
        ans += 1
    return ans
