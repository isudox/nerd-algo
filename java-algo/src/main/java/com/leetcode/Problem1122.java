package com.leetcode;

import java.util.*;

/**
 * 1122. Relative Sort Array
 * https://leetcode.com/problems/relative-sort-array/
 */
public class Problem1122 {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < arr2.length; i++) {
            map.put(arr2[i], i);
        }
        Integer[] nums = new Integer[arr1.length];
        for (int i = 0; i < arr1.length; i++) {
            nums[i] = arr1[i];
            if (!map.containsKey(arr1[i])) {
                map.put(arr1[i], arr2.length + arr1[i]);
            }
        }
        Arrays.sort(nums, Comparator.comparingInt(map::get));
        for (int i = 0; i < nums.length; i++) {
            arr1[i] = nums[i];
        }
        return arr1;
    }
}
