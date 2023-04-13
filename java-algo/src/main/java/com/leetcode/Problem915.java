package com.leetcode;

/**
 * 915. Partition Array into Disjoint Intervals
 * https://leetcode.com/problems/partition-array-into-disjoint-intervals/
 */
public class Problem915 {
    public int partitionDisjoint(int[] nums) {
        int[] rmins = new int[nums.length];
        rmins[nums.length - 1] = nums[nums.length - 1];
        for (int i = nums.length - 2; i >= 0; i--) {
            rmins[i] = Math.min(nums[i], rmins[i + 1]);
        }
        int max = nums[0];
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
            if (max <= rmins[i + 1]) {
                return i + 1;
            }
        }
        return 0;
    }
}
