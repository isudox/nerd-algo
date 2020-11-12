from typing import List
import pytest
from common.converter import Converter


@pytest.mark.parametrize("s, expect", [
    ("", 0),
    (" ", 1),
    ("bbbbb", 1),
    ("abcabcbb", 3),
    ("pwwkew", 3)
])
def test_3(s: str, expect: int):
    from leetcode.problem_3 import Solution
    solution = Solution()
    assert solution.length_of_longest_substring_1(s) == expect
    assert solution.length_of_longest_substring_2(s) == expect
    assert solution.length_of_longest_substring_3(s) == expect
    assert solution.length_of_longest_substring_4(s) == expect
    assert solution.length_of_longest_substring_5(s) == expect


@pytest.mark.parametrize("s, ans", [
    ("42", 42),
    ("   -42", -42),
    ("4193 with words", 4193),
    ("words and 987", 0),
    ("-91283472332", -2147483648)
])
def test_8(s: str, ans: int):
    from leetcode.problem_8 import Solution
    solution = Solution()
    assert solution.my_atoi(s) == ans


@pytest.mark.parametrize("x, res", [
    (1, True),
    (12, False),
    (333, True),
    (333, True)
])
def test_9(x, res):
    from leetcode.problem_9 import Solution
    sol = Solution()
    assert sol.is_palindrome(x) == res


@pytest.mark.parametrize("s, p, expect", [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("mississippi", "mis*is*p*.", False),
    ("ab", ".*c", False)
])
def test_10(s, p, expect):
    from leetcode.problem_10 import Solution
    solution = Solution()
    assert solution.is_match(s, p) == expect


@pytest.mark.parametrize("nums, expect", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
]
                         )
def test_15(nums: List[int], expect: List[List[int]]):
    from leetcode.problem_15 import Solution
    solution = Solution()
    assert solution.three_sum(nums) == expect


@pytest.mark.parametrize("nums, target, res", [([-1, 2, 1, -4], 1, 2)])
def test_16(nums, target, res):
    from leetcode.problem_16 import Solution
    sol = Solution()
    assert sol.three_sum_closest(nums, target) == res


@pytest.mark.parametrize("s, ans", [
    ("", True),
    ("[", False),
    ("()", True),
    ("()[]{}", True),
    ("([)]", False),
])
def test_20(s: str, ans: bool):
    from leetcode.problem_20 import Solution
    sol = Solution()
    assert sol.is_valid(s) == ans


@pytest.mark.parametrize("nums, ans", [
    ([1, 2, 3], [1, 3, 2]),
    ([1, 3, 2], [2, 1, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 1, 5], [1, 5, 1]),
    ([5, 1, 1], [1, 1, 5]),
    ([1], [1])
])
def test_31(nums: List[int], ans: List[int]):
    from leetcode.problem_31 import Solution
    sol = Solution()
    sol.next_permutation(nums)
    assert nums == ans


@pytest.mark.parametrize("s, ans", [
    ("(()", 2),
    (")()())", 4),
    ("()(()", 2),
    ("(()))())(", 4),
    ("()())(((()))", 6)
])
def test_32(s, ans):
    from leetcode.problem_32 import Solution
    sol = Solution()
    assert sol.longest_valid_parentheses(s) == ans
    assert sol.longest_valid_parentheses_2(s) == ans


@pytest.mark.parametrize("board, ans", [
    ([["5", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
     [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
      ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
      ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
      ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
      ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
      ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
      ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
      ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
      ["3", "4", "5", "2", "8", "6", "1", "7", "9"]])
])
def test_37(board: List[List[str]], ans: List[List[str]]):
    from leetcode.problem_37 import Solution
    sol = Solution()
    sol.solve_sudoku(board)
    assert board == ans


@pytest.mark.parametrize("n, expect", [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (10, "13211311123113112211")
])
def test_38(n, expect):
    from leetcode.problem_38 import Solution
    solution = Solution()
    assert solution.count_and_say(n) == expect


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
def test_39(candidates, target, expect):
    from leetcode.problem_39 import Solution
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
def test_40(candidates, target, expect):
    from leetcode.problem_40 import Solution
    solution = Solution()
    assert solution.combination_sum2(candidates, target) == expect


@pytest.mark.parametrize("nums, expect", [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1)
])
def test_41(nums, expect):
    from leetcode.problem_41 import Solution
    sol = Solution()
    assert sol.first_missing_positive(nums) == expect


@pytest.mark.parametrize("height, expect", [
    ([], 0),
    ([3, 2, 1, 2, 1], 1),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
])
def test_42(height, expect):
    from leetcode.problem_42 import Solution
    solution = Solution()
    assert solution.trap(height) == expect


@pytest.mark.parametrize("a, b, c", [
    ("2", "3", "6"),
    ("123", "456", "56088"),
    ("1234567890", "9876543210", "12193263111263526900")
])
def test_43(a: str, b: str, c: str):
    from leetcode.problem_43 import Solution
    assert Solution().multiply(a, b) == c


@pytest.mark.parametrize("s, p, expect", [
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False),
])
def test_44(s, p, expect):
    from leetcode.problem_44 import Solution
    solution = Solution()
    assert solution.is_match(s, p) == expect
    assert solution.is_match_2(s, p) == expect


@pytest.mark.parametrize("nums, expect", [
    ([2, 3, 1, 1, 4], 2)
])
def test_45(nums, expect):
    from leetcode.problem_45 import Solution
    assert Solution().jump(nums) == expect


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
def test_46(nums, expect):
    from leetcode.problem_46 import Solution
    assert Solution().permute(nums) == expect


@pytest.mark.parametrize("nums, expect", [
    ([1, 2], [[1, 2], [2, 1]]),
    ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]])
])
def test_47(nums, expect):
    from leetcode.problem_47 import Solution
    solution = Solution()
    assert solution.permute_unique_dfs(nums) == expect


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
def test_48(matrix, expect):
    from leetcode.problem_48 import Solution
    Solution().rotate(matrix)
    assert matrix == expect


@pytest.mark.parametrize("strs, expect", [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [
        ['eat', 'tea', 'ate'],
        ['tan', 'nat'],
        ['bat']
    ]),
])
def test_49(strs, expect):
    from leetcode.problem_49 import Solution
    assert Solution().group_anagrams(strs) == expect


