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
