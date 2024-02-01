package com.leetcode;

import java.util.Arrays;

/**
 * 2966. Divide Array Into Arrays With Max Difference
 * https://leetcode.com/problems/divide-array-into-arrays-with-max-difference
 */
public class Problem2966 {
    public int[][] divideArray(int[] nums, int k) {
        int[][] ans = new int[nums.length / 3][3];
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i += 3) {
            if (nums[i + 2] - nums[i] > k) {
                return new int[][]{};
            }
            int[] arr = ans[i / 3];
            System.arraycopy(nums, i, arr, 0, 3);
        }
        return ans;
    }
}
