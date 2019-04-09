# -*- coding: utf-8 -*-
import pytest

from util.converter import Converter


@pytest.mark.parametrize("x, res", [
    (1, True),
    (12, False),
    (333, True),
    (333, True)
])
def test_palindrome_number(x, res):
    from solution.palindrome_number import Solution

    assert Solution().is_palindrome(x) == res


@pytest.mark.parametrize("nums, target, res", [([-1, 2, 1, -4], 1, 2)])
def test_3sum_closest(nums, target, res):
    from solution.three_sum_closest import Solution

    assert Solution().three_sum_closest(nums, target) == res


@pytest.mark.parametrize("a, b, res", [(1, 1, "ab"), (1, 4, "bbabb")])
def test_str_without_3a3b(a, b, res):
    from solution.string_without_3a3b import Solution

    assert Solution().str_without_3a3b(a, b) == res


@pytest.mark.parametrize(
    "days, costs, res",
    [
        ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
    ],
)
def test_minimum_cost_for_tickets(days, costs, res):
    from solution.minimum_cost_for_tickets import Solution

    assert Solution().min_cost_tickets(days, costs) == res


@pytest.mark.parametrize(
    "root, res",
    [([3, 0, 0], 2), ([0, 3, 0], 3), ([1, 0, 2], 2), ([1, 0, 0, None, 3], 4)],
)
def test_distribute_coins_in_binary_tree(root, res):
    from solution.distribute_coins_in_binary_tree import Solution

    assert Solution().distribute_coins(Converter.list_to_tree(root)) == res


def test_time_based_key_value_store():
    from solution.time_based_key_value_store import TimeMap

    time_map = TimeMap()
    time_map.set("name", "isudox", 1000)
    assert time_map.get("name", 1000) == "isudox"


@pytest.mark.parametrize(
    "li, res",
    [
        ([0, 1, 1, 0, 1, 0, 1, 1, 0, 0], 5),
        ([9, 4, 2, 10, 7, 8, 8, 1, 9], 5),
        ([4, 8, 12, 16], 2),
        ([1, 5, 3], 3),
        ([1, 1, 1], 1),
        ([1, 1], 1),
        ([100], 1),
    ],
)
def test_longest_turbulent_subarray(li, res):
    from solution.longest_turbulent_subarray import Solution

    assert Solution().max_turbulence_size(li) == res


@pytest.mark.parametrize("nums, res", [([2, 1, 3], 12)])
def test_triples_with_bitwise_and_equal_to_zero(nums, res):
    from solution.triples_with_bitwise_and_equal_to_zero import Solution

    assert Solution().count_triplets(nums) == res


@pytest.mark.parametrize(
    "grid, res",
    [
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4),
        ([[0, 1], [2, 0]], 0),
    ],
)
def test_unique_paths_3(grid, res):
    from solution.unique_paths_iii import Solution

    assert Solution().unique_paths_iii(grid) == res


@pytest.mark.parametrize(
    "x, y, bound, res",
    [(2, 3, 10, [2, 3, 4, 5, 7, 9, 10]), (3, 5, 15, [2, 4, 6, 8, 10, 14])],
)
def test_powerful_integers(x, y, bound, res):
    from solution.powerful_integers import Solution

    assert Solution().powerful_integers(x, y, bound) == res


