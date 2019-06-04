package com.leetcode;

import java.util.Arrays;

/**
 * 16. 3Sum Closest
 * https://leetcode.com/problems/3sum-closest/
 * <p>
 * Given an array nums of n integers and an integer target, find three integers
 * in nums such that the sum is closest to target. Return the sum of the three
 * integers. You may assume that each input would have exactly one solution.
 * <p>
 * Example:
 *
 * <pre>
 *     Given array nums = [-1, 2, 1, -4], and target = 1.
 *
 *     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 * </pre>
 */
public class ThreeSumClosest {
    public int threeSumClosest(int[] nums, int target) {
        int sum = Integer.MAX_VALUE;
        int diff = Integer.MAX_VALUE;
        int count = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < count; i++) {
            int j = i + 1, k = count - 1;
            while (j < k) {
                int curSum = nums[i] + nums[j] + nums[k];
                int curDiff = curSum - target;
                if (curDiff == 0) return curSum;
                diff = Math.abs(diff) < Math.abs(curDiff) ? diff : curDiff;
                sum = target + diff;
                if (curDiff >= 0) {
                    k--;
                    while (j < k && nums[k] == nums[k + 1]) k--;
                } else {
                    j++;
                    while (j < k && nums[j] == nums[j - 1]) j++;
                }
            }
        }
        return sum;
    }
}
