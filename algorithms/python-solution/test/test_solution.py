# -*- coding: utf-8 -*-
import pytest

from solution.palindrome_number import Solution as Palindrome
from solution.three_sum_closest import Solution as ThreeSumClosest
from solution.string_without_3a3b import Solution as StringWithout3a3b


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


@pytest.mark.parametrize("a, b, res", [
    (1, 1, "ab"),
    (1, 4, "bbabb")
])
def test_str_without_3a3b(a, b, res):
    solution = StringWithout3a3b()
    assert solution.strWithout3a3b(a, b) == res
