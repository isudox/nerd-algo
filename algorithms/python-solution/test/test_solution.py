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
    # ([4, 2, 1], 32, 39882198)
])
def test_combination_sum_4(nums, target, expect):
    from solution.combination_sum_iv import Solution
    solution = Solution()

    assert solution.combination_sum4(nums, target) == expect


@pytest.mark.parametrize("nums, expect", [
    ([-1], -1),
    ([-2, -1], -1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1, 2, 3, 4, 5], 15),
    ([-64, 78, 56, 10, -8, 26, -18, 47, -31, 75, 89, 13, 48, -19, -69, 36, -39,
      55, -5, -4, -15, -37, -27, -8, -5, 35, -51, 83, 21, -47, 46, 33, -91, -21,
      -57, 0, 81, 1, -75, -50, -23, -86, 39, -98, -29, 69, 38, 32, 24, -90, -95,
      86, -27, -23, -22, 44, -88, 3, 27, 9, 55, -50, -80, 40, 5, -61, -82, -14,
      40, -58, 35, 93, -68, -26, 94, 3, -79, 9, -88, 21, 19, -84, 7, 91, -8, 84,
      12, -19, -13, -83, 66, -80, -34, 62, 59, 48, -98, 53, -66, 18, 94, 46, 11,
      -73, 96, -18, 6, -83, 91, 17, 38, 10, 9, -78, -22, 77, 83, 89, -42, -30,
      -94, -98, -34, -51, 63, -97, 96, 64, 55, -93, -41, 27, 52, 69, 53, 26,
      -71, -64, 42, -80, 52, -43, 6, -62, -21, 83, -85, -38, 49, -50, 8, 55,
      -72, 74, 80, 90, 53, 53, 32, -15, 36, 90, -88, -34, 37, 41, 91, 65, 76,
      33, 61, 5, 90, -33, 42, -54, -73, 34, -16, 75, 83, 91, 7, -89, 42, -36,
      77, -5, -83, 9, 80, 53, -23, 68, -81, 90, 10, -90, 55, -14, 19, -7, 91,
      -14, 59, 33, 31, 62, -33, -85, 37, -73, 83, -78, -86, 25, -15, 91, 97, 2,
      -23, 54, -68, 53, 22, -73, 43, -68, -87, -25, 18, 31, 67, -14, 94, 3, -81,
      25, -35, -37, 17, 79, -34, -23, -99, -43, -98, -38, -52, 75, 63, 1, 29,
      71, -68, -71, 74, 51, -40, 86, -73, 54, -5, 70, -60, -11, -49, -64, 90,
      -8, -25, -16, -52, 40, 60, -75, 96, 39, -13, -79, 14, -73, 22, -79, 75,
      30, -51, 49, -19, -15, 36, -16, -60, -69, -68, -21, -4, -18, -9, -14, 50,
      65, 70, 75, -17, 30, 99, -44, -31, -14, -46, 60, -10, 52, 80, -35, -18,
      -94, -86, 62, -10, 49, -53, 6, 56, -45, 62, -48, 36, -47, 15, -37, -81,
      -15, -62, -22, 91, -85, 33, -62, -23, 86, 97, 66, 15, 54, -69, 96, 36,
      -55, 36, -97, 70, 82, 9, 4, -63, -29, 32, 49, 23, -53, 88, 18, 8, -96, 72,
      -23, -82, 6, 14, -6, -31, -12, -39, 61, -58, -32, 57, 77, 12, -7, 56, -40,
      -48, -35, 40, -35, 12, -28, 90, -87, -4, 79, 30, 80, 82, -20, -43, 76, 62,
      70, -30, -92, -42, 7, 68, -24, 75, 26, -70, -36, 95, 86, 0, -52, -49, -60,
      12, 63, -11, -20, 75, 84, -41, -18, 41, -82, 61, 98, 70, 0, 45, -83, 8,
      -96, 24, -24, -44, -24, -98, -14, 39, 97, -51, -60, -78, -24, -44, 10,
      -84, 44, 89, 67, 5, -75, -73, -53, -81, 64, -55, 88, -35, 89, -94, 72, 69,
      29, -52, -97, 81, -73, -35, 20, -99, 13, 36, 98, 65, 69, 8, 81, 13, -25,
      25, 95, -1, 51, -58, -5, 16, -37, -17, 57, -71, -35, 29, 75, 70, 53, 77,
      51, 79, -58, -51, 56, 31, 84, 54, -27, 30, -37, -46, -56, 14, 56, -84, 89,
      7, -43, -16, 99, 19, 67, 56, 24, -68, -38, -1, -97, -84, -24, 53, 71, -6,
      -98, 28, -98, 63, -18, -25, -7, 21, 5, 13, -88, -39, 28, -98, 68, 61, -15,
      44, -43, -71, 1, 81, -39, 62, -20, -60, 54, 33, 69, 26, -96, 48, -69, -94,
      11, -11, -20, 80, 87, 61, -29, 98, -77, 75, 99, 67, 37, -38, 11, 93, -10,
      88, 51, 27, 28, -68, 66, -41, 41, 36, 84, 44, -16, 91, 49, 71, -19, -94,
      28, -32, 44, 75, -57, 66, 51, -80, 10, -35, -19, 97, -65, 70, 63, 86, -2,
      -9, 94, -59, 26, 35, 76, 11, -21, -63, -21, -94, 84, 59, 87, 13, -96, 31,
      -35, -53, -26, -84, -34, 60, -20, 23, 58, 15, -7, 21, -22, 67, 88, -28,
      -91, 14, -93, 61, -98, -38, 75, -19, -56, 59, -83, -91, -51, -79, 16, 14,
      -56, 90, 6, -14, 27, 63, -91, -15, -22, -22, 82, 32, -54, 47, -96, -69,
      -61, 86, 91, -60, -75, 43, -3, -31, 3, -9, -23, 28, 11, 69, -81, 31, 59,
      25, -83, -36, -12, -75, 48, 42, -21, 8, -26, 24, -68, -23, 31, -30, -60,
      0, -13, -36, -57, 60, 32, 22, -49, 85, -49, 38, 55, -54, -31, -9, 70, -38,
      54, -65, -37, -20, 76, 42, 64, -73, -57, 95, -20, 74, -57, 19, -49, 29,
      83, -7, -11, -8, -84, 40, -45, -57, -45, 86, -12, 24, -46, -64, 62, -91,
      -30, -74, -35, -76, 44, -94, -73, 86, 77, 7, 37, -80, -74, 87, 48, 85,
      -19, -85, -45, -27, 31, 9, -8, 85, -28, 79, -14, 25, 91, -51, 10, -61,
      -49, 74, -38, 94, 56, -12, 57, 34, 71, -5, 53, 74, -18, -21, 59, 39, -30,
      90, -88, -99, -24, 3, 62, 47, -40, -51, -27, -49, -26, 82, -11, 1, 34, 27,
      -5, -10, 92, -48, -99, 63, 23, 31, 14, -94, -90, -49, 44, -44, -59, 33,
      -44, 17, -64, -82, -36, -28, -57, 13, 0, -7, -4, 88, 70, -93, -7, -35, -4,
      -15, -6, -26, -75, 93, -95, 39, 98, 90, 66, 20, -54, -93, -47, -22, 0,
      -35, -28, 41, 14, -8, -46, -86, 84, 26, -98, 55, 32, -29, 96, -94, 32,
      -33, -21, 57, -39, -17, -27, -64, -50, -61, 55, -28, -78, 84, 49, 22, -73,
      -79, -37, 40, 12, -7, 53, -26, -80, 31, -94, 51, -97, -98, 56, 34, -54,
      -88, -32, -17, -29, 17, 18, 20, 32, -49, 91, 54, -65, 40, -47, -39, 38,
      -8, -99, -73, 84, 30, 0, -96, -38, 5, 32, -36, -16, -35, 74, 29, -23, -80,
      -88, 47, 36, 29, -32, -54, 79, -64, 76, 91, 53, -71, -71, -9, -3, -93, 17,
      -19, 36, 94, -38, 97, -1, 70, -62, 82, -65, -87, 11, 11, -68, -1, -41, 44,
      -71, 3, 89], 3452)
])
def test_maximum_subarray(nums, expect):
    from solution.maximum_subarray import Solution
    solution = Solution()

    assert solution.max_sub_array(nums) == expect


