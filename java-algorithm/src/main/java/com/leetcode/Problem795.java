package com.leetcode;

/**
 * 795. Number of Subarrays with Bounded Maximum
 * https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
 */
public class Problem795 {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        int ans = 0;
        int last1 = -1, last2 = -1;
        for (int i = 0; i < nums.length; i++) {
            if (left <= nums[i] && nums[i] <= right) {
                last1 = i;
            } else if (nums[i] > right) {
                last2 = i;
                last1 = -1;
            }
            if (last1 != -1) {
                ans += last1 - last2;
            }
        }
        return ans;
    }
}
