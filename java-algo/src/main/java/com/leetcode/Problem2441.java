package com.leetcode;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * 2441. Largest Positive Integer That Exists With Its Negative
 * https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
 */
public class Problem2441 {
    public int findMaxK(int[] nums) {
        Arrays.sort(nums);
        if (nums.length == 1 || nums[0] > 0 || nums[nums.length - 1] < 0) {
            return -1;
        }
        int ans = -1;
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (num < 0) {
                seen.add(num);
            } else if (seen.contains(-num)) {
                ans = num;
            }
        }
        return ans;
    }
}