@pytest.mark.parametrize("x, n, expect", [
    (2, 0, 1),
    (2, 3, 8),
    (2, -2, 0.25)
])
def test_50(x, n, expect):
    from leetcode.problem_50 import Solution
    sol = Solution()
    assert sol.my_pow(x, n) == expect


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
def test_51(n, expect):
    from leetcode.problem_51 import Solution
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
def test_52(n, expect: int):
    from leetcode.problem_52 import Solution
    solution = Solution()
    assert solution.total_n_queens(n) == expect


@pytest.mark.parametrize("nums, expect", [
    ([-1], -1),
    ([-2, -1], -1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1, 2, 3, 4, 5], 15)
])
def test_53(nums, expect):
    from leetcode.problem_53 import Solution
    solution = Solution()
    assert solution.max_sub_array(nums) == expect


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
def test_54(matrix, output):
    from leetcode.problem_54 import Solution
    sol = Solution()
    assert sol.spiral_order(matrix) == output


@pytest.mark.parametrize("nums, expect", [
    ([0], True),
    ([2, 0, 0], True),
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([4, 2, 6, 1, 0, 6, 4, 3, 2, 1, 0, 1, 1, 0, 8, 1], False)
])
def test_55(nums, expect):
    from leetcode.problem_55 import Solution
    sol = Solution()
    assert sol.can_jump(nums) == expect


@pytest.mark.parametrize("intervals, expect", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[2, 3], [4, 5], [6, 7], [8, 9]], [[2, 3], [4, 5], [6, 7], [8, 9]]),
    ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10], [1, 10]], [[1, 10]])
])
def test_56(intervals, expect):
    from leetcode.problem_56 import Solution
    assert Solution().merge(intervals) == expect


@pytest.mark.parametrize("intervals, new_interval, expect", [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8],
     [[1, 2], [3, 10], [12, 16]]),
])
def test_57(intervals, new_interval, expect):
    from leetcode.problem_57 import Solution
    solution = Solution()
    assert solution.insert(intervals, new_interval) == expect


@pytest.mark.parametrize("s, expect", [
    ("", 0),
    ("   ", 0),
    ("hello world", 5),
    ("hello world   ", 5)
])
def test_58(s, expect):
    from leetcode.problem_58 import Solution
    solution = Solution()
    assert solution.length_of_last_word(s) == expect


@pytest.mark.parametrize("n, matrix", [
    (1, [[1]]),
    (2, [[1, 2], [4, 3]]),
    (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
    (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
])
def test_59(n, matrix):
    from leetcode.problem_59 import Solution
    solution = Solution()
    assert solution.generate_matrix(n) == matrix


@pytest.mark.parametrize("m,n, expect", [
    (3, 2, 3),
    (7, 3, 28),
    (9, 9, 12870)
])
def test_62(m, n, expect):
    from leetcode.problem_62 import Solution
    sol = Solution()
    assert sol.unique_paths(m, n) == expect


@pytest.mark.parametrize("grid, expect", [
    ([
         [0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]
     ], 2)
])
def test_63(grid, expect):
    from leetcode.problem_63 import Solution
    sol = Solution()
    assert sol.unique_paths_with_obstacles(grid) == expect


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
def test_64(grid, expect):
    from leetcode.problem_64 import Solution
    s = Solution()
    assert s.min_path_sum(grid) == expect


@pytest.mark.parametrize("digits, expect", [
    ([1, 2, 3], [1, 2, 4]),
    ([0], [1]),
    ([9, 9, 9], [1, 0, 0, 0]),
])
def test_66(digits, expect):
    from leetcode.problem_66 import Solution
    sol = Solution()
    assert sol.plus_one_2(digits) == expect


@pytest.mark.parametrize("a, b, result", [
    ("0", "0", "0"),
    ("11", "1", "100"),
    ("1010", "1011", "10101"),
    ("100", "110010", "110110")
])
def test_67(a: str, b: str, result: str):
    from leetcode.problem_67 import Solution
    sol = Solution()
    assert sol.add_binary(a, b) == result


@pytest.mark.parametrize("x, expect", [
    (0, 0),
    (1, 1),
    (4, 2),
    (8, 2),
    (101, 10),
    (9999999999999999, 99999999)
])
def test_69(x, expect):
    from leetcode.problem_69 import Solution
    sol = Solution()
    assert sol.my_sqrt_1(x) == expect


@pytest.mark.parametrize("n, expect", [
    (1, 1),
    (2, 2),
    (3, 3),
])
def test_70(n, expect):
    from leetcode.problem_70 import Solution
    sol = Solution()
    assert sol.climb_stairs(n) == expect


@pytest.mark.parametrize("word1, word2, expect", [
    ("horse", "ros", 3),
    ("intention", "execution", 5)
])
def test_72(word1, word2, expect):
    from leetcode.problem_72 import Solution
    solution = Solution()
    assert solution.min_distance(word1, word2) == expect


@pytest.mark.parametrize("nums, expect", [
    ([], []),
    ([2, 0, 1], [0, 1, 2]),
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ([2, 1, 0, 2, 1, 0], [0, 0, 1, 1, 2, 2])
])
def test_75(nums, expect):
    from leetcode.problem_75 import Solution
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
def test_76(s, t, expect):
    from leetcode.problem_76 import Solution
    solution = Solution()
    assert solution.min_window(s, t) == expect


@pytest.mark.parametrize("n, k, ans", [
    (4, 2, [[1, 4], [2, 4], [3, 4], [1, 3], [2, 3], [1, 2]]),
    (5, 3, [[1, 4, 5], [2, 4, 5], [3, 4, 5], [1, 3, 5], [2, 3, 5],
            [1, 2, 5], [1, 3, 4], [2, 3, 4], [1, 2, 4], [1, 2, 3]])
])
def test_77(n: int, k: int, ans: List[List[int]]):
    from leetcode.problem_77 import Solution
    sol = Solution()
    assert sol.combine(n, k) == ans


@pytest.mark.parametrize("nums, sets", [
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
])
def test_78(nums, sets):
    from leetcode.problem_78 import Solution
    sol = Solution()
    assert sol.subsets(nums) == sets


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
def test_79(board, word, expect):
    from leetcode.problem_79 import Solution
    sol = Solution()
    assert sol.exist(board, word) == expect


@pytest.mark.parametrize("heights, expect", [
    ([2, 1, 5, 6, 2, 3], 10),
    ([1, 2, 3, 0, 4], 4),
    ([6, 2, 5, 4, 5, 1, 6], 12)
])
def test_84(heights, expect):
    from leetcode.problem_84 import Solution
    sol = Solution()
    assert sol.largest_rectangle_area_1(heights) == expect


@pytest.mark.parametrize("matrix, expect", [
    ([
         ["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]
     ], 6)
])
def test_85(matrix, expect):
    from leetcode.problem_85 import Solution
    sol = Solution()
    assert sol.maximal_rectangle(matrix) == expect


@pytest.mark.parametrize("nums, sets", [
    ([2, 2, 2], [[], [2], [2, 2], [2, 2, 2]]),
    ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
])
def test_90(nums, sets):
    from leetcode.problem_90 import Solution
    assert Solution().subsets_with_dup(nums) == sets


@pytest.mark.parametrize("s, ans", [
    ("25525511135", ["255.255.11.135", "255.255.111.35"]),
    ("010010", ["0.10.0.10", "0.100.1.0"])
])
def test_93(s: str, ans: List[str]):
    from leetcode.problem_93 import Solution
    sol = Solution()
    assert sol.restore_ip_addresses(s) == ans


@pytest.mark.parametrize("n, res", [
    (10, 16796),
    (19, 1767263190)
])
def test_96(n, res):
    from leetcode.problem_96 import Solution
    solution = Solution()
    assert solution.num_trees_1(n) == res


@pytest.mark.parametrize("s1, s2, s3, expect", [
    ("a", "", "a", True),
    ("a", "", "aa", False),
    ("a", "ab", "aba", True),
    ("aabd", "abdc", "aabdabcd", True),
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("aabcc", "dbbca", "aadbcbbcac", True),
    ("caccbbcacacabaaa", "ccaaaccabbabbcaa", "ccccaacacababcbbacbbccaacaaabaaa",
     False)
])
def test_97(s1, s2, s3, expect):
    from leetcode.problem_97 import Solution
    solution = Solution()
    assert solution.is_interleave(s1, s2, s3) == expect
    assert solution.is_interleave_1(s1, s2, s3) == expect


@pytest.mark.parametrize("p, q, expect", [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False)
])
def test_100(p, q, expect):
    from leetcode.problem_100 import Solution
    solution = Solution()
    assert solution.is_same_tree(Converter.list2tree(p),
                                 Converter.list2tree(q)) == expect


@pytest.mark.parametrize("nodes, expect", [
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
    ([1, 2, 2, 3, None, None, 3], True)
])
def test_101(nodes, expect):
    from leetcode.problem_101 import Solution
    sol = Solution()
    assert sol.is_symmetric_recursive(Converter.list2tree(nodes)) == expect
    assert sol.is_symmetric_iterative(Converter.list2tree(nodes)) == expect


@pytest.mark.parametrize("root, expect", [
    ([], []),
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])
])
def test_102(root, expect):
    from leetcode.problem_102 import Solution
    sol = Solution()
    assert sol.level_order(Converter.list2tree(root)) == expect


