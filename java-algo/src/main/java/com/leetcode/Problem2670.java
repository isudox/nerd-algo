package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * https://leetcode.com/problems/find-the-distinct-difference-array
 */
public class Problem2670 {
    public int[] distinctDifferenceArray(int[] nums) {
        int[] diff = new int[nums.length];
        Map<Integer, Integer> left = new HashMap<>(), right = new HashMap<>();
        for (int num : nums) {
            right.put(num, right.getOrDefault(num, 0) + 1);
        }
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            left.put(num, left.getOrDefault(num, 0) + 1);
            right.put(num, right.get(num) - 1);
            if (right.get(num) == 0) {
                right.remove(num);
            }
            diff[i] = left.size() - right.size();
        }
        return diff;
    }
}
