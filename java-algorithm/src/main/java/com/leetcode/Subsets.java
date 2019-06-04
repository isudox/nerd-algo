package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 78. Subsets
 * https://leetcode.com/problems/subsets/
 *
 * Given a set of distinct integers, nums,
 * return all possible subsets (the power set).
 *
 * Note: The solution set must not contain duplicate subsets.
 *
 * Example:
 *
 * Input: nums = [1,2,3]
 * Output:
 * [
 *   [3],
 *   [1],
 *   [2],
 *   [1,2,3],
 *   [1,3],
 *   [2,3],
 *   [1,2],
 *   []
 * ]
 */
public class Subsets {

    public List<List<Integer>> subsets(int[] nums) {
        int len = nums.length;
        List<List<Integer>> list = Arrays.asList(new ArrayList<>());
        if (len == 0) {
            return list;
        }

        List<List<Integer>> preList = subsets(Arrays.copyOfRange(nums, 0, len - 1));
        // key tip: deep copy and append new num.
        list = new ArrayList<>(preList);
        for (List<Integer> ele : preList) {
            List<Integer> copy = new ArrayList<>(ele);
            copy.add(nums[len - 1]);
            list.add(copy);
        }

        return list;
    }
}