@pytest.mark.parametrize("root, expect", [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([], 0),
    ([1, 2], 2)
])
def test_104(root, expect):
    from leetcode.problem_104 import Solution
    sol = Solution()
    assert sol.max_depth(Converter.list2tree(root)) == expect


@pytest.mark.parametrize("triangle, ans", [
    ([
         [2],
         [3, 4],
         [6, 5, 7],
         [4, 1, 8, 3]
     ], 11)
])
def test_120(triangle: List[List[int]], ans: int):
    from leetcode.problem_120 import Solution
    sol = Solution()
    assert sol.minimum_total(triangle) == ans
    assert sol.minimum_total_1(triangle) == ans


@pytest.mark.parametrize("prices, expect", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0)
])
def test_121(prices, expect):
    from leetcode.problem_121 import Solution
    sol = Solution()
    assert sol.max_profit(prices) == expect


@pytest.mark.parametrize('prices, ans', [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0)
])
def test_122(prices: List[int], ans: int):
    from leetcode.problem_122 import Solution
    sol = Solution()
    assert sol.max_profit(prices) == ans


# @pytest.mark.timeout(1)
@pytest.mark.parametrize("begin_word, end_word, word_list, ans", [
    ('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"],
     [
         ["hit", "hot", "dot", "dog", "cog"],
         ["hit", "hot", "lot", "log", "cog"]
     ]),
    ('hit', 'cog', ["hot", "dot", "dog", "lot", "log"], [])
])
def test_126(begin_word: str, end_word: str, word_list: List[str], ans: List[List[str]]):
    from leetcode.problem_126 import Solution
    sol = Solution()
    assert sol.find_ladders(begin_word, end_word, word_list) == ans


