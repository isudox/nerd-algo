# -*- coding: utf-8 -*-
"""964. Least Operators to Express Number
https://leetcode.com/problems/least-operators-to-express-number/

Given a single positive integer x, we will write an expression of the form
x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc.
is either addition, subtraction, multiplication, or division (+, -, *, or /).
For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

  The division operator (/) returns rational numbers.
  There are no parentheses placed anywhere.
  We use the usual order of operations: multiplication and division happens
  before addition and subtraction.
  It's not allowed to use the unary negation operator (-).  For example,
  "x - x" is a valid expression as it only uses subtraction, but "-x + x" is
  not because it uses negation.

We would like to write an expression with the least number of operators such
that the expression equals the given target.  Return the least number of
operators used.

Example 1:

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.

Example 2:

Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.

Example 3:

Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.  The expression contains 3 operations.

Note:

2 <= x <= 100
1 <= target <= 2 * 10^8
"""
from functools import lru_cache


class Solution:
    def least_ops_express_target(self, x: 'int', target: 'int') -> 'int':
        if target < x:
            # if x>target, target=x-x/x-x/x... or target=x/x+x/x+x/x
            return min(2 * target - 1, 2 * (x - target))

        cur, ops = x, 0
        while cur < target:
            cur *= x
            ops += 1

        if cur == target:
            return ops

        # if cur > target, step back to the previous x
        left = self.least_ops_express_target(x, target - (cur / x)) - 1
        if cur - target >= target:
            return left + ops + 1
        right = self.least_ops_express_target(x, cur - target)
        return min(left, right) + ops + 1

    # fucking amazing!!!
    def least_ops_express_target_2(self, x: 'int', target: 'int') -> 'int':
        # cost = [2,1,3,4,5,6,...,39]
        cost = list(range(40))
        cost[0] = 2

        @lru_cache(None)
        def dp(i, targ):
            if targ == 0:
                return 0
            if targ == 1:
                return cost[i]
            if i >= 39:
                return float('inf')

            t, r = divmod(targ, x)
            return min(r * cost[i] + dp(i + 1, t),
                       (x - r) * cost[i] + dp(i + 1, t + 1))

        return dp(0, target) - 1
