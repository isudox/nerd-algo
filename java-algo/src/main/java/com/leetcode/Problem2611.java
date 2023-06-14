package com.leetcode;

import java.util.Arrays;

/**
 * 2611. Mice and Cheese
 * https://leetcode.com/problems/mice-and-cheese/
 */
public class Problem2611 {
    public int miceAndCheese(int[] reward1, int[] reward2, int k) {
        Integer[] diffs = new Integer[reward1.length];
        for (int i = 0; i < reward1.length; i++) {
            diffs[i] = reward1[i] - reward2[i];
        }
        Arrays.sort(diffs, (a, b) -> b - a);
        int ans = 0;
        for (int r : reward2) {
            ans += r;
        }
        for (int i = 0; i < k; i++) {
            ans += diffs[i];
        }
        return ans;
    }
}