@pytest.mark.timeout(1)
@pytest.mark.parametrize("begin_word, end_word, word_list, ans", [
    ("hot", "dog", ["hot", "dog"], 0),
    ('hit', 'cog', ["hot", "dot", "dog", "lot", "log"], 0),
    ('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"], 5)
])
def test_127(begin_word: str, end_word: str, word_list: List[str], ans: int):
    from leetcode.problem_127 import Solution
    sol = Solution()
    assert sol.ladder_length(begin_word, end_word, word_list) == ans
    assert sol.ladder_length_2(begin_word, end_word, word_list) == ans


@pytest.mark.parametrize("nums, expect", [
    ([100, 4, 200, 1, 3, 2], 4),
    ([1, 2, 0, 1], 3)
])
def test_128(nums, expect):
    from leetcode.problem_128 import Solution
    sol = Solution()
    assert sol.longest_consecutive_1(nums) == expect
    assert sol.longest_consecutive_2(nums) == expect
    assert sol.longest_consecutive_3(nums) == expect


@pytest.mark.parametrize("board, ans", [
    ([
         ["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]],
     [
         ['X', 'X', 'X', 'X'],
         ['X', 'X', 'X', 'X'],
         ['X', 'X', 'X', 'X'],
         ['X', 'O', 'X', 'X']]),
    ([
         ["X", "O", "X"],
         ["X", "O", "X"],
         ["X", "O", "X"]],
     [
         ["X", "O", "X"],
         ["X", "O", "X"],
         ["X", "O", "X"]]),
    ([
         ["O", "O", "O"],
         ["O", "O", "O"],
         ["O", "O", "O"]],
     [
         ["O", "O", "O"],
         ["O", "O", "O"],
         ["O", "O", "O"]]),
    ([
         ["O", "X", "X", "O", "X"],
         ["X", "O", "O", "X", "O"],
         ["X", "O", "X", "O", "X"],
         ["O", "X", "O", "O", "O"],
         ["X", "X", "O", "X", "O"]],
     [
         ["O", "X", "X", "O", "X"],
         ["X", "X", "X", "X", "O"],
         ["X", "X", "X", "O", "X"],
         ["O", "X", "O", "O", "O"],
         ["X", "X", "O", "X", "O"]])
])
def test_130(board: List[List[str]], ans):
    from leetcode.problem_130 import Solution
    sol = Solution()
    sol.solve(board)
    assert board == ans


@pytest.mark.parametrize("nums, ans", [
    ([2, 1, 2], 1),
    ([1], 1),
    ([4, 3, 5, 3, 4], 5)
])
def test_136(nums, ans):
    from leetcode.problem_136 import Solution
    solution = Solution()
    assert solution.single_number(nums) == ans
    assert solution.reduce_func(nums) == ans


@pytest.mark.parametrize("string, word_dict, expect", [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a", "aa", "aaa", "aaaa"], True),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a", "aa", "aaa", "aaaa"], False)
])
def test_139(string, word_dict, expect):
    from leetcode.problem_139 import Solution
    sol = Solution()
    assert sol.word_break_1(string, word_dict) == expect
    assert sol.word_break_2(string, word_dict) == expect


@pytest.mark.parametrize('s, word_dict, ans', [
    ('apple', ['apple'], ['apple']),
    ("catsanddog", ["cat", "cats", "and", "sand", "dog"], ['cat sand dog', 'cats and dog']),
    ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"],
     ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"])
])
def test_140(s: str, word_dict: List[str], ans: List[str]):
    from leetcode.problem_140 import Solution
    sol = Solution()
    assert sol.word_break(s, word_dict) == ans


@pytest.mark.parametrize("head, expect", [
    ([1, 2], False)
])
def test_141(head, expect):
    from leetcode.problem_141 import Solution
    sol = Solution()
    # TODO


def test_146():
    from leetcode.problem_146 import LRUCache3
    cache = LRUCache3(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3


@pytest.mark.parametrize("nums, ans", [
    ([0, 2], 2),
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0)
])
def test_152(nums, ans):
    from leetcode.problem_152 import Solution
    sol = Solution()
    assert sol.max_product(nums) == ans
    assert sol.max_product_2(nums) == ans
    assert sol.max_product_3(nums) == ans


@pytest.mark.parametrize("nums, ans", [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0)
])
def test_153(nums: List[int], ans: int):
    from leetcode.problem_153 import Solution
    sol = Solution()
    assert sol.find_min(nums) == ans


@pytest.mark.parametrize("nums, ans", [
    ([1, 3, 5], 1),
    ([2, 2, 2, 0, 1], 0)
])
def test_154(nums: List[int], ans: int):
    from leetcode.problem_154 import Solution
    sol = Solution()
    assert sol.find_min(nums) == ans


def test_155():
    from leetcode.problem_155 import MinStack
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.get_min() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.get_min() == -2


@pytest.mark.parametrize("nums, target, ans", [
    ([2, 7, 11, 15], 9, [1, 2]),
])
def test_167(nums, target, ans):
    from leetcode.problem_167 import Solution
    sol = Solution()
    assert sol.two_sum(nums, target) == ans


@pytest.mark.parametrize("nums, ans", [
    ([1, 2, 3, 1], 4),
    ([2, 1, 1, 2], 4),
    ([2, 7, 9, 3, 1], 12)
])
def test_198(nums: List[int], ans: int):
    from leetcode.problem_198 import Solution
    sol = Solution()
    assert sol.rob(nums) == ans


@pytest.mark.parametrize("grid, expect", [
    ([
         ['1', '1', '1', '1', '0'],
         ['1', '1', '0', '1', '0'],
         ['1', '1', '0', '0', '0'],
         ['0', '0', '0', '0', '0'],
     ], 1),
    ([
         ['1', '1', '0', '0', '0'],
         ['1', '1', '0', '0', '0'],
         ['0', '0', '1', '0', '0'],
         ['0', '0', '0', '1', '1'],
     ], 3)
])
def test_200(grid, expect):
    from leetcode.problem_200 import Solution
    sol = Solution()
    assert sol.num_islands(grid) == expect


@pytest.mark.parametrize("num_courses, prerequisites, ans", [
    (2, [], True),
    (2, [[1, 0]], True),
    (3, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False)
])
def test_207(num_courses: int, prerequisites: List[List[int]], ans: bool):
    from leetcode.problem_207 import Solution
    sol = Solution()
    assert sol.can_finish(num_courses, prerequisites) == ans


def test_208():
    from leetcode.problem_208 import Trie
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")


@pytest.mark.parametrize("nums, ans", [
    ([], 0),
    ([0], 0),
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4)
])
def test_213(nums: List[int], ans: int):
    from leetcode.problem_213 import Solution
    sol = Solution()
    assert sol.rob(nums) == ans


@pytest.mark.parametrize("s, ans", [
    ("aacecaaa", "aaacecaaa"),
    ("abcd", "dcbabcd"),
])
def test_214(s: str, ans: str):
    from leetcode.problem_214 import Solution
    sol = Solution()
    assert sol.shortest_palindrome(s) == ans


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
def test_216(n, k, expect):
    from leetcode.problem_216 import Solution
    solution = Solution()
    assert solution.combination_sum3(n, k) == expect


@pytest.mark.parametrize("nums, expect", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([0, 0], [0, 0]),
    ([1, 0], [0, 1]),
    ([1, 0, 2], [0, 2, 0]),
])
def test_238(nums, expect):
    from leetcode.problem_238 import Solution
    sol = Solution()
    assert sol.product_except_self(nums) == expect


@pytest.mark.parametrize("nums, k, ans", [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])
])
def test_239(nums: List[int], k: int, ans: List[int]):
    from leetcode.problem_239 import Solution
    sol = Solution()
    assert sol.max_sliding_window(nums, k) == ans


