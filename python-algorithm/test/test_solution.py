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
    from leetcode.palindrome_number import Solution

    assert Solution().is_palindrome(x) == res


@pytest.mark.parametrize("nums, target, res", [([-1, 2, 1, -4], 1, 2)])
def test_3sum_closest(nums, target, res):
    from leetcode.three_sum_closest import Solution

    assert Solution().three_sum_closest(nums, target) == res


@pytest.mark.parametrize("a, b, res", [(1, 1, "ab"), (1, 4, "bbabb")])
def test_str_without_3a3b(a, b, res):
    from leetcode.string_without_3a3b import Solution

    assert Solution().str_without_3a3b(a, b) == res


@pytest.mark.parametrize(
    "days, costs, res",
    [
        ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
    ],
)
def test_minimum_cost_for_tickets(days, costs, res):
    from leetcode.minimum_cost_for_tickets import Solution

    assert Solution().min_cost_tickets(days, costs) == res


@pytest.mark.parametrize(
    "root, res",
    [([3, 0, 0], 2), ([0, 3, 0], 3), ([1, 0, 2], 2), ([1, 0, 0, None, 3], 4)],
)
def test_distribute_coins_in_binary_tree(root, res):
    from leetcode.distribute_coins_in_binary_tree import Solution

    assert Solution().distribute_coins(Converter.list_to_tree(root)) == res


def test_time_based_key_value_store():
    from leetcode.time_based_key_value_store import TimeMap

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
    from leetcode.longest_turbulent_subarray import Solution

    assert Solution().max_turbulence_size(li) == res


@pytest.mark.parametrize("nums, res", [([2, 1, 3], 12)])
def test_triples_with_bitwise_and_equal_to_zero(nums, res):
    from leetcode.triples_with_bitwise_and_equal_to_zero import Solution

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
    from leetcode.unique_paths_iii import Solution

    assert Solution().unique_paths_iii(grid) == res


@pytest.mark.parametrize(
    "x, y, bound, res",
    [(2, 3, 10, [2, 3, 4, 5, 7, 9, 10]), (3, 5, 15, [2, 4, 6, 8, 10, 14])],
)
def test_powerful_integers(x, y, bound, res):
    from leetcode.powerful_integers import Solution

    assert Solution().powerful_integers(x, y, bound) == res


@pytest.mark.parametrize(
    "a, res",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_sorted_squares(a, res):
    from leetcode.squares_of_a_sorted_array import Solution

    assert Solution().sorted_squares(a) == res


@pytest.mark.parametrize(
    "a, res",
    [([2, 1, 2], 5), ([1, 2, 1], 0), ([3, 2, 3, 4], 10), ([3, 6, 2, 3], 8)]
)
def test_largest_perimeter(a, res):
    from leetcode.largest_perimeter_triangle import Solution

    assert Solution().largest_perimeter(a) == res


@pytest.mark.parametrize("arr, k, res", [([4, 5, 0, -2, -3, 1], 5, 7)])
def test_subarray_sums_divisible_by_k(arr, k, res):
    from leetcode.subarray_sums_divisible_by_k import Solution

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
    from leetcode.equal_rational_numbers import Solution

    assert Solution().is_rational_equal(s, t) == res


@pytest.mark.parametrize(
    "points, k, res",
    [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ],
)
def test_k_closest_points_to_origin(points, k, res):
    from leetcode.k_closest_points_to_origin import Solution

    assert Solution().k_closest_2(points, k) == res


@pytest.mark.parametrize(
    "nums, res", [([3, 2, 4, 1], [3, 4, 2, 3, 2]), ([1, 2, 3], [])]
)
def test_pancake_sorting(nums, res):
    from leetcode.pancake_sorting import Solution

    assert Solution().pancake_sort(nums) == res


@pytest.mark.parametrize(
    "x, target, ans", [(3, 19, 5), (5, 501, 8), (100, 200000000, 7)]
)
def test_least_operators_to_express_number(x, target, ans):
    from leetcode.least_operators_to_express_number import Solution

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
    from leetcode.minimum_area_rectangle_ii import Solution

    assert Solution().min_area_free_rect(points) == area


@pytest.mark.parametrize("li, ans", [
    ([1, 2, 3, 3], 3), ([2, 1, 2, 5, 3, 2], 2), ([5, 1, 5, 2, 5, 3, 5, 4], 5)
])
def test_n_repeated_element_in_size_2n_array(li, ans):
    from leetcode.n_repeated_element_in_size_2n_array import Solution
    s = Solution()

    assert s.repeated_n_times(li) == ans
    assert s.ans(li) == ans
    assert s.ans_2(li) == ans


@pytest.mark.parametrize(
    "arr, ans", [([6, 0, 8, 2, 1, 5], 4), ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7)]
)
def test_maximum_width_ramp(arr, ans):
    from leetcode.maximum_width_ramp import Solution

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
    from leetcode.delete_columns_to_make_sorted import Solution

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
    from leetcode.delete_columns_to_make_sorted_ii import Solution

    assert Solution().min_deletion_size(arr) == ans


