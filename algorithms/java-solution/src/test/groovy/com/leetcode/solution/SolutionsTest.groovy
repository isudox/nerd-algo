/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2017-2019 sudoz
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

package com.leetcode.solution

import com.leetcode.common.*
import com.leetcode.util.*
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
        def solution = new TriplesWithBitwiseANDEqualToZero()

        expect:
        solution.countTriplets(nums) == res

        where:
        nums                        | res
        [2, 1, 3]                   | 12
        [41816, 11362, 40028, 40141, 46197, 33562, 18640, 57505, 23138, 30034,
         41410, 33824, 62683, 62568, 60932, 61215, 38073, 32125, 46144, 14117,
         17424, 2870, 10673, 253, 42901, 9201, 51555, 44597, 63614, 25985, 60384,
         29733, 22249, 6706, 57857, 52087, 21163, 29867, 21308, 1889, 2906, 24163,
         13735, 34374, 12306, 13213, 44083, 48208, 20462, 56360, 16688, 22540,
         46693, 2916, 61222, 4740, 30207, 47487, 3110, 53018, 64152, 30180, 7741,
         5339, 6470, 50163, 27132, 60242, 28877, 5055, 27979, 49468, 54351, 2578,
         11821, 32113, 8394, 57087, 61240, 20945, 28497, 36507, 18710, 35459,
         13184, 19440, 28952, 39627, 35138, 17104, 15190, 7781, 51347, 6481, 48030,
         16303, 18648, 48239, 43228, 48622, 33769, 56301, 7981, 42283, 7749, 48318,
         23521, 44229, 46103, 43293, 14520, 54512, 15737, 33957, 44213, 15309,
         41190, 18797, 11231, 53067, 36249, 21488, 38366, 1657, 8508, 25924, 63947,
         33454, 5010, 50137, 51212, 50777, 37322, 45593, 13989, 48009, 53488,
         49805, 23164, 38733, 41221, 59035, 7078, 54652, 34500, 23502, 29858, 828,
         14422, 42779, 43309, 32420, 62477, 31517, 20574, 55560, 16984, 39603,
         46099, 53850, 51469, 25171, 3878, 2509, 47609, 63025, 22489, 28914, 47565,
         43111, 17046, 44012, 19982, 23354, 35357, 47992, 9910, 1440, 41145, 1609,
         2946, 14796, 42852, 4361, 4089, 63707, 27698, 58486, 14190, 28522, 23464,
         11595, 21549, 64670, 48975, 25078, 26822, 17284, 34821, 48210, 45000,
         30320, 2748, 60391, 26799, 25578, 203, 9058, 56941, 33681, 48000, 9710,
         21630, 55059, 53782, 16173, 1440, 52852, 11065, 51621, 44804, 11030, 5143,
         60794, 39182, 40665, 29983, 9835, 39450, 16546, 52815, 48019, 1786, 61107,
         2380, 5873, 19184, 9883, 15476, 23318, 48201, 26523, 17684, 32264, 25728,
         20366, 59017, 36074, 64050, 50653, 37388, 17199, 45012, 29879, 47276,
         26462, 32506, 1355, 48493, 2246, 44612, 38142, 50850, 18990, 44964, 13572,
         34686, 22300, 64123, 63692, 13695, 37095, 21590, 63474, 60589, 38413,
         47191, 44651, 23157, 60054, 58946, 21670, 48981, 595, 53500, 37019, 62410,
         23802, 41006, 21168, 51300, 39367, 64714, 66, 9224, 2857, 8247, 60908,
         62167, 31484, 62042, 53633, 51027, 48973, 12298, 35971, 27779, 62245,
         11392, 11131, 43179, 10315, 7212, 33025, 52209, 39652, 49463, 17416,
         18675, 28095, 64936, 47049, 62013, 35249, 36343, 64886, 12451, 51287,
         51872, 55360, 49155, 10179, 43327, 60535, 36915, 23654, 62227, 36804,
         26977, 40247, 52699, 14962, 1028, 34674, 61692, 44581, 41347, 41144,
         32570, 47901, 16331, 58442, 17987, 61927, 60718, 5106, 29371, 48761,
         29468, 33351, 52876, 46202, 62783, 10779, 60526, 60816, 41598, 61629,
         16560, 57788, 50690, 39956, 5939, 1974, 718, 16420, 49961, 25337, 50819,
         41002, 25510, 57681, 2517, 30494, 54385, 8310, 46562, 21503, 1592, 31046,
         34189, 2725, 37088, 22769, 294, 12502, 7262, 35430, 2825, 60826, 55381,
         61951, 20630, 59327, 64507, 50117, 18027, 43967, 39037, 26489, 20060,
         3922, 8217, 8778, 31515, 42067, 50073, 3061, 53985, 2848, 36368, 48768,
         41367, 62238, 22590, 38396, 5426, 36686, 53300, 13212, 17102, 45901,
         16638, 16989, 61309, 65440, 10171, 58993, 36223, 2529, 38371, 42044, 2214,
         49656, 53595, 4695, 42493, 29920, 15644, 30059, 10445, 21867, 42939,
         31226, 36432, 35615, 53778, 22503, 53278, 5242, 28031, 23089, 29594,
         54624, 33580, 64700, 56456, 7788, 20767, 1489, 48087, 1258, 58060, 12670,
         27121, 4065, 20398, 25527, 3423, 50302, 46619, 23454, 54735, 5073, 3539,
         23263, 59103, 49575, 44061, 36879, 52675, 27015, 2011, 52586, 12484,
         25405, 23436, 8084, 22989, 11605, 40371, 42823, 894, 29915, 36310, 57125,
         32507, 5272, 3389, 56499, 51821, 56259, 17186, 42467, 6272, 54170, 21863,
         62596, 30892, 2167, 59575, 40994, 18814, 2411, 24686, 10280, 35932, 9626,
         11443, 60350, 41950, 15897, 57599, 40941, 61970, 31648, 58189, 44462,
         2894, 15747, 18453, 11142, 15609, 14813, 57563, 30336, 57443, 9043, 37022,
         882, 60968, 369, 25552, 52532, 65528, 1278, 54007, 33429, 2502, 50929,
         7333, 40073, 51008, 44144, 24895, 1732, 28590, 59879, 21818, 16250, 9032,
         33439, 34953, 4787, 26722, 43167, 63311, 28281, 28576, 30876, 14747,
         25876, 42288, 26021, 38101, 54760, 65402, 58001, 24366, 1423, 40082,
         31100, 15533, 2641, 21074, 52302, 63184, 6990, 57516, 3192, 46758, 1756,
         27593, 57031, 25762, 60592, 46739, 39595, 10576, 22314, 26941, 38679,
         65276, 18593, 33001, 61174, 22637, 41196, 50209, 41305, 49376, 12824,
         62740, 11593, 38252, 19401, 41577, 19078, 28259, 44710, 17633, 47702,
         22732, 8660, 40182, 10863, 28218, 26109, 4991, 46581, 44618, 50973, 35711,
         36301, 11090, 13596, 14958, 34426, 53672, 23394, 57794, 48226, 46953,
         21965, 7764, 63097, 56007, 26795, 56571, 58931, 22444, 32870, 21744,
         45557, 59779, 64523, 48744, 20004, 57704, 65052, 22709, 62174, 33524,
         63218, 65264, 53276, 44789, 10093, 322, 39024, 46167, 61311, 33889, 45668,
         42425, 13429, 42224, 64338, 7286, 45124, 40259, 24632, 51992, 687, 58485,
         53566, 31503, 7087, 29663, 38289, 16638, 31885, 50838, 60472, 36807,
         54214, 5107, 56122, 60346, 11010, 54230, 55677, 57583, 33891, 39862,
         13636, 46408, 26543, 1387, 8799, 25442, 58011, 37024, 60047, 60914, 5688,
         38549, 21923, 33213, 29853, 31453, 6671, 54601, 32130, 42269, 30977,
         11863, 35455, 10455, 55848, 54500, 9413, 4511, 4488, 25771, 62458, 36447,
         17401, 15050, 7266, 9245, 53206, 9085, 56627, 53936, 8965, 36616, 462,
         56494, 36587, 49501, 32135, 45247, 61029, 36670, 57324, 22481, 6391, 337,
         14853, 54957, 20414, 14720, 32481, 62056, 33356, 22339, 5079, 37595,
         14827, 24084, 24979, 49688, 15180, 61334, 48653, 31530, 57702, 23538,
         25188, 8478, 51023, 26292, 32784, 30865, 43003, 24506, 60021, 28306,
         23541, 26271, 50219, 65080, 56787, 31439, 19094, 29228, 22545, 15960,
         12251, 62644, 32722, 7207, 25159, 25474, 33654, 64227, 64004, 37086,
         40507, 44278, 32913, 31894, 20612, 44821, 6022, 20784, 58391, 14901,
         63411, 64498, 37708, 2650, 6126, 13126, 21417, 7412, 52246, 23865, 15317,
         2863, 25078, 295, 7634, 39626, 61272, 13065, 48566, 12956, 97, 58755,
         55450, 4376, 11608, 15355, 60838, 25030, 52912, 28561, 24985, 50157,
         40354, 17650, 38195, 46127, 54203, 44379, 41992, 39053, 6032, 61943,
         46847, 17882, 45373, 40685, 43178, 24832, 37563, 43255, 13215, 33293,
         7886, 6916, 59707, 8162, 58541, 30788, 29812, 22270, 27277, 24722, 37026,
         21993, 53869, 15306, 16283, 31493, 61281, 1567, 47409, 393, 26532, 50083,
         29234, 28146, 16594, 31135, 14959, 18580, 42814, 39285, 60918, 63495,
         34234, 5738, 19654, 33934, 44116, 62009, 10165, 2404, 57018, 52767, 50184,
         30710, 44419, 26966, 12586, 25617, 51579, 52550, 62988, 58174, 44701,
         34138, 47443, 12006, 60495, 46699, 38960, 28445, 41519, 40480, 58907,
         37403, 13983, 28926, 15923, 59306, 55281, 36426, 12870, 2853, 8792, 29046,
         44184, 14679, 44860, 56488, 49626, 27887, 42318, 64773, 58026, 22160,
         44921, 10696, 36527, 23365, 28714, 28763, 43465, 55443, 30708, 9606,
         49424, 49259, 62511, 25824, 30400, 35428, 58466, 46151, 1394, 13587,
         55960, 38369, 57272, 26961, 13793, 271, 65277, 8937, 42137, 32093, 24913,
         35206, 5130, 63572, 32292] | 113138322
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
}
