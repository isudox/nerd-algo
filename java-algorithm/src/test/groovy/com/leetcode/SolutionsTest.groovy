package com.leetcode

import spock.lang.Specification

/**
 * Test algorithms with incomplete cases by Spock.
 */
class SolutionsTest extends Specification {

    void setup() {}

    void cleanup() {}

    def "two sum"(int[] nums, int target, int[] result) {
        given:
        def solution = new TwoSum()

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

    def "add two numbers"() {
        given:
        def solution = new AddTwoNumbers()
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

    def "longest substring without repeating characters"() {
        given:
        def solution = new LongestSubstringWithoutRepeatingCharacters()

        when:
        def res = solution.lengthOfLongestSubstring("pwwkew")

        then:
        res == 3
    }

    def "merge k sorted lists"() {
        given:
        def solution = new MergeKSortedLists()
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

    def "reverse nodes in k-group"(int[] nums, int k, int[] res) {
        given:
        def solution = new ReverseNodesInKGroup()
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

    def " longest valid parentheses"(String s, int len) {
        given:
        def solution = new LongestValidParentheses()

        expect:
        solution.longestValidParentheses(s) == len

        where:
        s           | len
        ""          | 0
        "()"        | 2
        "((()"      | 2
        "(()()"     | 4
        "(()()(()"  | 4
        ")()())"    | 4
        "()(()))))" | 6
    }

    def "search in rotated sorted array"(int[] nums, int target, int res) {
        given:
        def solution = new SearchInRotatedSortedArray()

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

    def "find first and last position of element in sorted array"(int[] nums, int target, int[] res) {
        given:
        def solution = new FindFirstAndLastPositionOfElementInSortedArray()

        expect:
        solution.searchRange(nums, target) == res

        where:
        nums                         | target | res
        [5, 7, 7, 8, 8, 10] as int[] | 8      | [3, 4] as int[]
        [5, 7, 7, 8, 8, 10] as int[] | 6      | [-1, -1] as int[]
    }

    def "search insert position"(int[] nums, int target, int res) {
        given:
        def solution = new SearchInsertPosition()

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

    def "valid sudoku"(char[][] board, boolean res) {
        given:
        def solution = new ValidSudoku()

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

    def "distribute-coins-in-binary-tree"(TreeNode root, int res) {
        given:
        def solution = new DistributeCoinsInBinaryTree()

        expect:
        solution.distributeCoins(root) == res

        where:
        root | res
        null | 0
    }

//    def "unique-paths-iii"(int[][] grid, int res) {
//        given:
//        def solution = new UniquePaths3()
//
//        expect:
//        solution.uniquePathsIII(grid) == res
//
//        where:
//        grid                                        | res
//        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]] | 2
//        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]  | 4
//        [[0, 1], [2, 0]]                            | 0
//    }

    def "triples-with-bitwise-and-equal-to-zero"(int[] nums, int res) {
        given:
        def solution = new TriplesWithBitwiseAndEqualToZero()

        expect:
        solution.countTriplets(nums) == res

        where:
        nums      | res
        [2, 1, 3] | 12
    }

    def "min-cost-tickets"(int[] days, int[] costs, int res) {
        given:
        def solution = new MinimumCostForTickets()

        expect:
        solution.mincostTickets(days, costs) == res

        where:
        days                                    | costs      | res
        [1, 4, 6, 7, 8, 20]                     | [2, 7, 15] | 11
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31] | [2, 7, 15] | 17
    }

    def "string-without-3a3b"(int A, int B, String res) {
        given:
        def solution = new StringWithout3aOr3b()

        expect:
        solution.strWithout3a3b(A, B) == res

        where:
        A | B || res
        1 | 1 || "ab"
        1 | 2 || "bba"
        4 | 1 || "aabaa"
    }

    def "unique-paths-iii"(int[][] grid, int res) {
        given:
        def solution = new UniquePaths3()

        expect:
        solution.uniquePathsIII(grid) == res

        where:
        grid                                        | res
        [[1, 2], [0, 0]]                            | 1
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]] | 2
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]  | 4
    }

    def "squares-of-a-sorted-array"(int[] A, int[] res) {
        given:
        def solution = new SquaresOfSortedArray()

        expect:
        solution.sortedSquares2(A) == res

        where:
        A                  | res
        [-4, -1, 0, 3, 10] | [0, 1, 9, 16, 100]
        [-7, -3, 2, 3, 11] | [4, 9, 9, 49, 121]
    }

    def "largest-perimeter-triangle"(int[] A, int res) {
        given:
        def solution = new LargestPerimeterTriangle()

        expect:
        solution.largestPerimeter(A) == res

        where:
        A            | res
        [2, 1, 2]    | 5
        [1, 2, 1]    | 0
        [3, 2, 3, 4] | 10
        [3, 6, 2, 3] | 8
    }

    def "subarray-sums-divisible-by-k"(int[] A, int K, int res) {
        given:
        def solution = new SubarraySumsDivisibleByK()

        expect:
        solution.subarraysDivByK(A, K) == res

        where:
        A                    | K | res
        [1, 2, 3, 4, 5]      | 5 | 4
        [4, 5, 0, -2, -3, 1] | 5 | 7
    }

    def "pancake-sorting"(int[] nums, Integer[] res) {
        given:
        def solution = new PancakeSorting()

        expect:
        Converter.collToArr(solution.pancakeSort(nums)) == res

        where:
        nums         | res
        [3, 2, 4, 1] | [3, 4, 2, 3, 2]
        [1, 2, 3]    | []
    }

    def "least-operators-to-express-number"(int x, int target, int ans) {
        given:
        def solution = new LeastOperatorsToExpressNumber()

        expect:
        solution.leastOpsExpressTarget(x, target) == ans

        where:
        x   | target    | ans
        3   | 19        | 5
        5   | 501       | 8
        100 | 200000000 | 7
    }

    def "minimum-area-rectangle-ii"(int[][] points, double ans) {
        given:
        def solution = new MinimumAreaRectangle2()

        expect:
        solution.minAreaFreeRect(points) == ans

        where:
        points                                   | ans
        [[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]] | 0.0
        [[1, 2], [2, 1], [1, 0], [0, 1]]         | 2.0
        [[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]] | 1.0
    }

    def "n-repeated-element-in-size-2n-array"(int[] arr, int ans) {
        given:
        def solution = new NRepeatedElementInSize2NArray()

        expect:
        solution.repeatedNTimes(arr) == ans

        where:
        arr                      | ans
        [1, 2, 3, 3]             | 3
        [2, 1, 2, 5, 3, 2]       | 2
        [5, 1, 5, 2, 5, 3, 5, 4] | 5
    }

    def "maximum-width-ramp"(int[] arr, int ans) {
        given:
        def solution = new MaximumWidthRamp()

        expect:
        solution.maxWidthRamp(arr) == ans

        where:
        arr                            | ans
        [6, 0, 8, 2, 1, 5]             | 4
        [9, 8, 1, 0, 1, 9, 4, 0, 4, 1] | 7
    }

    def "validate-stack-sequences"(int[] pushed, int[] popped, boolean ans) {
        given:
        def solution = new ValidateStackSequences()

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

    def "numbers-with-same-consecutive-differences"(int n, int k, int[] ans) {
        given:
        def solution = new NumbersWithSameConsecutiveDifferences()

        expect:
        solution.numsSameConsecDiff(n, k) == ans

        where:
        n | k || ans
        1 | 0 || [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        1 | 9 || [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        3 | 7 || [181, 292, 707, 818, 929]
        2 | 1 || [12, 10, 23, 21, 34, 32, 45, 43, 56, 54, 67, 65, 78, 76, 89, 87, 98]
    }

    def "custom-sort-string"(String s, String t, String ans) {
        given:
        def solution = new CustomSortString()

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

    def "single-number"(int[] nums, int ans) {
        given:
        def solution = new SingleNumber()

        expect:
        solution.singleNumber(nums) == ans
        solution.reduce(nums) == ans

        where:
        nums            | ans
        [0]             | 0
        [2, 2, 1]       | 1
        [4, 1, 2, 1, 2] | 4
    }

    def "combination-sum"(int[] candidates, int target, List<List<Integer>> ans) {
        given:
        def solution = new CombinationSum()

        expect:
        solution.combinationSum(candidates, target) == ans

        where:
        candidates   | target | ans
        [2, 3, 6, 7] | 7      | [[2, 2, 3], [7]]
        [2, 3, 5]    | 8      | [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    }

    def "combination-sum-2"(int[] candidates, int target, List<List<Integer>> expect) {
        given:
        def solution = new CombinationSum2()

        expect:
        solution.combinationSum2(candidates, target) == expect

        where:
        candidates             | target | expect
        [10, 1, 2, 7, 6, 1, 5] | 8      | [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        [2, 5, 2, 1, 2]        | 5      | [[1, 2, 2], [5]]
    }

    def "combination-sum-3"(int k, int n, List<List<Integer>> expect) {
        given:
        def solution = new CombinationSum3()

        expect:
        solution.combinationSum3(k, n) == expect

        where:
        k | n  || expect
        2 | 6  || [[1, 5], [2, 4]]
        3 | 7  || [[1, 2, 4]]
        3 | 9  || [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        5 | 18 || [[1, 2, 3, 4, 8], [1, 2, 3, 5, 7], [1, 2, 4, 5, 6]]
    }

    def "maximum-subarray"(int[] nums, int expect) {
        given:
        def solution = new MaximumSubarray()
        expect:
        solution.maxSubArray(nums) == expect
        where:
        nums                            | expect
        [-2]                            | -2
        [-2, -1]                        | -1
        [-2, 1, -3, 4, -1, 2, 1, -5, 4] | 6
    }

    def "trapping-rain-water"(int[] height, int expect) {
        given:
        def solution = new TrappingRainWater()
        expect:
        solution.trap(height) == expect
        where:
        height                               | expect
        [3, 2, 1, 2, 1]                      | 1
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] | 6
    }

    def "subsets"(int[] nums, List<List<Integer>> expect) {
        given:
        def solution = new Subsets()
        expect:
        solution.subsets(nums) == expect
        where:
        nums      | expect
        []        | [[]]
        [1]       | [[], [1]]
        [1, 2]    | [[], [1], [2], [1, 2]]
        [1, 2, 3] | [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    }

    def "subsets-ii"(int[] nums, List<List<Integer>> expect) {
        given:
        def solution = new Subsets2()
        expect:
        solution.subsetsWithDup(nums) == expect
        where:
        nums      | expect
        [2, 2, 2] | [[], [2], [2, 2], [2, 2, 2]]
        [1, 2, 2] | [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    }

    def "first-missing-positive"(int[] nums, int expect) {
        given:
        def solution = new FirstMissingPositive()
        expect:
        solution.firstMissingPositive(nums) == expect
        where:
        nums              | expect
        [1, 2, 0]         | 3
        [3, 4, -1, 1]     | 2
        [7, 8, 9, 11, 12] | 1
    }

    def "permutations"(int[] nums, List<List<Integer>> expect) {
        given:
        def solution = new Permutations()
        expect:
        solution.permute(nums) == expect
        where:
        nums      | expect
        [1, 2, 3] | [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
    }

    def "largest-rectangle-in-histogram"(int[] heights, int result) {
        given:
        def solution = new LargestRectangleInHistogram()
        expect:
        solution.largestRectangleArea(heights) == result
        where:
        heights               | result
        [2, 1, 5, 6, 2, 3]    | 10
        [6, 2, 5, 4, 5, 1, 6] | 12
        [2, 2, 2, 2, 2]       | 10
        []                    | 0
    }
}
