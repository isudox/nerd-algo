"""301. Remove Invalid Parentheses
https://leetcode.com/problems/remove-invalid-parentheses/

Given a string s that contains parentheses and letters, remove the minimum
number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""


class Solution:
    def remove_invalid_parentheses(self, s: str) -> List[str]:
        def bfs(idx: int, left_cnt: int, right_cnt: int, del_cnt: int, expr: str):
            nonlocal min_del_cnt, expr_set
            if idx == len(s):
                if left_cnt == right_cnt:
                    if del_cnt < min_del_cnt:
                        min_del_cnt = del_cnt
                        expr_set = {expr}
                    elif del_cnt == min_del_cnt:
                        expr_set.add(expr)
            elif s[idx] == '(':
                if del_cnt < min_del_cnt:
                    bfs(idx + 1, left_cnt, right_cnt, del_cnt + 1, expr)
                bfs(idx + 1, left_cnt + 1, right_cnt, del_cnt, expr + '(')
            elif s[idx] == ')':
                if del_cnt < min_del_cnt:
                    bfs(idx + 1, left_cnt, right_cnt, del_cnt + 1, expr)
                if left_cnt > right_cnt:
                    bfs(idx + 1, left_cnt, right_cnt + 1, del_cnt, expr + ')')
            else:
                bfs(idx + 1, left_cnt, right_cnt, del_cnt, expr + s[idx])

        min_del_cnt = len(s)
        expr_set = set()
        bfs(0, 0, 0, 0, '')
        return list(expr_set)
