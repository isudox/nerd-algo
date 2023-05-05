package com.leetcode;

/**
 * 2432. The Employee That Worked on the Longest Task
 * https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/
 */
public class Problem2432 {
    public int hardestWorker(int n, int[][] logs) {
        int ans = 0, maxTime = 0, startTime = 0;
        for (int[] log : logs) {
            int worker = log[0], endTime = log[1];
            int time = endTime - startTime;
            startTime = endTime;
            if (time > maxTime || (time == maxTime && ans > worker)) {
                maxTime = time;
                ans = worker;
            }
        }
        return ans;
    }
}
