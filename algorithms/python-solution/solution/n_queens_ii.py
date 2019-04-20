"""52. N-Queens II
https://leetcode.com/problems/n-queens-ii/description/


The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens
puzzle.

Example:


Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown
below.
[
[".Q..",  // Solution 1
"...Q",
"Q...",
"..Q."],

["..Q.",  // Solution 2
"Q...",
"...Q",
".Q.."]
]
"""
from typing import List


class Solution:

    def total_n_queens(self, n: int) -> int:
        ans = 0

        def validate(row: int, col: int, queens: List[int]) -> bool:
            """
            Validate current pos[row, col] if is safe.
            :param row: current row.
            :param col: current column.
            :param queens: the columns of previous queens.
            :return:
            """
            for i in range(row):
                cur_queen_col = queens[i]
                if row == i or col == cur_queen_col \
                        or abs(cur_queen_col - col) == abs(i - row):
                    return False
            return True

        def backtrack(row: int, queens: List[int], ):
            """
            Put queen to the safe position of current row.
            :param row: current row.
            :param queens: positions of previous queens.
            :return:
            """
            if row == n:
                nonlocal ans
                ans += 1
                return
            for col in range(n):
                if validate(row, col, queens):
                    backtrack(row + 1, queens + [col])

        for i in range(n):
            backtrack(1, [i])

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.total_n_queens(1))
    print(solution.total_n_queens(2))
    print(solution.total_n_queens(3))
    print(solution.total_n_queens(4))
    print(solution.total_n_queens(5))
    print(solution.total_n_queens(6))
    print(solution.total_n_queens(7))
    print(solution.total_n_queens(8))
    print(solution.total_n_queens(9))
