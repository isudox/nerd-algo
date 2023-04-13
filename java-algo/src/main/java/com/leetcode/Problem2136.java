package com.leetcode;

import java.util.Arrays;

/**
 * 2136. Earliest Possible Day of Full Bloom
 * https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
 */
public class Problem2136 {
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        int n = plantTime.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) {
            idx[i] = i;
        }
        Arrays.sort(idx, (a, b) -> Integer.compare(growTime[b], growTime[a]));
        int ans = 0;
        int days = 0;
        for (int i : idx) {
            ans = Math.max(ans, days + plantTime[i] + growTime[i]);
            days += plantTime[i];
        }
        return ans;
    }
}
