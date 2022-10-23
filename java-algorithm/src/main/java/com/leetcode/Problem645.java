package com.leetcode;

/**
 * 645. Set Mismatch
 * https://leetcode.com/problems/set-mismatch/
 */
public class Problem645 {
    public int[] findErrorNums(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        int n = nums.length;
        int diff = (1 + n) * n / 2 - sum;
        int[] ans = new int[2];
        for (int i = 0; i < n; i++) {
            int num = Math.abs(nums[i]);
            if (nums[num - 1] < 0) {
                ans = new int[]{num, num + diff};
                break;
            }
            nums[num - 1] *= -1;
        }
        return ans;
    }
}
