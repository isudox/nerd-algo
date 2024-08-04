package com.leetcode;

import java.util.Arrays;

/**
 * 1508. Range Sum of Sorted Subarray Sums
 * https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
 */
public class Problem1508 {
    public int rangeSum(int[] nums, int n, int left, int right) {
        int sz = nums.length;
        int[] presum = new int[sz + 1];
        for (int i = 0; i < sz; i++) {
            presum[i + 1] = presum[i] + nums[i];
        }
        int[] arr = new int[sz * (sz + 1) / 2];
        int index = 0;
        for (int i = 0; i < presum.length; i++) {
            for (int j = i + 1; j < presum.length; j++) {
                arr[index++] = presum[j] - presum[i];
            }
        }
        Arrays.sort(arr);
        int ans = 0, base = (int) 1e9 + 7;
        for (int i = left - 1; i < right; i++) {
            ans = (ans + arr[i] % base) % base;
        }
        return ans;
    }
}
