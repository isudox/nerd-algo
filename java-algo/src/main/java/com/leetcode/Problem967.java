package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 967. Numbers With Same Consecutive Differences
 * https://leetcode.com/problems/numbers-with-same-consecutive-differences/
 *
 * Return all non-negative integers of length N such that the absolute difference
 * between every two consecutive digits is K.
 *
 * Note that every number in the answer must not have leading zeros except for the
 * number 0 itself.
 * For example, 01 has one leading zero and is invalid, but 0 is valid.
 *
 * You may return the answer in any order.
 *
 *
 * Example 1:
 *
 *   Input: N = 3, K = 7
 *   Output: [181,292,707,818,929]
 *   Explanation: Note that 070 is not a valid number, because it has leading zeroes.
 *
 * Example 2:
 *
 *   Input: N = 2, K = 1
 *   Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 *
 *
 * Note:
 *
 *   1 <= N <= 9
 *   0 <= K <= 9
 */
public class Problem967 {

    public int[] numsSameConsecDiff(int n, int k) {
        if (n == 1)
            return new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);
        for (int i = 1; i < n; i++)
            list = assemble(list, k);

        return list.parallelStream().mapToInt(Integer::intValue).toArray();
    }

    private List<Integer> assemble(List<Integer> nums, int k) {
        List<Integer> list = new ArrayList<>();
        for (Integer num : nums) {
            int nextDigit = num % 10 + k;
            if (nextDigit < 10) {
                list.add(num * 10 + nextDigit);
            }
            if (num % 10 - k >= 0 && (num % 10 - k) != nextDigit) {
                nextDigit = num % 10 - k;
                list.add(num * 10 + nextDigit);
            }
        }
        return list;
    }
}
