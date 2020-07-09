from typing import List

import pytest


@pytest.mark.parametrize("d, s, ans", [
    (["looked", "just", "like", "her", "brother"], "jesslookedjustliketimherbrother", 7),
])
def test_re_space(d: List[str], s: str, ans: int):
    from other.ctci.re_space import Solution
    sol = Solution()
    assert sol.re_space(d, s) == ans
