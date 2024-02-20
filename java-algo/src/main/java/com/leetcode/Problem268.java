package com.leetcode;

/**
 * 268. Missing Number
 * https://leetcode.com/problems/missing-number/
 */
public class Problem268 {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = n * (n + 1) / 2;
        for (int num : nums) {
            sum -= num;
        }
        return sum;
    }

    public int missingNumber2(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (x < 0 || x == n) {
                continue;
            }
            while ( x < n && nums[x] != -1) {
                int y = nums[x];
                nums[x] = -1;
                x = y;
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] != -1) {
                return i;
            }
        }
        return n;
    }
}
