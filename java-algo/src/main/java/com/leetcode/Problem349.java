package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 349. Intersection of Two Arrays
 * https://leetcode.com/problems/intersection-of-two-arrays/
 */
public class Problem349 {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> nums = new HashSet<>();
        for (int num : nums1) {
            nums.add(num);
        }
        Set<Integer> seen = new HashSet<>();
        for (int num : nums2) {
            if (nums.contains(num)) {
                seen.add(num);
            }
        }
        int[] ans = new int[seen.size()];
        int i = 0;
        for (int num : seen) {
            ans[i++] = num;
        }
        return ans;
    }
}
