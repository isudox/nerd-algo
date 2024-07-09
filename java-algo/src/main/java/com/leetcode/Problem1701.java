package com.leetcode;

/**
 * 1701. Average Waiting Time
 * https://leetcode.com/problems/average-waiting-time/
 */
public class Problem1701 {
    public double averageWaitingTime(int[][] customers) {
        long curTime = 0, totalTime = 0;
        for (int[] c : customers) {
            int start = c[0], cost = c[1];
            if (curTime >= start) {
                curTime += cost;
                totalTime += curTime - start;
            } else {
                totalTime += cost;
                curTime = start + cost;
            }
        }
        return (double) totalTime / customers.length;
    }
}