@pytest.mark.parametrize("matrix, target, ans", [
    ([[1, 2]], 3, False),
    ([
         [1, 4, 7, 11, 15],
         [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]
     ], 5, True),
    ([
         [1, 4, 7, 11, 15],
         [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]
     ], 20, False)
])
def test_240(matrix: List[List[int]], target: int, ans: bool):
    from leetcode.problem_240 import Solution
    sol = Solution()
    assert sol.search_matrix(matrix, target) == ans


@pytest.mark.timeout(1)
@pytest.mark.parametrize("n, ans", [
    (12, 3),
    (13, 2),
    (44, 3)
])
def test_279(n, ans):
    from leetcode.problem_279 import Solution
    sol = Solution()
    assert sol.num_squares_2(n) == ans
    assert sol.num_squares_3(n) == ans


@pytest.mark.parametrize("nums, ans", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0, 0, 0, 1], [1, 0, 0, 0]),
    ([1, 0], [1, 0])
])
def test_283(nums: List[int], ans: List[int]):
    from leetcode.problem_283 import Solution
    sol = Solution()
    sol.move_zeroes(nums)
    assert nums == ans


@pytest.mark.parametrize("nums, ans", [
    ([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12], 6),
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([10, 9, 2, 5, 3, 4], 3)
])
def test_300(nums: List[int], ans: int):
    from leetcode.problem_300 import Solution
    sol = Solution()
    assert sol.length_of_lis(nums) == ans
    assert sol.length_of_lis_1(nums) == ans


@pytest.mark.parametrize("prices, ans", [
    ([1, 2, 3, 0, 2], 3)
])
def test_309(prices: List[int], ans):
    from leetcode.problem_309 import Solution
    sol = Solution()
    assert sol.max_profit(prices) == ans


