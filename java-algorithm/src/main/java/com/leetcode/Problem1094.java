package com.leetcode;

/**
 * 1094. Car Pooling
 * https://leetcode.com/problems/car-pooling/
 */
public class Problem1094 {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] picks = new int[1001];
        for (int[] t : trips) {
            picks[t[1]] += t[0];
            picks[t[2]] -= t[0];
        }
        int cnt = 0;
        for (int pick : picks) {
            cnt += pick;
            if (cnt > capacity) {
                return false;
            }
        }
        return true;
    }
}
