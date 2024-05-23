package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * 78. Subsets
 * https://leetcode.com/problems/subsets/
 */
public class Problem78 {
    public List<List<Integer>> subsets(int[] nums) {
        int len = nums.length;
        List<List<Integer>> list = Collections.singletonList(new ArrayList<>());
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

    public List<List<Integer>> subsets2(int[] nums) {
        int n = nums.length;
        int limit = 1 << n;
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < limit; i++) {
            int x = i;
            List<Integer> subset = new ArrayList<>();
            for (int num : nums) {
                if ((x & 1) == 1) {
                    subset.add(num);
                }
                x >>= 1;
            }
            ans.add(subset);
        }
        return ans;
    }

}