@pytest.mark.parametrize("board, expect", [
    ([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
     [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]),
    ([[1, 0, 1, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 0]],
     [[0, 0, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 1, 1, 0]]),
])
def test_289(board, expect):
    from leetcode.problem_289 import Solution
    solution = Solution()
    solution.game_of_life(board)
    assert board == expect


@pytest.mark.parametrize("nums, ans", [
    ([3, 1, 5, 8], 167),
    ([1, 3, 5, 8], 160),
    ([1, 0, 1], 2),
])
def test_312(nums: List[int], ans: int):
    from leetcode.problem_312 import Solution
    sol = Solution()
    assert sol.max_coins(nums) == ans


@pytest.mark.timeout(1)
@pytest.mark.parametrize("nums, ans", [
    ([2, 0, 1], [2, 0, 0]),
    ([5, 2, 6, 1], [2, 1, 1, 0]),
    ([(10000 - x) for x in range(10000)], [(9999 - x) for x in range(10000)]),
    ([x for x in range(10000)], [0 for x in range(10000)])
])
def test_315(nums: List[int], ans):
    from leetcode.problem_315 import Solution
    sol = Solution()
    assert sol.count_smaller_1(nums) == ans


@pytest.mark.parametrize("nums, lower, upper, ans", [
    ([-2,5,-1], -2, 2, 3),
])
def test_327(nums: List[int], lower: int, upper: int, ans: int):
    from leetcode.problem_327 import Solution
    sol = Solution()
    assert sol.count_range_sum(nums, lower, upper) == ans


@pytest.mark.parametrize("matrix, ans", [
    ([
         [9, 9, 4],
         [6, 6, 8],
         [2, 1, 1]
     ], 4),
    ([
         [3, 4, 5],
         [3, 2, 6],
         [2, 2, 1]
     ], 4),
    ([], 0),
    ([[]], 0)
])
def test_329(matrix: List[List[int]], ans):
    from leetcode.problem_329 import Solution
    sol = Solution()
    assert sol.longest_increasing_path(matrix) == ans


@pytest.mark.parametrize("words, ans", [
    (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
    (["bat", "tab", "cat"], [[0, 1], [1, 0]])
])
def test_336(words: List[str], ans: List[List[int]]):
    from leetcode.problem_336 import Solution
    sol = Solution()
    assert sol.palindrome_pairs(words) == ans


@pytest.mark.parametrize("n, ans", [
    (2, 1),
    (10, 36)
])
def test_343(n: int, ans: int):
    from leetcode.problem_343 import Solution
    sol = Solution()
    assert sol.integer_break(n) == ans


@pytest.mark.parametrize("s, expect", [
    ([], []),
    (["1"], ["1"]),
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
])
def test_344(s, expect):
    from leetcode.problem_344 import Solution
    sol = Solution()
    sol.reverse_string(s)
    assert s == expect


@pytest.mark.parametrize("nums1, nums2, ans", [
    ([2, 1], [1, 2], [1, 2]),
    ([1, 2, 2, 1], [2, 2], [2, 2]),
])
def test_350(nums1: List[int], nums2: List[int], ans: List[int]):
    from leetcode.problem_350 import Solution
    sol = Solution()
    assert sol.intersect(nums1, nums2) == ans
    assert sol.intersect_1(nums1, nums2) == ans


@pytest.mark.parametrize("matrix, k, ans", [
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
    ([[1, 1, 3, 8, 13], [4, 4, 4, 8, 18], [9, 14, 18, 19, 20],
      [14, 19, 23, 25, 25], [18, 21, 26, 28, 29]], 13, 18)
])
def test_378(matrix, k, ans):
    from leetcode.problem_378 import Solution
    sol = Solution()
    assert sol.kth_smallest_2(matrix, k) == ans


@pytest.mark.parametrize("s, t, ans", [
    ('abc', 'acebxcd', True),
    ("axc", "ahbgdc", False),
    ("acb", "ahbgdc", False),
    ("", "ahbgdc", True),
    ("a", "", False)
])
def test_392(s, t, ans):
    from leetcode.problem_392 import Solution
    sol = Solution()
    assert sol.is_subsequence(s, t) == ans
    assert sol.is_subsequence_2(s, t) == ans


@pytest.mark.parametrize("nums, n, ans", [
    ([7, 2, 5, 10, 8], 1, 32),
    ([7, 2, 5, 10, 8], 2, 18)
])
def test_410(nums: List[int], n: int, ans: int):
    from leetcode.problem_410 import Solution
    sol = Solution()
    assert sol.split_array(nums, n) == ans


@pytest.mark.parametrize("num1, num2, ans", [
    ("0", "0", "0"),
    ("1", "9" * 5000, "1" + "0" * 5000),
    ("98", "9", "107"),
])
def test_415(num1: str, num2: str, ans: str):
    from leetcode.problem_415 import Solution
    sol = Solution()
    assert sol.add_strings(num1, num2) == ans
    assert sol.add_strings_2(num1, num2) == ans
    assert sol.add_strings_3(num1, num2) == ans


@pytest.mark.parametrize("s, p, ans", [
    ("aa", "bb", []),
    ("abab", "ab", [0, 1, 2]),
    ("cbaebabacd", "abc", [0, 6])
])
def test_438(s: str, p: str, ans: List[int]):
    from leetcode.problem_438 import Solution
    sol = Solution()
    assert sol.find_anagrams(s, p) == ans


@pytest.mark.parametrize("s, ans", [
    ("abab", True),
    ("aaa", True),
    ("aba", False),
    ("abcabcabcabc", True),
    ("abcde" * 100 + "abc", False)
])
def test_459(s: str, ans: bool):
    from leetcode.problem_459 import Solution
    sol = Solution()
    assert sol.repeated_substring_pattern(s) == ans
    assert sol.repeated_substring_pattern_1(s) == ans


def test_460():
    from leetcode.problem_460 import LFUCache
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


@pytest.mark.parametrize('grid, ans', [
    ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16),
    ([[1]], 4),
    ([[1, 0]], 4)
])
def test_463(grid, ans):
    from leetcode.problem_463 import Solution
    sol = Solution()
    assert sol.island_perimeter(grid) == ans


@pytest.mark.parametrize("nums, target, expect", [
    ([1, 1, 1, 1, 1], 3, 5),
    ([1, 0], 1, 2),
    ([19, 32, 36, 7, 37, 10, 44, 21, 40, 39, 39, 18, 5, 34, 3, 40, 33, 2, 46,
      46], 29, 5715),
    ([27, 22, 39, 22, 40, 32, 44, 45, 46, 8, 8, 21, 27, 8, 11, 29, 16, 15, 41,
      0], 10, 0)
])
def test_494(nums, target, expect):
    from leetcode.problem_494 import Solution
    solution = Solution()
    assert solution.find_target_sum_ways(nums, target) == expect
    assert solution.dfs(nums, target) == expect
    assert solution.brute_force(nums, target) == expect


@pytest.mark.parametrize('ring, key, ans', [
    ('godding', 'gd', 4),
    ("bcaeea", "ae", 4),
    ('iotfo', 'fioot', 11),
    ('abcad', 'bad', 6),
    ("godding", "godding", 13),
    ("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx", 137)
])
def test_514(ring: str, key: str, ans: int):
    from leetcode.problem_514 import Solution
    sol = Solution()
    assert sol.find_rotate_steps(ring, key) == ans


@pytest.mark.parametrize("nums, ans", [
    ([2, 6, 4, 8, 10, 9, 15], 5),
    ([1, 2, 3, 4], 0),
    ([2, 6, 4], 2),
    ([1], 0),
    ([5, 3, 9, 1, 7, 3, 2, 5], 8),
    ([1, 3, 5, 2], 3)
])
def test_581(nums, ans):
    from leetcode.problem_581 import Solution
    sol = Solution()
    assert sol.find_unsorted_subarray(nums) == ans


@pytest.mark.parametrize("moves, ans", [
    ("UD", True),
    ("LL", False)
])
def test_657(moves: str, ans: bool):
    from leetcode.problem_657 import Solution
    sol = Solution()
    assert sol.judge_circle_2(moves) == ans


@pytest.mark.parametrize("rooms, ans", [
    ([[1, 3], [3, 0, 1], [2], [0]], False),
    ([[1], [2], [3], []], True)
])
def test_841(rooms: List[List[int]], ans: bool):
    from leetcode.problem_841 import Solution
    sol = Solution()
    assert sol.can_visit_all_rooms(rooms) == ans
    assert sol.can_visit_all_rooms_1(rooms) == ans
    assert sol.can_visit_all_rooms_2(rooms) == ans


@pytest.mark.parametrize("nums1, nums2, expect", [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5)
])
def test_median_of_two_sorted_arrays(nums1, nums2, expect):
    pass
    # assert Solution().find_median_sorted_arrays(nums1, nums2) == expect


@pytest.mark.parametrize('nums, ans', [
    ([2, 3, 1, 1, 4, 0, 0, 4, 3, 3], [2, 3, 0, 1, 4, 1, 0, 3, 4, 3]),
    ([4, 2, 5, 7], [4, 5, 2, 7])
])
def test_922(nums: List[int], ans: List[int]):
    from leetcode.problem_922 import Solution
    sol = Solution()
    sol.sort_array_by_parity_ii_2(nums)
    assert nums == ans


@pytest.mark.parametrize("nums, ans", [
    ([1, 2], False),
    ([1, 2, 3], False),
    ([3, 2, 1], False),
    ([3, 5, 5], False),
    ([0, 3, 2, 1], True)
])
def test_941(nums: List[int], ans: bool):
    from leetcode.problem_941 import Solution
    sol = Solution()
    assert sol.valid_mountain_array(nums) == ans
    assert sol.valid_mountain_array_1(nums) == ans


@pytest.mark.parametrize("a, b, res", [(1, 1, "ab"), (1, 4, "bbabb")])
def test_984(a, b, res):
    from leetcode.problem_984 import Solution
    sol = Solution()
    assert sol.str_without_3a3b(a, b) == res


@pytest.mark.parametrize("days, costs, res", [
    ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
],
                         )
def test_983(days, costs, res):
    from leetcode.problem_983 import Solution
    sol = Solution()
    assert sol.min_cost_tickets(days, costs) == res


@pytest.mark.parametrize(
    "root, res",
    [([3, 0, 0], 2), ([0, 3, 0], 3), ([1, 0, 2], 2), ([1, 0, 0, None, 3], 4)],
)
def test_979(root, res):
    from leetcode.problem_979 import Solution
    sol = Solution()
    assert sol.distribute_coins(Converter.list_to_tree(root)) == res


