package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1248. Count Number of Nice Subarrays
 * https://leetcode.com/problems/count-number-of-nice-subarrays
 */
public class Problem1248 {
    public int numberOfSubarrays(int[] nums, int k) {
        int ans = 0, n = nums.length;
        int[] presum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            presum[i + 1] = presum[i] + nums[i] % 2;
        }
        Map<Integer, Integer> seen = new HashMap<>();
        seen.put(0, 1);
        for (int i = 1; i <= n; i++) {
            ans += seen.getOrDefault(presum[i] - k, 0);
            seen.put(presum[i], seen.getOrDefault(presum[i], 0) + 1);
        }
        return ans;
    }
}
