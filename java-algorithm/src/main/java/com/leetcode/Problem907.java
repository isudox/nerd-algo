package com.leetcode;

/**
 * 907. Sum of Subarray Minimums
 * https://leetcode.com/problems/sum-of-subarray-minimums/
 */
public class Problem907 {
    public int sumSubarrayMins(int[] arr) {
        int mod = (int) 1e9 + 7;
        long ans = 0L;
        for (int i = 0; i < arr.length; i++) {
            int left = i - 1;
            while (left >= 0 && arr[i] < arr[left]) {
                left--;
            }
            int right = i + 1;
            while (right < arr.length && arr[i] <= arr[right]) {
                right++;
            }
            ans += (long) arr[i] * (i - left) * (right - i);
            ans %= mod;
        }
        return (int) ans;
    }
}
