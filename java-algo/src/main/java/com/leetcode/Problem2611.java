package com.leetcode;

import java.util.Arrays;

/**
 * 2611. Mice and Cheese
 * https://leetcode.com/problems/mice-and-cheese/
 */
public class Problem2611 {
    public int miceAndCheese(int[] reward1, int[] reward2, int k) {
        Integer[][] diffTuples = new Integer[reward1.length][2];
        for (int i = 0; i < reward1.length; i++) {
            diffTuples[i][0] = i;
            diffTuples[i][1] = reward1[i] - reward2[i];
        }
        Arrays.sort(diffTuples, (a, b) -> b[1] - a[1]);
        int ans = 0;
        for (int r : reward2) {
            ans += r;
        }
        for (int i = 0; i < k; i++) {
            ans += diffTuples[i][1];
        }
        return ans;
    }
}
