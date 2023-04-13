"""1380.
"""
from typing import List


def lucky_numbers(matrix: List[List[int]]) -> List[int]:
    ans = []
    for row in matrix:
        pos, minimum = 0, row[0]
        for i, num in enumerate(row):
            if num < minimum:
                minimum = num
                pos = i
        ok = True
        for j in range(len(matrix)):
            if matrix[j][pos] > minimum:
                ok = False
                break
        if ok:
            ans.append(minimum)
    return ans
