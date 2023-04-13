package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1695. Maximum Erasure Value
 * https://leetcode.com/problems/maximum-erasure-value/
 */
public class Problem1695 {
    public int maximumUniqueSubarray(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        int sum = 0, ans = 0;
        for (int r = 0, l = 0; r < nums.length; r++) {
            sum += nums[r];
            int cnt = counter.getOrDefault(nums[r], 0);
            counter.put(nums[r], cnt + 1);
            while (counter.get(nums[r]) > 1) {
                sum -= nums[l];
                counter.put(nums[l], counter.get(nums[l]) - 1);
                l++;
            }
            ans = Math.max(ans, sum);
        }
        return ans;
    }
}
