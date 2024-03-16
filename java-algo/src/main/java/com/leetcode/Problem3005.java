package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 3005. Count Elements With Maximum Frequency
 */
public class Problem3005 {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        int maxCnt = 0, ans = 0;
        for (int cnt : counts.values()) {
            if (cnt > maxCnt) {
                maxCnt = cnt;
                ans = 1;
            } else if (cnt == maxCnt) {
                ans++;
            }
        }
        return maxCnt * ans;
    }
}
