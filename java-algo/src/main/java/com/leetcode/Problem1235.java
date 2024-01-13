package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;

public class Problem1235 {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        int[][] jobs = new int[n][];
        for (int i = 0; i < n; i++) {
            jobs[i] = new int[]{startTime[i], endTime[i], profit[i]};
        }
        Arrays.sort(jobs, Comparator.comparingInt(a -> a[1]));
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int k = bs(jobs, i - 1, jobs[i - 1][0]);
            dp[i] = Math.max(dp[i - 1], dp[k] + jobs[i - 1][2]);
        }
        return dp[n];
    }

    private int bs(int[][] jobs, int r, int target) {
        int l = 0;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (jobs[mid][1] > target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}
