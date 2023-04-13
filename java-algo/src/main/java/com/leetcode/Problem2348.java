package com.leetcode;

/**
 * 2348. Number of Zero-Filled Subarrays
 * https://leetcode.com/problems/number-of-zero-filled-subarrays/
 */
public class Problem2348 {
    public long zeroFilledSubarray(int[] nums) {
        long cnt = 0, ans = 0;
        for (int num : nums) {
            if (num == 0) {
                cnt++;
            } else if (cnt > 0) {
                ans += (cnt + 1) * cnt / 2;
                cnt = 0;
            }
        }
        ans += (cnt + 1) * cnt / 2;
        return ans;
    }
}
