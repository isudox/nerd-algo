package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 930. Binary Subarrays With Sum
 * https://leetcode.com/problems/binary-subarrays-with-sum/
 */
public class Problem930 {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int ans = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        counter.put(0, 1);
        int i = 0;
        int preSum = 0;
        while (i < nums.length) {
            preSum += nums[i++];
            if (counter.containsKey(preSum - goal)) {
                ans += counter.get(preSum - goal);
            }
            counter.put(preSum, counter.getOrDefault(preSum, 0) + 1);
        }
        return ans;
    }
}
