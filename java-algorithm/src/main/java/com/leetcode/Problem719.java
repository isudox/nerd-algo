package com.leetcode;

import java.util.Arrays;

/**
 * 719. Find K-th Smallest Pair Distance
 * https://leetcode.com/problems/find-k-th-smallest-pair-distance/
 */
public class Problem719 {
    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        int i = 0, j = 1000000;
        while (i < j) {
            int mid = i + (j - i) / 2;
            if (helper(nums, mid) >= k) {
                j = mid;
            } else {
                i = mid + 1;
            }
        }
        return j;
    }

    private int helper(int[] nums, int x) {
        int cnt = 0;
        for (int i = 0, j = i + 1; i < nums.length; i++) {
            while (j < nums.length && nums[j] - nums[i] <= x) {
                j++;
            }
            cnt += j - i - 1;
        }
        return cnt;
    }
}
