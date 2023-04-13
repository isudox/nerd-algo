package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 442. Find All Duplicates in an Array
 * https://leetcode.com/problems/find-all-duplicates-in-an-array/
 */
public class Problem442 {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        for (int num : nums) {
            int val = Math.abs(num);
            if (nums[val - 1] < 0) {
                ans.add(val);
            } else {
                nums[val - 1] *= -1;
            }
        }
        return ans;
    }
}
