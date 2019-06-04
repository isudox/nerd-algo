package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 15. 3Sum
 * https://leetcode.com/problems/3sum/
 * <p>
 * Given an array nums of n integers, are there elements a, b, c in nums
 * such that a + b + c = 0? Find all unique triplets in the array which gives
 * the sum of zero.
 * <p>
 * Note:
 * <p>
 * The solution set must not contain duplicate triplets.
 * <p>
 * Example:
 *
 * <pre>
 *     Given array nums = [-1, 0, 1, 2, -1, -4],
 *
 *     A solution set is:
 *     [
 *       [-1, 0, 1],
 *       [-1, -1, 2]
 *     ]
 * </pre>
 */
public class ThreeSum {

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length < 3) return res;
        Arrays.sort(nums);
        int count = nums.length, i = 0;
        while (nums[i] <= 0 && nums[count - 1] >= 0 && i < count - 2) {
            int j = i + 1;
            int k = count - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[j++], nums[k--]));
                    while (j < k && nums[j] == nums[j - 1]) j++;
                    while (j < k && nums[k] == nums[k + 1]) k--;
                } else if (sum < 0) {
                    j++;
                    while (j < k && nums[j] == nums[j - 1]) j++;
                } else {
                    k--;
                    while (j < k && nums[k] == nums[k + 1]) k--;
                }
            }
            i++;
            while (i < count - 2 && nums[i] == nums[i - 1]) i++;
        }
        return res;
    }
}