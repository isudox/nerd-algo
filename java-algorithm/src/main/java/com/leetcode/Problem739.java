package com.leetcode;

/**
 * 739. Daily Temperatures
 * https://leetcode.com/problems/daily-temperatures/
 *
 * Given a list of daily temperatures T, return a list such that, for each day
 * in the input, tells you how many days you would have to wait until a warmer
 * temperature. If there is no future day for which this is possible,
 * put 0 instead.
 *
 * For example, given the list of temperatures
 * T = [73, 74, 75, 71, 69, 72, 76, 73],
 * your output should be [1, 1, 4, 2, 1, 1, 0, 0].
 *
 * Note: The length of temperatures will be in the range [1, 30000].
 * Each temperature will be an integer in the range [30, 100].
 */
public class Problem739 {

    public int[] bruteFroce(int[] t) {
        int[] result = new int[t.length];

        for (int i = 0; i < t.length; i++) {
            int count = 0;
            for (int j = i; j < t.length; j++) {
                if (t[j] > t[i]) {
                    break;
                }
                count++;
            }
            if (i + count == t.length) {
                result[i] = 0;
            } else {
                result[i] = count;
            }

        }

        return result;
    }

}