@pytest.mark.parametrize("arr, ans", [
    (["babca", "bbazb"], 3),
    (["edcba"], 4),
    (["ghi", "def", "abc"], 0)
])
def test_delete_columns_to_make_sorted_iii(arr, ans):
    from leetcode.delete_columns_to_make_sorted_iii import Solution

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
    from leetcode.validate_stack_sequences import Solution

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
    from leetcode.numbers_with_same_consecutive_differences import Solution

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
    from leetcode.custom_sort_string import Solution

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
    from leetcode.single_number import Solution
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
    from leetcode.combination_sum import Solution
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
    from leetcode.combination_sum_ii import Solution
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
    from leetcode.combination_sum_iii import Solution
    solution = Solution()

    assert solution.combination_sum3(n, k) == expect


@pytest.mark.parametrize("nums, target, expect", [
    ([1, 2, 3], 4, 7),
    # ([4, 2, 1], 32, 39882198)
])
def test_combination_sum_4(nums, target, expect):
    from leetcode.combination_sum_iv import Solution
    solution = Solution()

    assert solution.combination_sum4(nums, target) == expect


@pytest.mark.parametrize("nums, expect", [
    ([-1], -1),
    ([-2, -1], -1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1, 2, 3, 4, 5], 15)
])
def test_maximum_subarray(nums, expect):
    from leetcode.maximum_subarray import Solution
    solution = Solution()

    assert solution.max_sub_array(nums) == expect


@pytest.mark.parametrize("n, expect", [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (10, "13211311123113112211")
])
def test_count_and_say(n, expect):
    from leetcode.count_and_say import Solution
    solution = Solution()

    assert solution.count_and_say(n) == expect


@pytest.mark.parametrize("height, expect", [
    ([], 0),
    ([3, 2, 1, 2, 1], 1),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
])
def test_trapping_rain_water(height, expect):
    from leetcode.trapping_rain_water import Solution
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
    from leetcode.n_queens import Solution
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
    from leetcode.n_queens_ii import Solution
    solution = Solution()

    assert solution.total_n_queens(n) == expect


@pytest.mark.parametrize("jewels, stones, expect", [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0)
])
def test_jewels_and_stones(jewels: str, stones: str, expect: int):
    from leetcode.jewels_and_stones import Solution
    assert Solution().num_jewels_in_stones(jewels, stones) == expect


@pytest.mark.parametrize("a, b, c", [
    ("2", "3", "6"),
    ("123", "456", "56088"),
    ("1234567890", "9876543210", "12193263111263526900")
])
def test_multiply_strings(a: str, b: str, c: str):
    from leetcode.multiply_strings import Solution
    assert Solution().multiply(a, b) == c


@pytest.mark.parametrize("s, expect", [
    ([], []),
    (["1"], ["1"]),
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
])
def test_reverse_string(s, expect):
    from leetcode.reverse_string import Solution
    Solution().reverse_string(s)
    assert s == expect


@pytest.mark.parametrize("nums, expect", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([0, 0], [0, 0]),
    ([1, 0], [0, 1]),
    ([1, 0, 2], [0, 2, 0]),
])
def test_product_of_array_except_self(nums, expect):
    from leetcode.product_of_array_except_self import Solution
    assert Solution().product_except_self(nums) == expect


@pytest.mark.parametrize("nums, sets", [
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
])
def test_subsets(nums, sets):
    from leetcode.subsets import Solution
    assert Solution().subsets(nums) == sets


