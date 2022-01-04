"""913. Cat and Mouse
https://leetcode.com/problems/cat-and-mouse/
"""
from typing import List


def cat_mouse_game(graph: List[List[int]]) -> int:
    def dfs(x: int, y: int, turn: int) -> int:
        if turn >= 2 * n:
            return 0
        ret = memo[x][y][turn]
        if ret > -1:
            return ret
        if x == 0:
            return 1
        if x == y:
            return 2
        move_mouse = True if turn % 2 == 0 else False
        cur_pos = x if move_mouse else y
        ret = default_ret = 2 if move_mouse else 1
        for z in graph[cur_pos]:
            if not move_mouse and z == 0:
                continue
            next_x = z if move_mouse else x
            next_y = y if move_mouse else z
            next_ret = dfs(next_x, next_y, turn + 1)
            if next_ret != default_ret:
                ret = next_ret
                if ret != 0:
                    break
        memo[x][y][turn] = ret
        return ret

    n = len(graph)
    memo = [[[-1] * (n * 2) for _ in range(n)] for _ in range(n)]
    return dfs(1, 2, 0)


if __name__ == '__main__':
    print(
        cat_mouse_game([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))
    print(cat_mouse_game([[1, 3], [0], [3], [0, 2]]))
