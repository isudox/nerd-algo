package com.leetcode;

/**
 * 75. Sort Colors
 * https://leetcode.com/problems/sort-colors/
 */
public class Problem75 {
    public void sortColors(int[] nums) {
        int[] cnt = new int[3];
        for (int num : nums) {
            cnt[num]++;
        }
        int i = 0, j = 0;
        while (i < nums.length) {
            while (j < 3 && cnt[j] == 0) {
                j++;
            }
            if (j == 3) {
                break;
            }
            nums[i++] = j;
            cnt[j]--;
        }
    }
}
