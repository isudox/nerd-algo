package com.leetcode;

/**
 * 995. Minimum Number of K Consecutive Bit Flips
 * https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
 */
public class Problem995 {
    public int minKBitFlips(int[] nums, int k) {
        int n = nums.length;
        int[] diff = new int[n + 1];
        int ans = 0, revCnt = 0;
        for (int i = 0; i < n; i++) {
            revCnt += diff[i];
            if ((nums[i] + revCnt) % 2 == 0) {
                if (i + k > n) {
                    return -1;
                }
                ans++;
                revCnt++;
                diff[i + k]--;
            }
        }
        return ans;
    }
}
