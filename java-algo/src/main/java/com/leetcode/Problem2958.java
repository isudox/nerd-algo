package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 2958. Length of Longest Subarray With at Most K Frequency
 * https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
 */
public class Problem2958 {
    public int maxSubarrayLength(int[] nums, int k) {
        int ans = 0;
        Map<Integer, Integer> frequency = new HashMap<>();
        for (int i = -1, j = 0; j < nums.length; j++) {
            frequency.put(nums[j], frequency.getOrDefault(nums[j], 0) + 1);
            while (frequency.get(nums[j]) > k) {
                i++;
                frequency.put(nums[i], frequency.get(nums[i]) - 1);
            }
            ans = Math.max(ans, j - i);
        }
        return ans;
    }
}
