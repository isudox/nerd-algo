package com.leetcode.solution;

import java.util.HashMap;
import java.util.Map;

/**
 * 1. Two Sum
 * https://leetcode.com/problems/two-sum/
 * <p>
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 * <p>
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * <p>
 * Example:
 * <pre>
 *     Given nums = [2, 7, 11, 15], target = 9,
 *
 *     Because nums[0] + nums[1] = 2 + 7 = 9,
 *     return [0, 1].
 * </pre>
 */
public class TwoSum {
    /**
     * The nerd approach.
     */
    public int[] twoSum1(int[] nums, int target) {
        int len = nums.length;
        int[] res = new int[2];

        if (len < 2) {
            return res;
        }

        for (int i = 0; i < len; i++) {
            for (int j = i + 1; j < len; j++) {
                if (nums[i] + nums[j] == target) {
                    res[0] = i;
                    res[1] = j;
                    break;
                }
            }
        }

        return res;
    }

    /**
     * Faster approach using a HashMap.
     */
    public int[] twoSum2(int[] nums, int target) {
        int[] res = new int[2];
        int i = 0, len = nums.length;
        Map<Integer, Integer> map = new HashMap<>(len);

        for (; i < len; i++) {
            if (map.containsKey(target - nums[i])) {
                res[0] = map.get(target - nums[i]);
                res[1] = i;
            } else {
                map.put(nums[i], i);
            }
        }

        return res;
    }
}
