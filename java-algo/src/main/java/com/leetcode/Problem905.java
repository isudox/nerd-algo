package com.leetcode;

/**
 * 905. Sort Array By Parity
 * https://leetcode.com/problems/sort-array-by-parity/
 */
public class Problem905 {
    public int[] sortArrayByParity(int[] nums) {
        int i = 0, j = nums.length - 1;
        while (i < j) {
            if (nums[i] % 2 == 0) {
                i++;
                continue;
            }
            if (nums[j] % 2 == 1) {
                j--;
                continue;
            }
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            i++;
            j--;
        }
        return nums;
    }
}
