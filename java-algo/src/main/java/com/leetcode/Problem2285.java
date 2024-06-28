package com.leetcode;

import java.util.Arrays;

/**
 * 2285. Maximum Total Importance of Roads
 * https://leetcode.com/problems/maximum-total-importance-of-roads/
 */
public class Problem2285 {
    public long maximumImportance(int n, int[][] roads) {
        int[] degrees = new int[n];
        for (int[] r : roads) {
            degrees[r[0]]++;
            degrees[r[1]]++;
        }
        Arrays.sort(degrees);
        long ans = 0;
        for (int i = 0; i < degrees.length; i++) {
            ans += (long) degrees[i] * (i + 1);
        }
        return ans;
    }
}
