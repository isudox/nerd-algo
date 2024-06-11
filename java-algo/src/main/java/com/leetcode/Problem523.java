package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 523. Continuous Subarray Sum
 * https://leetcode.com/problems/continuous-subarray-sum/
 */
class Problem523 {
    public boolean checkSubarraySum2(int[] nums, int k) {
        Map<Integer, Integer> store = new HashMap<>();
        store.put(0, -1);
        for (int i = 0; i < nums.length; i++) {
            nums[i] = (nums[i] + (i == 0 ? 0 : nums[i - 1])) % k;
            if (store.containsKey(nums[i])) {
                if (i - store.get(nums[i]) >= 2) {
                    return true;
                }
            } else {
                store.put(nums[i], i);
            }
        }
        return false;
    }
}
