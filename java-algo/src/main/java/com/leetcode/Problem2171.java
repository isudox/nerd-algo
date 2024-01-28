package com.leetcode;

import java.util.Arrays;

/**
 * https://leetcode.com/problems/removing-minimum-number-of-magic-beans
 */
public class Problem2171 {
    public long minimumRemoval(int[] beans) {
        Arrays.sort(beans);
        int n = beans.length;
        long sum = 0, maxRemain = 0;
        for (int i = 0; i < n; i++) {
            sum += beans[i];
            maxRemain = Math.max(maxRemain, (long) (n - i) * beans[i]);
        }
        return sum - maxRemain;
    }
}
