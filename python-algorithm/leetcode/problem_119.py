"""119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Constraints:

0 <= rowIndex <= 33
"""
from typing import List


class Solution:
    def get_row(self, row_index: int) -> List[int]:
        if row_index == 0:
            return [1]
        if row_index == 1:
            return [1, 1]
        ans = [1]
        pre_ans = self.get_row(row_index - 1)
        for i in range(row_index - 1):
            ans.append(pre_ans[i] + pre_ans[i + 1])
        ans.append(1)
        return ans

    def get_row_2(self, row_index: int) -> List[int]:
        if row_index == 0:
            return [1]
        if row_index == 1:
            return [1, 1]
        ans = [0] * (row_index + 1)
        for i in range(1, row_index + 1):
            ans[0] = ans[i] = 1
            for j in range(i - 1, 0, -1):
                ans[j] = ans[j] + ans[j - 1]
        return ans