@pytest.mark.parametrize(
    "a, res",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_sorted_squares(a, res):
    from solution.squares_of_a_sorted_array import Solution

    assert Solution().sorted_squares(a) == res


@pytest.mark.parametrize(
    "a, res",
    [([2, 1, 2], 5), ([1, 2, 1], 0), ([3, 2, 3, 4], 10), ([3, 6, 2, 3], 8)]
)
def test_largest_perimeter(a, res):
    from solution.largest_perimeter_triangle import Solution

    assert Solution().largest_perimeter(a) == res


@pytest.mark.parametrize("arr, k, res", [([4, 5, 0, -2, -3, 1], 5, 7)])
def test_subarray_sums_divisible_by_k(arr, k, res):
    from solution.subarray_sums_divisible_by_k import Solution

    assert Solution().subarrays_div_by_k(arr, k) == res


@pytest.mark.parametrize(
    "s, t, res",
    [
        ("0.(52)", "0.5(25)", True),
        ("0.1666(6)", "0.166(66)", True),
        ("0.9(9)", "1.", True),
        ("0.12", "0.12(1)", False),
    ],
)
def test_equal_rational_numbers(s, t, res):
    from solution.equal_rational_numbers import Solution

    assert Solution().is_rational_equal(s, t) == res


@pytest.mark.parametrize(
    "points, k, res",
    [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ],
)
def test_k_closest_points_to_origin(points, k, res):
    from solution.k_closest_points_to_origin import Solution

    assert Solution().k_closest_2(points, k) == res


@pytest.mark.parametrize(
    "nums, res", [([3, 2, 4, 1], [3, 4, 2, 3, 2]), ([1, 2, 3], [])]
)
def test_pancake_sorting(nums, res):
    from solution.pancake_sorting import Solution

    assert Solution().pancake_sort(nums) == res


@pytest.mark.parametrize(
    "x, target, ans", [(3, 19, 5), (5, 501, 8), (100, 200000000, 7)]
)
def test_least_operators_to_express_number(x, target, ans):
    from solution.least_operators_to_express_number import Solution

    assert Solution().least_ops_express_target(x, target) == ans
    assert Solution().least_ops_express_target_2(x, target) == ans


@pytest.mark.parametrize(
    "points, area",
    [
        ([[1, 2], [2, 1], [1, 0], [0, 1]], 2.00000),
        ([[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]], 1.00000),
        ([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]], 0.00000),
    ],
)
def test_min_area_rect(points, area):
    from solution.minimum_area_rectangle_ii import Solution

    assert Solution().min_area_free_rect(points) == area


@pytest.mark.parametrize(
    "li, ans",
    [([1, 2, 3, 3], 3), ([2, 1, 2, 5, 3, 2], 2), ([5, 1, 5, 2, 5, 3, 5, 4], 5)],
)
def test_n_repeated_element_in_size_2n_array(li, ans):
    from solution.n_repeated_element_in_size_2n_array import Solution

    assert Solution().repeated_n_times(li) == ans
    assert Solution().ans(li) == ans
    assert Solution().ans_2(li) == ans


@pytest.mark.parametrize(
    "arr, ans", [([6, 0, 8, 2, 1, 5], 4), ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7)]
)
def test_maximum_width_ramp(arr, ans):
    from solution.maximum_width_ramp import Solution

    assert Solution().max_width_ramp(arr) == ans


@pytest.mark.parametrize(
    "arr, ans",
    [
        (["cba", "daf", "ghi"], 1),
        (["zyx", "wvu", "tsr"], 3),
        (["a", "b"], 0),
        (["rrjk", "furt", "guzm"], 2),
    ],
)
def test_delete_columns_to_make_sorted(arr, ans):
    from solution.delete_columns_to_make_sorted import Solution

    assert Solution().min_deletion_size(arr) == ans
    assert Solution().ans(arr) == ans


@pytest.mark.parametrize("arr, ans", [
    (["ca", "bb", "ac"], 1),
    (["xc", "yb", "za"], 0),
    (["zyx", "wvu", "tsr"], 3),
    (["xga", "xfb", "yfa"], 1),
],
                         )
def test_delete_columns_to_make_sorted_ii(arr, ans):
    from solution.delete_columns_to_make_sorted_ii import Solution

    assert Solution().min_deletion_size(arr) == ans


@pytest.mark.parametrize("arr, ans", [
    (["babca", "bbazb"], 3),
    (["edcba"], 4),
    (["ghi", "def", "abc"], 0)
])
def test_delete_columns_to_make_sorted_iii(arr, ans):
    from solution.delete_columns_to_make_sorted_iii import Solution

    assert Solution().min_deletion_size(arr) == ans


@pytest.mark.parametrize("pushed, popped, ans", [
    ([], [], True),
    ([1, 2], [1, 2, 3], False),
    ([2, 1, 0], [1, 2, 0], True),
    ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
    ([2, 3, 0, 1], [0, 3, 2, 1], True)
])
def test_validate_stack_sequences(pushed, popped, ans):
    from solution.validate_stack_sequences import Solution

    solution = Solution()
    assert solution.validate_stack_sequences(pushed, popped) == ans
    assert solution.ans(pushed, popped) == ans


