"""
我们称一个矩阵为黑白矩阵，当且仅当对于该矩阵中每一个位置如(i,j),
其上下左右四个方向的数字相等，即(i-1,j),(i+1,j),(i,j+1),(i,j-1)四个位置上的数字两两相等
且均不等于(i,j)位置上的数字(超出边界的格子忽略)。

现在给出一个 n*m 的矩阵，问最少修改多少个数字,使得该矩阵成为黑白矩阵
"""
from typing import List


class Solution:
    def brute_force(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        nums = []
        for row in matrix:
            for num in row:
                if num not in nums:
                    nums.append(num)
        count = len(nums)
        if count == 0:
            return 0
        if count == 1:
            nums.append(nums[0] + 1)
        least_moves = rows * cols
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                moves_1 = moves_2 = 0
                row_1 = [nums[i if x % 2 == 0 else j] for x in range(cols)]
                row_2 = [nums[i if x % 2 == 1 else j] for x in range(cols)]
                for r in range(rows):
                    temp_1 = [
                        matrix[r][i] - (row_1[i] if r % 2 == 0 else row_2[i])
                        for i in range(cols)]
                    temp_2 = [
                        matrix[r][i] - (row_2[i] if r % 2 == 0 else row_1[i])
                        for i in range(cols)]
                    moves_1 += cols - temp_1.count(0)
                    moves_2 += cols - temp_2.count(0)
                least_moves = min(moves_1, moves_2, least_moves)
        return least_moves

    def least_changes(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = []
        return 0