def test_981():
    from leetcode.problem_981 import TimeMap
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
def test_978(li, res):
    from leetcode.problem_978 import Solution
    sol = Solution()
    assert sol.max_turbulence_size(li) == res


@pytest.mark.parametrize("nums, res", [([2, 1, 3], 12)])
def test_982(nums, res):
    from leetcode.problem_982 import Solution
    sol = Solution()
    assert sol.count_triplets(nums) == res


@pytest.mark.parametrize(
    "x, y, bound, res",
    [(2, 3, 10, [2, 3, 4, 5, 7, 9, 10]), (3, 5, 15, [2, 4, 6, 8, 10, 14])],
)
def test_970(x, y, bound, res):
    from leetcode.problem_970 import Solution
    sol = Solution()
    assert sol.powerful_integers(x, y, bound) == res


@pytest.mark.parametrize(
    "a, res",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_977(a, res):
    from leetcode.problem_977 import Solution
    sol = Solution()
    assert sol.sorted_squares(a) == res


@pytest.mark.parametrize(
    "grid, res",
    [
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4),
        ([[0, 1], [2, 0]], 0),
    ],
)
def test_980(grid, res):
    from leetcode.problem_980 import Solution
    sol = Solution()
    assert sol.unique_paths_iii(grid) == res


@pytest.mark.parametrize(
    "a, res",
    [([2, 1, 2], 5), ([1, 2, 1], 0), ([3, 2, 3, 4], 10), ([3, 6, 2, 3], 8)]
)
def test_976(a, res):
    from leetcode.problem_976 import Solution
    sol = Solution()
    assert sol.largest_perimeter(a) == res


@pytest.mark.parametrize("arr, k, res", [([4, 5, 0, -2, -3, 1], 5, 7)])
def test_974(arr, k, res):
    from leetcode.problem_974 import Solution

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
def test_972(s, t, res):
    from leetcode.problem_972 import Solution
    sol = Solution()
    assert sol.is_rational_equal(s, t) == res


@pytest.mark.parametrize("points, k, res", [
    ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
    ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ([[0, 1], [1, 0]], 2, [[0, 1], [1, 0]])
])
def test_973(points, k, res):
    from leetcode.problem_973 import Solution
    sol = Solution()
    assert sol.k_closest(points, k) == res
    assert sol.k_closest_2(points, k) == res


@pytest.mark.parametrize(
    "nums, res", [([3, 2, 4, 1], [3, 4, 2, 3, 2]), ([1, 2, 3], [])]
)
def test_969(nums, res):
    from leetcode.problem_969 import Solution

    assert Solution().pancake_sort(nums) == res


@pytest.mark.parametrize(
    "points, area",
    [
        ([[1, 2], [2, 1], [1, 0], [0, 1]], 2.00000),
        ([[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]], 1.00000),
        ([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]], 0.00000),
    ],
)
def test_963(points, area):
    from leetcode.problem_963 import Solution
    sol = Solution()
    assert sol.min_area_free_rect(points) == area


@pytest.mark.parametrize(
    "x, target, ans", [(3, 19, 5), (5, 501, 8), (100, 200000000, 7)]
)
def test_964(x, target, ans):
    from leetcode.problem_964 import Solution

    assert Solution().least_ops_express_target(x, target) == ans
    assert Solution().least_ops_express_target_2(x, target) == ans


@pytest.mark.parametrize("li, ans", [
    ([1, 2, 3, 3], 3), ([2, 1, 2, 5, 3, 2], 2), ([5, 1, 5, 2, 5, 3, 5, 4], 5)
])
def test_961(li, ans):
    from leetcode.problem_961 import Solution
    s = Solution()

    assert s.repeated_n_times(li) == ans
    assert s.ans(li) == ans
    assert s.ans_2(li) == ans


@pytest.mark.parametrize(
    "arr, ans", [([6, 0, 8, 2, 1, 5], 4), ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7)]
)
def test_962(arr, ans):
    from leetcode.problem_962 import Solution

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
def test_944(arr, ans):
    from leetcode.problem_944 import Solution

    assert Solution().min_deletion_size(arr) == ans
    assert Solution().ans(arr) == ans


@pytest.mark.parametrize("arr, ans", [
    (["ca", "bb", "ac"], 1),
    (["xc", "yb", "za"], 0),
    (["zyx", "wvu", "tsr"], 3),
    (["xga", "xfb", "yfa"], 1),
],
                         )
def test_955(arr, ans):
    from leetcode.problem_955 import Solution

    assert Solution().min_deletion_size(arr) == ans


@pytest.mark.parametrize("arr, ans", [
    (["babca", "bbazb"], 3),
    (["edcba"], 4),
    (["ghi", "def", "abc"], 0)
])
def test_960(arr, ans):
    from leetcode.problem_960 import Solution

    assert Solution().min_deletion_size(arr) == ans


@pytest.mark.parametrize("pushed, popped, ans", [
    ([], [], True),
    ([1, 2], [1, 2, 3], False),
    ([2, 1, 0], [1, 2, 0], True),
    ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
    ([2, 3, 0, 1], [0, 3, 2, 1], True)
])
def test_946(pushed, popped, ans):
    from leetcode.problem_946 import Solution

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
def test_967(n, k, expect):
    from leetcode.problem_967 import Solution

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
def test_791(s, t, ans):
    from leetcode.problem_791 import Solution

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


@pytest.mark.parametrize("nums, target, expect", [
    ([1, 2, 3], 4, 7),
    # ([4, 2, 1], 32, 39882198)
])
def test_377(nums, target, expect):
    from leetcode.problem_377 import Solution
    solution = Solution()
    assert solution.combination_sum4(nums, target) == expect


@pytest.mark.parametrize("jewels, stones, expect", [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0)
])
def test_771(jewels: str, stones: str, expect: int):
    from leetcode.problem_771 import Solution
    assert Solution().num_jewels_in_stones(jewels, stones) == expect


@pytest.mark.parametrize("a, b, c", [
    ("2", "3", "6"),
    ("123", "456", "56088"),
    ("1234567890", "9876543210", "12193263111263526900")
])
def test_43(a: str, b: str, c: str):
    from leetcode.problem_43 import Solution
    assert Solution().multiply(a, b) == c


