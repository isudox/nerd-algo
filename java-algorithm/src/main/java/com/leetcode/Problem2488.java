package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 2488. Count Subarrays With Median K
 * https://leetcode.com/problems/count-subarrays-with-median-k/
 */
public class Problem2488 {
    public int countSubarrays(int[] nums, int k) {
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < k) {
                nums[i] = -1;
            } else if (nums[i] > k) {
                nums[i] = 1;
            } else {
                nums[i] = 0;
                idx = i + 1;
            }
        }
        int[] presum = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            presum[i + 1] = presum[i] + nums[i];
        }
        int ans = 0;
        Map<Integer, Integer> store = new HashMap<>();
        store.put(0, 1);
        for (int i = 1; i < presum.length; i++) {
            if (i > idx) {
                ans += store.getOrDefault(presum[i], 0);
                ans += store.getOrDefault(presum[i] - 1, 0);
            }
            if (i < idx) {
                store.put(presum[i], store.getOrDefault(presum[i], 0) + 1);
            }
        }
        return ans;
    }
}