@pytest.mark.parametrize("nums, sets", [
    ([2, 2, 2], [[], [2], [2, 2], [2, 2, 2]]),
    ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
])
def test_subsets_ii(nums, sets):
    from leetcode.subsets_ii import Solution
    assert Solution().subsets_with_dup(nums) == sets


@pytest.mark.parametrize("nums, expect", [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1)
])
def test_first_missing_positive(nums, expect):
    from leetcode.first_missing_positive import Solution
    assert Solution().first_missing_positive(nums) == expect


@pytest.mark.parametrize("nums, expect", [
    ([1, 2, 3], [
        [3, 2, 1],
        [2, 3, 1],
        [2, 1, 3],
        [3, 1, 2],
        [1, 3, 2],
        [1, 2, 3]
    ])
])
def test_permutations(nums, expect):
    from leetcode.permutations import Solution
    assert Solution().permute(nums) == expect


@pytest.mark.parametrize("nums, expect", [
    ([1, 2], [[1, 2], [2, 1]]),
    ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]])
])
def test_permutations_ii(nums, expect):
    from leetcode.permutations_ii import Solution
    solution = Solution()
    assert solution.permute_unique_dfs(nums) == expect


@pytest.mark.parametrize("x, n, expect", [
    (2, 0, 1),
    (2, 3, 8),
    (2, -2, 0.25)
])
def test_pow_n(x, n, expect):
    from leetcode.powx_n import Solution
    assert Solution().my_pow(x, n) == expect


@pytest.mark.parametrize("strs, expect", [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [
        ['eat', 'tea', 'ate'],
        ['tan', 'nat'],
        ['bat']
    ]),
])
def test_group_anagrams(strs, expect):
    from leetcode.group_anagrams import Solution
    assert Solution().group_anagrams(strs) == expect


@pytest.mark.parametrize("matrix, expect", [
    ([
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
     ], [
         [7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]
     ]),
    ([
         [5, 1, 9, 11],
         [2, 4, 8, 10],
         [13, 3, 6, 7],
         [15, 14, 12, 16]
     ], [
         [15, 13, 2, 5],
         [14, 3, 4, 1],
         [12, 6, 8, 9],
         [16, 7, 10, 11]
     ])
])
def test_rotate_image(matrix, expect):
    from leetcode.rotate_image import Solution
    Solution().rotate(matrix)
    assert matrix == expect


@pytest.mark.parametrize("nums, expect", [
    ([0], True),
    ([2, 0, 0], True),
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([4, 2, 6, 1, 0, 6, 4, 3, 2, 1, 0, 1, 1, 0, 8, 1], False)
])
def test_jump_game(nums, expect):
    from leetcode.jump_game import Solution
    assert Solution().can_jump(nums) == expect


@pytest.mark.parametrize("intervals, expect", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[2, 3], [4, 5], [6, 7], [8, 9]], [[2, 3], [4, 5], [6, 7], [8, 9]]),
    ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10], [1, 10]], [[1, 10]])
])
def test_merge_intervals(intervals, expect):
    from leetcode.merge_intervals import Solution
    assert Solution().merge(intervals) == expect


@pytest.mark.parametrize("intervals, new_interval, expect", [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8],
     [[1, 2], [3, 10], [12, 16]]),
])
def test_insert_interval(intervals, new_interval, expect):
    from leetcode.insert_interval import Solution
    solution = Solution()
    assert solution.insert_2(intervals, new_interval) == expect


@pytest.mark.parametrize("s, expect", [
    ("", 0),
    ("   ", 0),
    ("hello world", 5),
    ("hello world   ", 5)
])
def test_length_of_last_word(s, expect):
    from leetcode.length_of_last_word import Solution
    solution = Solution()
    assert solution.length_of_lastWord(s) == expect


