from typing import List

import pytest


@pytest.mark.parametrize("d, s, ans", [
    (["looked", "just", "like", "her", "brother"],
     "jesslookedjustliketimherbrother", 7),
])
def test_re_space(d: List[str], s: str, ans: int):
    from other.ctci.re_space import Solution
    sol = Solution()
    assert sol.re_space(d, s) == ans


@pytest.mark.parametrize("maze, ans", [
    (["S#O", "M..", "M.T"], 16),
    (["S#O", "M.#", "M.T"], -1),
    (["S#O", "M.T", "M.."], 17)
])
def test_xun_bao(maze: List[str], ans: int):
    from other.leetcode_cn.xun_bao import Solution
    sol = Solution()
    #assert sol.minimal_steps(maze) == ans


@pytest.mark.parametrize("num, expect", [
    (12258, 5),
    (25, 2),
    (506, 1),
])
def test_lcof(num, expect):
    from other.leetcode_cn.lcof import Solution
    solution = Solution()
    assert solution.translate_num(num) == expect


@pytest.mark.parametrize("matrix, expect", [
    ([
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
     ], 7),
    ([
         [1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]
     ], 4)
])
def test_black_white_matrix(matrix, expect):
    from other.black_white_matrix import Solution
    s = Solution()
    assert s.brute_force(matrix) == expect
