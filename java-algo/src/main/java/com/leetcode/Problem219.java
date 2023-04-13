package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 219. Contains Duplicate II
 * https://leetcode.com/problems/contains-duplicate-ii/
 */
public class Problem219 {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (i > k) {
                seen.remove(nums[i - k - 1]);
            }
            if (seen.contains(nums[i])) {
                return true;
            }
            seen.add(nums[i]);
        }
        return false;
    }
}