@pytest.mark.parametrize("matrix, output", [
    ([[1]], [1]),
    ([
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
     ], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([
         [1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]
     ], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
])
def test_spiral_matrix(matrix, output):
    from leetcode.spiral_matrix import Solution
    s = Solution()
    assert s.spiral_order(matrix) == output


@pytest.mark.parametrize("n, matrix", [
    (1, [[1]]),
    (2, [[1, 2], [4, 3]]),
    (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
    (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
])
def test_spiral_matrix_ii(n, matrix):
    from leetcode.spiral_matrix_ii import Solution
    solution = Solution()
    assert solution.generate_matrix(n) == matrix


@pytest.mark.parametrize("m,n, expect", [
    (3, 2, 3),
    (7, 3, 28),
    (9, 9, 12870)
])
def test_unique_paths(m, n, expect):
    from leetcode.unique_paths import Solution
    s = Solution()
    assert s.unique_paths(m, n) == expect


@pytest.mark.parametrize("grid, expect", [
    ([
         [0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]
     ], 2)
])
def test_unique_paths_ii(grid, expect):
    from leetcode.unique_paths_ii import Solution
    s = Solution()
    assert s.unique_paths_with_obstacles(grid) == expect


@pytest.mark.parametrize("grid, expect", [
    ([
         [1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]
     ], 7),
    ([
         [1, 2, 3, 4],
         [12, 51, 9, 5],
         [23, 9, 1, 8]
     ], 23)
])
def test_min_path_sum(grid, expect):
    from leetcode.minimum_path_sum import Solution
    s = Solution()
    assert s.min_path_sum(grid) == expect


@pytest.mark.parametrize("digits, expect", [
    ([1, 2, 3], [1, 2, 4]),
    ([0], [1]),
    ([9, 9, 9], [1, 0, 0, 0]),
])
def test_plus_one(digits, expect):
    from leetcode.plus_one import Solution
    s = Solution()
    assert s.plus_one_2(digits) == expect


@pytest.mark.parametrize("n, expect", [
    (1, 1),
    (2, 2),
    (3, 3),
])
def test_climb_stairs(n, expect):
    from leetcode.climbing_stairs import Solution
    s = Solution()
    assert s.climb_stairs(n) == expect


@pytest.mark.parametrize("s, p, expect", [
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False),
])
def test_wildcard_matching(s, p, expect):
    from leetcode.wildcard_matching import Solution
    solution = Solution()
    assert solution.is_match(s, p) == expect


@pytest.mark.parametrize("s, p, expect", [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("mississippi", "mis*is*p*.", False),
    ("ab", ".*c", False)
])
def test_regular_expression_matching(s, p, expect):
    from leetcode.regular_expression_matching import Solution
    solution = Solution()
    assert solution.is_match(s, p) == expect


@pytest.mark.parametrize("word1, word2, expect", [
    ("horse", "ros", 3),
    ("intention", "execution", 5)
])
def test_edit_distance(word1, word2, expect):
    from leetcode.edit_distance import Solution
    solution = Solution()
    assert solution.min_distance(word1, word2) == expect


@pytest.mark.parametrize("nums, expect", [
    ([], []),
    ([2, 0, 1], [0, 1, 2]),
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ([2, 1, 0, 2, 1, 0], [0, 0, 1, 1, 2, 2])
])
def test_sort_colors(nums, expect):
    from leetcode.sort_colors import Solution
    solution = Solution()
    solution.sort_colors_1_pass(nums)
    assert nums == expect


@pytest.mark.parametrize("s, t, expect", [
    ("", "", ""),
    ("A", "A", "A"),
    ("A", "", ""),
    ("", "A", ""),
    ("ADOBECODEBANC", "ABC", "BANC")
])
def test_minimum_window_substring(s, t, expect):
    from leetcode.minimum_window_substring import Solution
    solution = Solution()
    assert solution.min_window(s, t) == expect


@pytest.mark.parametrize("board, word, expect", [
    ([
         ["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]
     ], "ABCCED", True),
    ([
         ['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']
     ], "SEE", True),
    ([
         ['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']
     ], "ABCB", False)
])
def test_word_search(board, word, expect):
    from leetcode.word_search import Solution
    s = Solution()
    assert s.exist(board, word) == expect


@pytest.mark.parametrize("heights, expect", [
    ([2, 1, 5, 6, 2, 3], 10),
    ([1, 2, 3, 0, 4], 4),
    ([6, 2, 5, 4, 5, 1, 6], 12)
])
def test_largest_rectangle_in_histogram(heights, expect):
    from leetcode.largest_rectangle_in_histogram import Solution
    s = Solution()
    assert s.largest_rectangle_area_1(heights) == expect


@pytest.mark.parametrize("matrix, expect", [
    ([
         ["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]
     ], 6)
])
def test_maximal_rectangle(matrix, expect):
    from leetcode.maximal_rectangle import Solution
    s = Solution()
    # assert s.maximal_rectangle(matrix) == expect


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
