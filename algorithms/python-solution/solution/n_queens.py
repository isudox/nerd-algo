"""51. N-Queens
https://leetcode.com/problems/n-queens/description/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

![](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.

Example:


Input: 4
Output: [
⁠[".Q..",  // Solution 1
⁠ "...Q",
⁠ "Q...",
⁠ "..Q."],

⁠["..Q.",  // Solution 2
⁠ "Q...",
⁠ "...Q",
⁠ ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as
shown above.
"""
from typing import List


class Solution:

    def solve_n_queens(self, n: int) -> List[List[str]]:

        ans = []

        def output(pos: int):
            """
            Output the string format of row.
            :param pos: the queen's position in current row.
            :return:
            """
            return "." * pos + "Q" + "." * (n - pos - 1)

        def validate(row: int, col: int, queens: List[int]) -> bool:
            """
            Validate current pos[row, col] if is safe.
            :param row: current row index.
            :param col: current column index.
            :param queens: the columns of previous queens.
            :return:
            """
            for i in range(row):
                cur_queen_col = queens[i]
                if row == i:
                    return False
                if col == cur_queen_col:
                    return False
                if abs(cur_queen_col - col) == abs(i - row):
                    return False
            return True

        def backtrack(row: int, queens: List[int], string: List[str]) -> bool:
            """
            Put queen to the safe position of current row.
            :param row: current row.
            :param queens: positions of previous queens.
            :param string: string format of previous queens
            :return:
            """
            if row == n:
                # all n queens have been put.
                ans.append(string)
                return True

            success = False
            for col in range(n):
                if validate(row, col, queens):
                    next_queen_safe = backtrack(row + 1, queens + [col],
                                                string + [output(col)])
                    if next_queen_safe:
                        success = True

            return success

        for i in range(n):
            backtrack(1, [i], [output(i)])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve_n_queens(1))
    print(solution.solve_n_queens(2))
    print(solution.solve_n_queens(3))
    print(solution.solve_n_queens(4))
    print(solution.solve_n_queens(5))
    print(solution.solve_n_queens(6))
    print(solution.solve_n_queens(7))
    print(solution.solve_n_queens(8))
