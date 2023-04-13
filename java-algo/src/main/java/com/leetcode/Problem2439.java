package com.leetcode;

/**
 * 2439. Minimize Maximum of Array
 * https://leetcode.com/problems/minimize-maximum-of-array/
 */
public class Problem2439 {
    public int minimizeArrayValue(int[] nums) {
        int lo = 0, hi = (int) 1e9;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (check(nums, mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    boolean check(int[] nums, int x) {
        long cnt = 0;
        for (int num : nums) {
            if (num <= x) {
                cnt += x - num;
            } else {
                if (cnt < num - x) {
                    return false;
                }
                cnt -= (num - x);
            }
        }
        return true;
    }
}
