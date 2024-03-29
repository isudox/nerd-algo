package com.leetcode;

/**
 * 2962. Count Subarrays Where Max Element Appears at Least K Times
 * https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
 */
public class Problem2962 {
    public long countSubarrays(int[] nums, int k) {
        int max = nums[0];
        for (int num : nums) {
            if (num > max) {
                max = num;
            }
        }
        long ans = 0, cnt = 0;
        for (int i = 0, j = 0; j < nums.length; j++) {
            if (nums[j] == max) {
                cnt++;
            }
            while (cnt == k) {
                if (nums[i++] == max) {
                    cnt--;
                }
            }
            ans += i;
        }
        return ans;
    }
}
