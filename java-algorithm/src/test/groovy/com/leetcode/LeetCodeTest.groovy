package com.leetcode

import com.common.Converter
import com.common.ListNode
import com.common.TreeNode
import spock.lang.Specification

/**
 * Test algorithms with incomplete cases by Spock.
 */
class LeetCodeTest extends Specification {

    void setup() {}

    void cleanup() {}

    def "1. Two Sum"(int[] nums, int target, int[] result) {
        given:
        def solution = new Problem1()

        expect:
        solution.twoSum1(nums, target) == result
        solution.twoSum2(nums, target) == result

        where:
        nums                           | target | result
        [1, 5, 8, 10, 23, 99] as int[] | 31     | [2, 4] as int[]
        [1, 5, 8, 10, 23, 99] as int[] | 100    | [0, 5] as int[]
        [-1, 0, 5, 10, 15, 8] as int[] | 9      | [0, 3] as int[]
        [-1, -3, -5, 10, 100] as int[] | 110    | [3, 4] as int[]
    }

    def "2. Add Two Numbers"() {
        given:
        def solution = new Problem2()
        def arr1 = [2, 4, 3] as int[]
        def arr2 = [5, 6, 4] as int[]
        def l1 = Converter.convertListNode(arr1)
        def l2 = Converter.convertListNode(arr2)

        when:
        def res1 = solution.addTwoNumbers1(l1, l2)
        def res2 = solution.addTwoNumbers2(l1, l2)
        def expected = Converter.convertListNode([7, 0, 8] as int[])

        then:
        Converter.convertArray(expected) == Converter.convertArray(res1)
        Converter.convertArray(expected) == Converter.convertArray(res2)
    }

    def "3. Longest Substring Without Repeating Characters"(String s, int len) {
        given:
        def solution = new Problem3()

        expect:
        solution.lengthOfLongestSubstring(s) == len

        where:
        s          | len
        "abcabcbb" | 3
        "bbbbb"    | 1
        "pwwkew"   | 3
    }

    def "23. Merge k Sorted Lists"() {
        given:
        def solution = new Problem23()
        def i1 = [1, 4, 5] as int[]
        def i2 = [1, 3, 4] as int[]
        int[] i3 = [2, 6]
        def l1 = Converter.convertListNode(i1)
        def l2 = Converter.convertListNode(i2)
        def l3 = Converter.convertListNode(i3)

        when:
        def res = solution.mergeKLists([l1, l2, l3] as ListNode[])

        then:
        Converter.convertArray(res) == [1, 1, 2, 3, 4, 4, 5, 6] as int[]
    }

    def "25. Reverse Nodes in k-Group"(int[] nums, int k, int[] res) {
        given:
        def solution = new Problem25()
        def node = Converter.convertListNode(nums)

        expect:
        Converter.convertArray(solution.reverseKGroup(node, k)) == res

        where:
        nums                     | k | res
        [1] as int[]             | 3 | [1] as int[]
        [1, 2, 3, 4, 5] as int[] | 1 | [1, 2, 3, 4, 5] as int[]
        [1, 2, 3, 4, 5] as int[] | 2 | [2, 1, 4, 3, 5] as int[]
        [1, 2, 3, 4, 5] as int[] | 3 | [3, 2, 1, 4, 5] as int[]
    }

    def "32. Longest Valid Parentheses"(String s, int len) {
        given:
        def solution = new Problem32()

        expect:
        solution.longestValidParentheses(s) == len
        solution.longestValidParentheses2(s) == len

        where:
        s           | len
        ""          | 0
        "()"        | 2
        "((()"      | 2
        "(()()"     | 4
        "(()()(()"  | 4
        ")()())"    | 4
        "(()))())(" | 4
        "()(()))))" | 6
    }

    def "33. Search in Rotated Sorted Array"(int[] nums, int target, int res) {
        given:
        def solution = new Problem33()

        expect:
        solution.search1(nums, target) == res
        solution.search2(nums, target) == res

        where:
        nums                  | target | res
        []                    | 1      | -1
        [1]                   | 1      | 0
        [1, 3]                | 3      | 1
        [4, 5, 6, 7, 0, 1, 2] | 0      | 4
        [4, 5, 6, 7, 0, 1, 2] | 3      | -1
    }

