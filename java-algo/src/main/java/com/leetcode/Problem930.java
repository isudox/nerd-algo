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
        int sum = 0;
        Map<Integer, Integer> seen = new HashMap<>();
        seen.put(0, 1);
        for (int num : nums) {
            sum += num;
            ans += seen.getOrDefault(sum - goal, 0);
            seen.put(sum, seen.getOrDefault(sum, 0) + 1);
        }
        return ans;
    }
}
