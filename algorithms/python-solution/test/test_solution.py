# -*- coding: utf-8 -*-
import pytest

from solution.palindrome_number import Solution as Palindrome
from solution.three_sum_closest import Solution as ThreeSumClosest


@pytest.mark.parametrize("x, res", [
    (1, True),
    (12, False),
    (333, True),
    (333, True),
])
def test_palindrome_number(x, res):
    solution = Palindrome()
    assert solution.is_palindrome(x) == res


@pytest.mark.parametrize("nums, target, res", [
    ([-1, 2, 1, -4], 1, 2)
])
def test_3sum_closest(nums, target, res):
    solution = ThreeSumClosest()
    assert solution.three_sum_closest(nums, target) == res
