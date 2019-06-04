package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * 90. Subsets II
 * https://leetcode.com/problems/subsets-ii/
 *
 * Given a collection of integers that might contain duplicates,
 * nums, return all possible subsets (the power set).
 *
 * Note: The solution set must not contain duplicate subsets.
 *
 * Example:
 *
 * Input: [1,2,2]
 * Output:
 * [
 *   [2],
 *   [1],
 *   [1,2,2],
 *   [2,2],
 *   [1,2],
 *   []
 * ]
 *
 * [] [1] [2] [1, 2]
 */
public class Subsets2 {

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        int len = nums.length;
        List<List<Integer>> list = Collections.singletonList(new ArrayList<>());
        if (len == 0) {
            return list;
        }

        List<List<Integer>> preList = subsetsWithDup(Arrays.copyOfRange(nums, 0, len - 1));
        // key tip: deep copy and append new num.
        list = new ArrayList<>(preList);
        int num = nums[len - 1];
        boolean isDup = isDup(nums, len - 1, num);
        for (List<Integer> ele : preList) {
            if (isDup) {
                // key tip: if previous list contains N num and N < frequency of num in previous nums, then abandon it
                if (Collections.frequency(ele, num) < Collections.frequency(preList.get(preList.size() - 1), num)) {
                    continue;
                }
            }
            List<Integer> copy = new ArrayList<>(ele);
            copy.add(num);
            list.add(copy);
        }
        return list;
    }

    private boolean isDup(int[] nums, int end, int num) {
        for (int i = 0; i < end; i++) {
            if (nums[i] == num) {
                return true;
            }
        }
        return false;
    }
}
