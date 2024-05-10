package com.leetcode;

import java.util.Arrays;

/**
 * 3075. Maximize Happiness of Selected Children
 * https://leetcode.com/problems/maximize-happiness-of-selected-children/
 */
public class Problem3075 {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        long ans = 0;
        int n = happiness.length;
        for (int i = n - 1; i >= n - k && happiness[i] > n - 1 - i; i--) {
            ans += happiness[i] - (n - 1 - i);
        }
        return ans;
    }
}
