package com.leetcode;

/**
 * 396. Rotate Function
 * https://leetcode.com/problems/rotate-function/
 */
public class Problem396 {
    public int maxRotateFunction(int[] nums) {
        int sum = 0;
        int ans = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            ans += i * nums[i];
            sum += nums[i];
        }
        int cur = ans;
        for (int i = 1; i < n; i++) {
            cur += sum - n * nums[n - i];
            if (cur > ans) {
                ans = cur;
            }
        }
        return ans;
    }
}
