# -*- coding: utf-8 -*-
"""282. Expression Add Operators
https://leetcode.com/problems/expression-add-operators/

Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they evaluate to the target value.

Example 1:

    Input: num = "123", target = 6
    Output: ["1+2+3", "1*2*3"]

Example 2:

    Input: num = "232", target = 8
    Output: ["2*3+2", "2+3*2"]

Example 3:

    Input: num = "105", target = 5
    Output: ["1*0+5","10-5"]

Example 4:

    Input: num = "00", target = 0
    Output: ["0+0", "0-0", "0*0"]

Example 5:

    Input: num = "3456237490", target = 9191
    Output: []
"""
from typing import List

"""
Note that a number can contain multiple digits.
Since the question asks us to find all of the valid expressions, we need a way 
to iterate over all of them. (Hint: Recursion!)
We can keep track of the expression string and evaluate it at the very end. 
But that would take a lot of time. Can we keep track of the expression's value 
as well so as to avoid the evaluation at the very end of recursion?
Think carefully about the multiply operator. It has a higher precedence than 
the addition and subtraction operators.
1 + 2 = 3
1 + 2 - 4 --> 3 - 4 --> -1
1 + 2 - 4 * 12 --> -1 * 12 --> -12 (WRONG!)
1 + 2 - 4 * 12 --> -1 - (-4) + (-4 * 12) --> 3 + (-48) --> -45 (CORRECT!)
We simply need to keep track of the last operand in our expression and reverse
it's effect on the expression's value while considering the multiply operator.
"""


class Solution:
    def add_operators(self, num: str, target: int) -> List[str]:
        result = []
        length = len(num)

        def recurse(start: int, pre_target: int, pre_expr: str):
            if start == length:
                if pre_target == target:
                    result.append(pre_expr)
            for i in range(start + 1, len(num) + 1):
                cur_num = num[start:i]
                if pre_expr[-1] == '+':
                    pre_target += int(cur_num)
                    recurse(i, pre_target, pre_expr + cur_num + '+')
                    recurse(i, pre_target, pre_expr + cur_num + '-')
                    recurse(i, pre_target, pre_expr + cur_num + '*')
                if pre_expr[-1] == '-':
                    pre_target -= int(cur_num)
                    recurse(i, pre_target, pre_expr + cur_num + '+')
                    recurse(i, pre_target, pre_expr + cur_num + '-')
                    recurse(i, pre_target, pre_expr + cur_num + '*')
                if pre_expr[-1] == '*':
                    pass

        return result
