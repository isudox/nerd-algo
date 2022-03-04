"""799. Champagne Tower
https://leetcode.com/problems/champagne-tower/
"""


def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
    tower = [[0] * k for k in range(1, 102)]
    tower[0][0] = poured
    for i in range(query_row + 1):
        for j in range(i + 1):
            x = (tower[i][j] - 1.0) / 2
            if x > 0:
                tower[i + 1][j] += x
                tower[i + 1][j + 1] += x
    return min(1.0, tower[query_row][query_glass])