    def "34. Find First and Last Position of Element in Sorted Array"(int[] nums, int target, int[] res) {
        given:
        def solution = new Problem34()

        expect:
        solution.searchRange(nums, target) == res

        where:
        nums                         | target | res
        [5, 7, 7, 8, 8, 10] as int[] | 8      | [3, 4] as int[]
        [5, 7, 7, 8, 8, 10] as int[] | 6      | [-1, -1] as int[]
    }

    def "35. Search Insert Position"(int[] nums, int target, int res) {
        given:
        def solution = new Problem35()

        expect:
        solution.searchInsert(nums, target) == res

        where:
        nums         | target | res
        []           | 9      | 0
        [1]          | 2      | 1
        [1, 3, 5, 6] | 5      | 2
        [1, 3, 5, 6] | 2      | 1
        [1, 3, 5, 6] | 7      | 4
        [1, 3, 5, 6] | 0      | 0
    }

    def "36. Valid Sudoku"(char[][] board, boolean res) {
        given:
        def solution = new Problem36()

        expect:
        res == solution.isValidSudoku(board)

        where:
        board                                           | res
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]] | false
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]] | true
    }

    def "39. Combination Sum"(int[] candidates, int target, List<List<Integer>> ans) {
        given:
        def solution = new Problem39()

        expect:
        solution.combinationSum(candidates, target) == ans

        where:
        candidates   | target | ans
        [2, 3, 6, 7] | 7      | [[2, 2, 3], [7]]
        [2, 3, 5]    | 8      | [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    }

    def "40. Combination Sum II"(int[] candidates, int target, List<List<Integer>> expect) {
        given:
        def solution = new Problem40()

        expect:
        solution.combinationSum2(candidates, target) == expect

        where:
        candidates             | target | expect
        [10, 1, 2, 7, 6, 1, 5] | 8      | [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        [2, 5, 2, 1, 2]        | 5      | [[1, 2, 2], [5]]
    }

    def "41. First Missing Positive"(int[] nums, int expect) {
        given:
        def solution = new Problem41()
        expect:
        solution.firstMissingPositive(nums) == expect
        where:
        nums              | expect
        [1, 2, 0]         | 3
        [3, 4, -1, 1]     | 2
        [7, 8, 9, 11, 12] | 1
    }

    def "42. Trapping Rain Water"(int[] height, int expect) {
        given:
        def solution = new Problem42()
        expect:
        solution.trap(height) == expect
        where:
        height                               | expect
        [3, 2, 1, 2, 1]                      | 1
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] | 6
    }

    def "44. Wildcard Matching"(String s, String p, boolean ans) {
        given:
        def sol = new Problem44()
        expect:
        sol.isMatch(s, p) == ans
        where:
        s       | p       | ans
        "acdcb" | "a*c?b" | false
        "adceb" | "*a*b"  | true
        "cb"    | "?a"    | false
        "aa"    | "*"     | true
        "aa"    | "a"     | false
    }

    def "46. Permutations"(int[] nums, List<List<Integer>> expect) {
        given:
        def solution = new Problem46()
        expect:
        solution.permute(nums) == expect
        where:
        nums      | expect
        [1, 2, 3] | [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
    }

    def "53. Maximum Subarray"(int[] nums, int expect) {
        given:
        def solution = new Problem53()
        expect:
        solution.maxSubArray(nums) == expect
        where:
        nums                            | expect
        [-2]                            | -2
        [-2, -1]                        | -1
        [-2, 1, -3, 4, -1, 2, 1, -5, 4] | 6
    }

    def "63. Unique Paths II"(int[][] grid, int ans) {
        given:
        def sol = new Problem63()
        expect:
        sol.uniquePathsWithObstacles(grid) == ans
        where:
        grid        | ans
        [[1]]       | 0
        [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]] | 2
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]] | 6
    }

    def "64. Minimum Path Sum"(int[][] grid, int ans) {
        given:
        def sol = new Problem64()
        expect:
        sol.findPathSum(grid) == ans
        where:
        grid        | ans
        [[1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]] | 7
    }

    def "70. Climbing Stairs"(int n, int expect) {
        given:
        def solution = new Problem70()
        expect:
        solution.climbStairs(n) == expect
        where:
        n  | expect
        3  | 3
        10 | 89
    }

    def "78. Subsets"(int[] nums, List<List<Integer>> expect) {
        given:
        def solution = new Problem78()
        expect:
        solution.subsets(nums) == expect
        where:
        nums      | expect
        []        | [[]]
        [1]       | [[], [1]]
        [1, 2]    | [[], [1], [2], [1, 2]]
        [1, 2, 3] | [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    }

    def "84. Largest Rectangle in Histogram"(int[] heights, int result) {
        given:
        def solution = new Problem84()
        expect:
        solution.largestRectangleArea(heights) == result
        where:
        heights               | result
        [2, 1, 5, 6, 2, 3]    | 10
        [6, 2, 5, 4, 5, 1, 6] | 12
        [2, 2, 2, 2, 2]       | 10
        []                    | 0
    }

    def "90. Subsets II"(int[] nums, List<List<Integer>> expect) {
        given:
        def solution = new Problem90()
        expect:
        solution.subsetsWithDup(nums) == expect
        where:
        nums      | expect
        [2, 2, 2] | [[], [2], [2, 2], [2, 2, 2]]
        [1, 2, 2] | [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    }

    def "96. Unique Binary Search Trees"(int n, int ans) {
        given:
        def sol = new Problem96()
        expect:
        sol.numTrees(n) == ans
        sol.numTrees2(n) == ans
        where:
        n | ans
        3 | 5
        4 | 14
        5 | 42
    }

    def "136. Single Number"(int[] nums, int ans) {
        given:
        def solution = new Problem136()

        expect:
        solution.singleNumber(nums) == ans
        solution.reduce(nums) == ans

        where:
        nums            | ans
        [0]             | 0
        [2, 2, 1]       | 1
        [4, 1, 2, 1, 2] | 4
    }

    def "152. Maximum Product Subarray"(int[] nums, int ans) {
        given:
        def sol = new Problem152()
        expect:
        sol.maxProduct(nums) == ans
        where:
        nums          | ans
        [0, 2]        | 2
        [2, 3, -2, 4] | 6
        [-2, 0, -1]   | 0
    }

    def "167. Two Sum II - Input array is sorted"(int[] nums, int target, int[] ans) {
        given:
        def sol = new Problem167()
        expect:
        sol.twoSum(nums, target) == ans
        where:
        nums           | target | ans
        [2, 7, 11, 15] | 9      | [1, 2]
    }

    def "206. Reverse Linked List"(int[] input, int[] output) {
        given:
        def sol = new Problem206()
        expect:
        ListNode node = sol.reverseList(Converter.convertListNode(input))
        Converter.convertArray(node) == output
        where:
        input           | output
        [1, 2, 3, 4, 5] | [5, 4, 3, 2, 1]
        [1]             | [1]
    }

    def "216. Combination Sum III"(int k, int n, List<List<Integer>> expect) {
        given:
        def solution = new Problem216()

        expect:
        solution.combinationSum3(k, n) == expect

        where:
        k | n  || expect
        2 | 6  || [[1, 5], [2, 4]]
        3 | 7  || [[1, 2, 4]]
        3 | 9  || [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        5 | 18 || [[1, 2, 3, 4, 8], [1, 2, 3, 5, 7], [1, 2, 4, 5, 6]]
    }

    def "279. Perfect Squares"(int n, int ans) {
        given:
        def sol = new Problem279()
        expect:
        sol.numSquares(n) == ans
        sol.numSquares2(n) == ans
        where:
        n      | ans
        1      | 1
        12     | 3
        13     | 2
        9999   | 4
        999999 | 4
    }

    def "312. Burst Balloons"(int[] nums, int ans) {
        given:
        def sol = new Problem312()
        expect:
        sol.maxCoins(nums) == ans
        where:
        nums         | ans
        [3, 1, 5, 8] | 167
        [1, 3, 5, 8] | 160
    }

    def "315. Count of Smaller Numbers After Self"(int[] nums, int[] ans) {
        given:
        def sol = new Problem315()
        expect:
        Converter.collToArr(sol.countSmaller(nums)) == ans
        where:
        nums         | ans
        [5, 2, 6, 1] | [2, 1, 1, 0]
    }

    def "329. Longest Increasing Path in a Matrix"(int[][] matrix, int ans) {
        given:
        def sol = new Problem329()
        expect:
        sol.longestIncreasingPath(matrix) == ans
        where:
        matrix      | ans
        [[9, 9, 4],
         [6, 6, 8],
         [2, 1, 1]] | 4
        [[3, 4, 5],
         [3, 2, 6],
         [2, 2, 1]] | 4
        []          | 0
        [[]]        | 0
    }

    def "350. Intersection of Two Arrays II"(int[] nums1, int[] nums2, int[] ans) {
        given:
        def sol = new Problem350()
        expect:
        sol.intersect(nums1, nums2) == ans
        sol.intersect1(nums1, nums2) == ans
        where:
        nums1        | nums2  | ans
        [2, 1]       | [1, 2] | [1, 2]
        [1, 2, 2, 1] | [2, 2] | [2, 2]
    }

    def "392. Is Subsequence"(String s, String t, boolean ans) {
        given:
        def sol = new Problem392()
        expect:
        sol.isSubsequence(s, t) == ans
        where:
        s     | t        | ans
        "abc" | "ahbgdc" | true
        "axc" | "ahbgdc" | false
        "acb" | "ahbgdc" | false
    }

    def "494. Target Sum"(int[] nums, int s, int expect) {
        given:
        def solution = new Problem494()
        expect:
        solution.findTargetSumWays1(nums, s) == expect
        solution.findTargetSumWays2(nums, s) == expect
        solution.findTargetSumWays3(nums, s) == expect
        where:
        nums                                                                         | s  | expect
        [1, 1, 1, 1, 1]                                                              | 3  | 5
        [27, 22, 39, 22, 40, 32, 44, 45, 46, 8, 8, 21, 27, 8, 11, 29, 16, 15, 41, 0] | 10 | 0
        [19, 32, 36, 7, 37, 10, 44, 21, 40, 39, 39, 18, 5, 34, 3, 40, 33, 2, 46, 46] | 29 | 5715
    }

    def "560. Subarray Sum Equals K"(int[] nums, int k, int ans) {
        given:
        def sol = new Problem560()
        expect:
        sol.subarraySum(nums, k) == ans
        where:
        nums        | k | ans
        [1, 1, 1]   | 2 | 2
        [1] * 20000 | 1 | 20000
    }

    def "581. Shortest Unsorted Continuous Subarray"(int[] nums, int ans) {
        given:
        def sol = new Problem581()
        expect:
        sol.findUnsortedSubarray(nums) == ans
        where:
        nums                     | ans
        [2, 6, 4, 8, 10, 9, 15]  | 5
        [1, 2, 3, 4]             | 0
        [2, 6, 4]                | 2
        [1]                      | 0
        [5, 3, 9, 1, 7, 3, 2, 5] | 8
        [1, 3, 5, 2]             | 3
    }

    def "785. Is Graph Bipartite"(int[][] graph, boolean ans) {
        given:
        def sol = new Problem785()
        expect:
        sol.isBipartite(graph) == ans
        where:
        graph                                  | ans
        [[]]                                   | true
        [[1, 3], [0, 2], [1, 3], [0, 2]]       | true
        [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]] | false
    }

    def "791. Custom Sort String"(String s, String t, String ans) {
        given:
        def solution = new Problem791()

        expect:
        solution.customSortString(s, t) == ans

        where:
        s      | t       | ans
        "cba"  | "abcd"  | "cbad"
        "abc"  | "badef" | "abdef"
        ""     | "abc"   | "abc"
        "def"  | "cba"   | "cba"
        "kqep" | "pekeq" | "kqeep"
    }

    def "946. Validate Stack Sequences"(int[] pushed, int[] popped, boolean ans) {
        given:
        def solution = new Problem946()

        expect:
        solution.validateStackSequences(pushed, popped) == ans
        solution.ans(pushed, popped) == ans

        where:
        pushed          | popped          | ans
        []              | []              | true
        [1, 2]          | [1, 2, 3]       | false
        [2, 1, 0]       | [1, 2, 0]       | true
        [1, 2, 3, 4, 5] | [4, 5, 3, 2, 1] | true
        [1, 2, 3, 4, 5] | [4, 3, 5, 1, 2] | false
        [2, 3, 0, 1]    | [0, 3, 2, 1]    | true
    }

    def "961. N-Repeated Element in Size 2N Array"(int[] arr, int ans) {
        given:
        def solution = new Problem961()

        expect:
        solution.repeatedNTimes(arr) == ans

        where:
        arr                      | ans
        [1, 2, 3, 3]             | 3
        [2, 1, 2, 5, 3, 2]       | 2
        [5, 1, 5, 2, 5, 3, 5, 4] | 5
    }

    def "962. Maximum Width Ramp"(int[] arr, int ans) {
        given:
        def solution = new Problem962()

        expect:
        solution.maxWidthRamp(arr) == ans

        where:
        arr                            | ans
        [6, 0, 8, 2, 1, 5]             | 4
        [9, 8, 1, 0, 1, 9, 4, 0, 4, 1] | 7
    }

    def "963. Minimum Area Rectangle II"(int[][] points, double ans) {
        given:
        def solution = new Problem963()

        expect:
        solution.minAreaFreeRect(points) == ans

        where:
        points                                   | ans
        [[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]] | 0.0
        [[1, 2], [2, 1], [1, 0], [0, 1]]         | 2.0
        [[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]] | 1.0
    }

    def "964. Least Operators to Express Number"(int x, int target, int ans) {
        given:
        def solution = new Problem964()

        expect:
        solution.leastOpsExpressTarget(x, target) == ans

        where:
        x   | target    | ans
        3   | 19        | 5
        5   | 501       | 8
        100 | 200000000 | 7
    }

    def "967. Numbers With Same Consecutive Differences"(int n, int k, int[] ans) {
        given:
        def solution = new Problem967()

        expect:
        solution.numsSameConsecDiff(n, k) == ans

        where:
        n | k || ans
        1 | 0 || [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        1 | 9 || [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        3 | 7 || [181, 292, 707, 818, 929]
        2 | 1 || [12, 10, 23, 21, 34, 32, 45, 43, 56, 54, 67, 65, 78, 76, 89, 87, 98]
    }

    def "969. Pancake Sorting"(int[] nums, Integer[] res) {
        given:
        def solution = new Problem969()

        expect:
        Converter.collToArr(solution.pancakeSort(nums)) == res

        where:
        nums         | res
        [3, 2, 4, 1] | [3, 4, 2, 3, 2]
        [1, 2, 3]    | []
    }

    def "974. Subarray Sums Divisible by K"(int[] A, int K, int res) {
        given:
        def solution = new Problem974()

        expect:
        solution.subarraysDivByK(A, K) == res

        where:
        A                    | K | res
        [1, 2, 3, 4, 5]      | 5 | 4
        [4, 5, 0, -2, -3, 1] | 5 | 7
    }

    def "976. Largest Perimeter Triangle"(int[] A, int res) {
        given:
        def solution = new Problem976()

        expect:
        solution.largestPerimeter(A) == res

        where:
        A            | res
        [2, 1, 2]    | 5
        [1, 2, 1]    | 0
        [3, 2, 3, 4] | 10
        [3, 6, 2, 3] | 8
    }

    def "977. Squares of a Sorted Array"(int[] A, int[] res) {
        given:
        def solution = new Problem977()

        expect:
        solution.sortedSquares2(A) == res

        where:
        A                  | res
        [-4, -1, 0, 3, 10] | [0, 1, 9, 16, 100]
        [-7, -3, 2, 3, 11] | [4, 9, 9, 49, 121]
    }

    def "979. Distribute Coins in Binary Tree"(TreeNode root, int res) {
        given:
        def solution = new Problem979()

        expect:
        solution.distributeCoins(root) == res

        where:
        root | res
        null | 0
    }

    def "980. Unique Paths III"(int[][] grid, int res) {
        given:
        def solution = new Problem980()

        expect:
        solution.uniquePathsIII(grid) == res

        where:
        grid                                        | res
        [[1, 2], [0, 0]]                            | 1
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]] | 2
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]  | 4
    }

    def "982. Triples with Bitwise AND Equal To Zero"(int[] nums, int res) {
        given:
        def solution = new Problem982()

        expect:
        solution.countTriplets(nums) == res

        where:
        nums      | res
        [2, 1, 3] | 12
    }

    def "983. Minimum Cost For Tickets"(int[] days, int[] costs, int res) {
        given:
        def solution = new Problem983()

        expect:
        solution.mincostTickets(days, costs) == res

        where:
        days                                    | costs      | res
        [1, 4, 6, 7, 8, 20]                     | [2, 7, 15] | 11
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31] | [2, 7, 15] | 17
    }

    def "984. String Without AAA or BBB"(int A, int B, String res) {
        given:
        def solution = new Problem984()

        expect:
        solution.strWithout3a3b(A, B) == res

        where:
        A | B || res
        1 | 1 || "ab"
        1 | 2 || "bba"
        4 | 1 || "aabaa"
    }

    def "1014. Best Sightseeing Pair"(int[] arr, int result) {
        given:
        def sol = new Problem1014()

        expect:
        sol.maxScoreSightseeingPair(arr) == result

        where:
        arr             | result
        [1, 2]          | 2
        [5, 3, 1]       | 7
        [8, 1, 5, 2, 6] | 11
    }
}
