package com.leetcode;

/**
 * 287. Find the Duplicate Number
 * https://leetcode.com/problems/find-the-duplicate-number/
 */
public class Problem287 {
    public int findDuplicate(int[] nums) {
        int[] seen = new int[nums.length];
        for (int num : nums) {
            if (seen[num]++ > 0) {
                return num;
            }
        }
        return 0;
    }
}