@pytest.mark.parametrize("n, k, expect", [
    (1, 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (1, 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (1, 2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (1, 3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (1, 5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (3, 7, [181, 292, 707, 818, 929]),
    (2, 1,
     [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
    (4, 1,
     [1010, 1012, 1210, 1212, 1232, 1234, 2101, 2121, 2123, 2321, 2323, 2343,
      2345, 3210, 3212, 3232, 3234, 3432, 3434, 3454, 3456, 4321, 4323, 4343,
      4345, 4543, 4545, 4565, 4567, 5432, 5434, 5454, 5456, 5654, 5656, 5676,
      5678, 6543, 6545, 6565, 6567, 6765, 6767, 6787, 6789, 7654, 7656, 7676,
      7678, 7876, 7878, 7898, 8765, 8767, 8787, 8789, 8987, 8989, 9876, 9878,
      9898])
])
def test_nums_same_consec_diff(n, k, expect):
    from solution.numbers_with_same_consecutive_differences import Solution

    ans = Solution().nums_same_consec_diff(n, k)
    assert len(ans) == len(expect)
    for num in ans:
        if num in expect:
            expect.remove(num)
    assert len(expect) == 0


@pytest.mark.parametrize("s, t, ans", [
    ("cba", "abcd", "cbad"),
    ("abc", "badef", "abdef"),
    ("", "abc", "abc"),
    ("def", "cba", "cba"),
    ("kqep", "pekeq", "kqeep")
])
def test_custom_sort_string(s, t, ans):
    from solution.custom_sort_string import Solution

    assert Solution().custom_sort_string(s, t) == ans


@pytest.mark.parametrize("grid, ans", [
    ([
         " /",
         "/ "
     ], 2),
    ([
         " /",
         "  "
     ], 1),
    ([
         "\\/",
         "/\\"
     ], 4),
    ([
         "/\\",
         "\\/"
     ], 5),
    ([
         "//",
         "/ "
     ], 3)
])
def test_regions_cut_by_slashes(grid, ans):
    pass

    # assert Solution().regions_by_slashes(grid) == ans


@pytest.mark.parametrize("nums, ans", [
    ([2, 1, 2], 1),
    ([1], 1),
    ([4, 3, 5, 3, 4], 5)
])
def test_single_number(nums, ans):
    from solution.single_number import Solution
    solution = Solution()

    assert solution.single_number(nums) == ans
    assert solution.reduce_func(nums) == ans


@pytest.mark.parametrize("candidates, target, expect", [
    ([2, 3, 6, 7], 7, [
        [2, 2, 3],
        [7]
    ]),
    ([2, 3, 5], 8, [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5]
    ]),
    ([3, 4, 5], 1, []),
    ([1, 3], 1, [[1]])
])
def test_combination_sum(candidates, target, expect):
    from solution.combination_sum import Solution
    solution = Solution()

    assert solution.combination_sum(candidates, target) == expect


@pytest.mark.parametrize("candidates, target, expect", [
    ([10, 1, 2, 7, 6, 1, 5], 8, [
        [1, 1, 6], [1, 2, 5], [1, 7], [2, 6]
    ]),
    ([2, 5, 2, 1, 2], 5, [
        [1, 2, 2], [5]
    ]),
])
def test_combination_sum_2(candidates, target, expect):
    from solution.combination_sum_ii import Solution
    solution = Solution()

    assert solution.combination_sum2(candidates, target) == expect


@pytest.mark.parametrize("n, k, expect", [
    (2, 6, [
        [1, 5], [2, 4]
    ]),
    (3, 7, [
        [1, 2, 4]
    ]),
    (3, 9, [
        [1, 2, 6], [1, 3, 5], [2, 3, 4]
    ]),
    (5, 18, [
        [1, 2, 3, 4, 8], [1, 2, 3, 5, 7], [1, 2, 4, 5, 6]
    ])
])
def test_combination_sum_3(n, k, expect):
    from solution.combination_sum_iii import Solution
    solution = Solution()

    assert solution.combination_sum3(n, k) == expect


@pytest.mark.parametrize("nums, target, expect", [
    ([1, 2, 3], 4, 7),
    ([4, 2, 1], 32, 39882198)
])
def test_combination_sum_4(nums, target, expect):
    from solution.combination_sum_iv import Solution
    solution = Solution()

    assert solution.combination_sum4(nums, target) == expect


@pytest.mark.parametrize("nums, expect", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1, 2, 3, 4, 5], 15)
])
def test_maximum_subarray(nums, expect):
    from solution.maximum_subarray import Solution
    solution = Solution()

    assert solution.max_sub_array(nums) == expect
