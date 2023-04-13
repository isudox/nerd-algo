package com.leetcode;

import java.util.Arrays;

/**
 * 324. Wiggle Sort II
 * https://leetcode.com/problems/wiggle-sort-ii/submissions/
 */
public class Problem324 {
    public void wiggleSort(int[] nums) {
        int n = nums.length;
        int[] arr = Arrays.copyOf(nums, n);
        Arrays.sort(arr);
        int mid = (n + 1) / 2;
        for (int i = 0, j = mid - 1, k = n - 1; i < n; i += 2, j--, k--) {
            nums[i] = arr[j];
            if (i + 1 < n) {
                nums[i + 1] = arr[k];
            }
        }
    }
}