@pytest.mark.parametrize("tree, expect", [
    ([1, 2, 3], 6),
    ([-10, 9, 20, None, None, 15, 7], 42)
])
def test_124(tree, expect):
    from leetcode.problem_124 import Solution
    sol = Solution()
    # TODO
    # assert s.max_path_sum(Converter.list2tree(tree)) == expect


@pytest.mark.parametrize("board, words, ans", [
    ([
         ['o', 'a', 'a', 'n'],
         ['e', 't', 'a', 'e'],
         ['i', 'h', 'k', 'r'],
         ['i', 'f', 'l', 'v']
     ], ["oath", "pea", "eat", "rain"], ["oath", "eat"]),
    ([["a", "b"], ["a", "a"]],
     ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"],
     ['aba', 'aaa', 'aaab', 'baa', 'aaba'])
])
def test_212(board: List[List[str]], words: List[str], ans: List[str]):
    from leetcode.problem_212 import Solution
    sol = Solution()
    assert sol.find_words(board, words) == ans


@pytest.mark.parametrize("num, target, expect", [
    ("3456237490", 9191, []),
    ("105", 5, ["1*0+5", "10-5"]),
    ("00", 0, ["0+0", "0-0", "0*0"]),
    ("123", 6, ["1+2+3", "1*2*3"])
])
def test_282(num: str, target: int, expect: List[str]):
    from leetcode.problem_282 import Solution
    solution = Solution()
    # assert solution.add_operators(num, target) == expect


@pytest.mark.timeout(2)
@pytest.mark.parametrize("t, expect", [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
])
def test_739(t, expect):
    from leetcode.problem_739 import Solution
    sol = Solution()
    assert sol.aily_temperatures(t) == expect


@pytest.mark.parametrize("grid, expect", [
    ([[2]], 10),
    ([[1, 2], [3, 4]], 34),
    ([[1, 0], [0, 2]], 16),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 32),
    ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 46)
])
def test_892(grid, expect):
    from leetcode.problem_892 import Solution
    assert Solution().surface_area(grid) == expect


@pytest.mark.parametrize("arr, target, expect", [
    ([4, 9, 3], 10, 3),
    ([2, 3, 5], 10, 5),
    ([60864, 25176, 27249, 21296, 20204], 56803, 11361)
])
def test_1300(arr, target, expect):
    from leetcode.problem_1300 import Solution
    sol = Solution()
    assert sol.find_best_value(arr, target) == expect


@pytest.mark.parametrize("arr, expect", [
    ([8, 1, 5, 2, 6], 11),
    ([1, 2, 3], 4)
])
def test_1014(arr, expect):
    from leetcode.problem_1014 import Solution
    sol = Solution()
    assert sol.max_score_sightseeing_pair(arr) == expect


@pytest.mark.parametrize("tasks, n, ans", [
    (["A", "A", "A", "B", "B", "B"], 2, 8),
    (["A", "A", "A", "B", "B", "B"], 0, 6),
    (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16)
])
def test_621(tasks, n, ans):
    from leetcode.problem_621 import Solution
    sol = Solution()
    assert sol.least_interval(tasks, n) == ans


@pytest.mark.parametrize("nums, ans", [
    ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24]),
])
def test_632(nums: List[List[int]], ans: List[int]):
    from leetcode.problem_632 import Solution
    sol = Solution()
    assert sol.smallest_range(nums) == ans
    assert sol.smallest_range_2(nums) == ans


@pytest.mark.parametrize("s, ans", [
    ("abc", 3),
    ("a" * 1000, 500500),
])
def test_647(s, ans):
    from leetcode.problem_647 import Solution
    sol = Solution()
    assert sol.count_substrings(s) == ans


@pytest.mark.parametrize("s, ans", [
    ("00110011", 6),
    ("10101", 4),
    ("", 1)
])
def test_696(s: str, ans: int):
    from leetcode.problem_696 import Solution
    sol = Solution()
    assert sol.count_binary_substrings(s) == ans


@pytest.mark.parametrize("a, b, ans", [
    ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),
    ([0] * 1000, [0] * 1000, 1000)
])
def test_718_maximum_length_of_repeated_subarray(a, b, ans):
    from leetcode.problem_718 import Solution
    assert Solution().find_length_1(a, b) == ans


@pytest.mark.parametrize("graph, ans", [
    ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
    ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
    ([[4], [], [4], [4], [0, 2, 3]], True),
    (
        [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9],
         [1, 5, 7, 8, 9],
         [3, 6, 9],
         [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]], False),
    ([[2, 4], [2, 3, 4], [0, 1], [1], [0, 1], [7], [9], [5], [], [6], [12, 14],
      [], [10], [], [10],
      [19], [18], [], [16], [15], [23], [23], [], [20, 21], [], [], [27], [26],
      [], [], [34],
      [33, 34], [], [31], [30, 31], [38, 39], [37, 38, 39], [36], [35, 36],
      [35, 36], [43], [], [],
      [40], [], [49], [47, 48, 49], [46, 48, 49], [46, 47, 49],
      [45, 46, 47, 48]], False)
])
def test_785(graph: List[List[int]], ans: bool):
    from leetcode.problem_785 import Solution
    sol = Solution()
    assert sol.is_bipartite(graph) == ans


@pytest.mark.parametrize("arr, ans", [
    ([1, 2, 2, 1, 1, 3], True),
    ([1, 2], False),
    ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
])
def test_1207(arr: List[int], ans: bool):
    from leetcode.problem_1207 import Solution
    sol = Solution()
    assert sol.unique_occurrences(arr) == ans


@pytest.mark.parametrize("arr, ans", [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 4, 8, 3, 5, 6, 7]),
    ([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]),
    ([10000, 10000], [10000, 10000])
])
def test_1356(arr: List[int], ans: List[int]):
    from leetcode.problem_1356 import Solution
    sol = Solution()
    assert sol.sort_by_bits(arr) == ans


@pytest.mark.parametrize("nums, ans", [
    ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
    ([6, 5, 4, 8], [2, 1, 0, 3]),
    ([7, 7, 7, 7], [0, 0, 0, 0])
])
def test_1365(nums: List[int], ans: List[int]):
    from leetcode.problem_1365 import Solution
    sol = Solution()
    assert sol.smaller_numbers_than_current(nums) == ans
