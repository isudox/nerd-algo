package com.leetcode;

/**
 * 1723. Find Minimum Time to Finish All Jobs
 * https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
 *
 * You are given an integer array jobs, where jobs[i] is the amount of time it
 * takes to complete the i^th job.
 *
 * There are k workers that you can assign jobs to. Each job should be assigned
 * to exactly one worker. The working time of a worker is the sum of the time it
 * takes to complete all jobs assigned to them. Your goal is to devise an
 * optimal assignment such that the maximum working time of any worker is
 * minimized.
 *
 * Return the minimum possible maximum working time of any assignment.
 *
 * Example 1:
 *
 * Input: jobs = [3,2,3], k = 3
 * Output: 3
 * Explanation: By assigning each person one job, the maximum time is 3.
 *
 * Example 2:
 *
 * Input: jobs = [1,2,4,7,8], k = 2
 * Output: 11
 * Explanation: Assign the jobs the following way:
 * Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
 * Worker 2: 4, 7 (working time = 4 + 7 = 11)
 * The maximum working time is 11.
 *
 * Constraints:
 *
 * 1 <= k <= jobs.length <= 12
 * 1 <= jobs[i] <= 10^7
 */
public class Problem1723 {
    public int minimumTimeRequired(int[] jobs, int k) {
        int n = jobs.length;
        int size = 1 << n;
        int[] sums = new int[size];
        for (int i = 1; i < size; i++) {
            // x is the zero count after the last 1
            int x = Integer.numberOfTrailingZeros(i);
            int y = i - (1 << x);
            sums[i] = sums[y] + jobs[x];
        }
        // dp[i][j]: the min time while jobs dispatch is j for top i workers
        int[][] dp = new int[k][size];
        for (int i = 0; i < size; i++) {
            dp[0][i] = sums[i];
        }
        for (int i = 1; i < k; i++) {
            for (int j = 0; j < size; j++) {
                int cur = Integer.MAX_VALUE;
                for (int x = j; x != 0; x = (x - 1) & j) {
                    cur = Math.min(cur, Math.max(dp[i - 1][j - x], sums[x]));
                }
                dp[i][j] = cur;
            }
        }
        return dp[k - 1][size - 1];
    }
}
