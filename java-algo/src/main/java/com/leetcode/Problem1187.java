package com.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 1187. Make Array Strictly Increasing
 * https://leetcode.com/problems/make-array-strictly-increasing/
 */
public class Problem1187 {
    Map<String, Integer> memo = new HashMap<>();

    public int makeArrayIncreasing(int[] arr1, int[] arr2) {
        Arrays.sort(arr2);
        int ans = dfs(arr1, arr2, 0, -1);
        return ans <= arr2.length ? ans : -1;
    }

    private int dfs(int[] arr1, int[] arr2, int i, int pre) {
        if (i >= arr1.length) {
            return 0;
        }
        String key = String.format("%d-%d", i, pre);
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        int ret = arr2.length + 1;
        // switch
        int j = binSearch(arr2, pre);
        if (j >= 0) {
            ret = Math.min(ret, 1 + dfs(arr1, arr2, i + 1, arr2[j]));
        }
        // not switch
        if (arr1[i] > pre) {
            ret = Math.min(ret, dfs(arr1, arr2, i + 1, arr1[i]));
        }
        memo.put(key, ret);
        return ret;
    }

    private int binSearch(int[] nums, int need) {
        if (nums[nums.length - 1] <= need) {
            return -1;
        }
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] > need) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
