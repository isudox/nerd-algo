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

Constraints:

0 <= num.length <= 10
num only contain digits.
"""
from typing import List

"""
Hints:
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
        ans = []

        def backtrack(store: List[str], i: int, res: int, mul: int):
            if i == len(num):
                if res == target:
                    ans.append(''.join(store))
                return
            size = len(store)
            if i > 0:
                store.append('')
            val = 0
            for j in range(i, len(num)):
                if j > i and num[i] == '0':
                    break
                val = val * 10 + int(num[j])
                store.append(num[j])
                if i == 0:
                    backtrack(store, j + 1, val, val)
                else:
                    store[size] = '+'
                    backtrack(store, j + 1, res + val, val)
                    store[size] = '-'
                    backtrack(store, j + 1, res - val, -val)
                    store[size] = '*'
                    backtrack(store, j + 1, res - mul + mul * val, mul * val)
            del store[size:]
        
        backtrack([], 0, 0, 0)
        return ans