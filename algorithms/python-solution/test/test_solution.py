# -*- coding: utf-8 -*-
import pytest

from util.converter import Converter


@pytest.mark.parametrize("x, res", [
    (1, True),
    (12, False),
    (333, True),
    (333, True),
])
def test_palindrome_number(x, res):
    from solution.palindrome_number import Solution
    assert Solution().is_palindrome(x) == res


@pytest.mark.parametrize("nums, target, res", [
    ([-1, 2, 1, -4], 1, 2)
])
def test_3sum_closest(nums, target, res):
    from solution.three_sum_closest import Solution
    assert Solution().three_sum_closest(nums, target) == res


@pytest.mark.parametrize("a, b, res", [
    (1, 1, "ab"),
    (1, 4, "bbabb")
])
def test_str_without_3a3b(a, b, res):
    from solution.string_without_3a3b import Solution
    assert Solution().strWithout3a3b(a, b) == res


@pytest.mark.parametrize("days, costs, res", [
    ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17)
])
def test_minimum_cost_for_tickets(days, costs, res):
    from solution.minimum_cost_for_tickets import Solution
    assert Solution().min_cost_tickets(days, costs) == res


@pytest.mark.parametrize("root, res", [
    ([3, 0, 0], 2),
    ([0, 3, 0], 3),
    ([1, 0, 2], 2),
    ([1, 0, 0, None, 3], 4)
])
def test_distribute_coins_in_binary_tree(root, res):
    from solution.distribute_coins_in_binary_tree import Solution
    assert Solution().distribute_coins(Converter.list_to_tree(root)) == res


def test_time_based_key_value_store():
    from solution.time_based_key_value_store import TimeMap
    time_map = TimeMap()
    time_map.set("name", "isudox", 1000)
    assert time_map.get("name", 1000) == "isudox"