@pytest.mark.parametrize("n, expect", [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (10, "13211311123113112211"),
    (15, "311311222113111231131112132112311321322112111312211312111322212311322113212221"),
])
def test_count_and_say(n, expect):
    from solution.count_and_say import Solution
    solution = Solution()

    assert solution.count_and_say(n) == expect


@pytest.mark.parametrize("height, expect", [
    ([], 0),
    ([3, 2, 1, 2, 1], 1),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
])
def test_trapping_rain_water(height, expect):
    from solution.trapping_rain_water import Solution
    solution = Solution()

    assert solution.trap(height) == expect


@pytest.mark.parametrize("n, expect", [
    (1, [
        [
            "Q"
        ]
    ]),
    (4, [
        [
            ".Q..",
            "...Q",
            "Q...",
            "..Q."],
        [
            "..Q.",
            "Q...",
            "...Q",
            ".Q.."]
    ]),
    (5, [
        [
            "Q....",
            "..Q..",
            "....Q",
            ".Q...",
            "...Q."
        ],
        [
            "Q....",
            "...Q.",
            ".Q...",
            "....Q",
            "..Q.."
        ],
        [
            ".Q...",
            "...Q.",
            "Q....",
            "..Q..",
            "....Q"
        ],
        [
            ".Q...",
            "....Q",
            "..Q..",
            "Q....",
            "...Q."
        ],
        [
            "..Q..",
            "Q....",
            "...Q.",
            ".Q...",
            "....Q"
        ],
        [
            "..Q..",
            "....Q",
            ".Q...",
            "...Q.",
            "Q...."
        ],
        [
            "...Q.",
            "Q....",
            "..Q..",
            "....Q",
            ".Q..."
        ],
        [
            "...Q.",
            ".Q...",
            "....Q",
            "..Q..",
            "Q...."
        ],
        [
            "....Q",
            ".Q...",
            "...Q.",
            "Q....",
            "..Q.."
        ],
        [
            "....Q",
            "..Q..",
            "Q....",
            "...Q.",
            ".Q..."
        ]
    ])
])
def test_n_queens(n, expect):
    from solution.n_queens import Solution
    solution = Solution()

    assert solution.solve_n_queens(n) == expect


@pytest.mark.parametrize("n, expect", [
    (1, 1),
    (2, 0),
    (3, 0),
    (4, 2),
    (5, 10),
    (6, 4),
    (7, 40),
    (8, 92),
    (9, 352),
])
def test_n_queens_ii(n, expect: int):
    from solution.n_queens_ii import Solution
    solution = Solution()

    assert solution.total_n_queens(n) == expect


@pytest.mark.parametrize("jewels, stones, expect", [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0)
])
def test_jewels_and_stones(jewels: str, stones: str, expect: int):
    from solution.jewels_and_stones import Solution
    assert Solution().num_jewels_in_stones(jewels, stones) == expect


@pytest.mark.parametrize("a, b, c", [
    ("2", "3", "6"),
    ("123", "456", "56088"),
    ("1234567890", "9876543210", "12193263111263526900")
])
def test_multiply_strings(a: str, b: str, c: str):
    from solution.multiply_strings import Solution
    assert Solution().multiply(a, b) == c
