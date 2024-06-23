package com.leetcode;

/**
 * 1482. Minimum Number of Days to Make m Bouquets
 * https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
 */
public class Problem1482 {
    public int minDays(int[] bloomDay, int m, int k) {
        if (bloomDay.length / m < k) {
            return -1;
        }
        int lo = bloomDay[0], hi = bloomDay[0];
        for (int e : bloomDay) {
            if (e < lo) lo = e;
            if (e > hi) hi = e;
        }
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (helper(bloomDay, m, k, mid))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }

    private boolean helper(int[] nums, int m, int k, int limit) {
        int flowers = 0, cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > limit) {
                cnt = 0;
            } else if (++cnt == k) {
                // optimize: 当已经制作所需数量的花束时，提前结束
                if (++flowers == m) {
                    return true;
                }
                cnt = 0;
            }
            // optimize: 当剩余花盆不足以制作所需花束时，提前结束
            if (cnt == 0 && nums.length - 1 - i < (m - flowers) * k) {
                return false;
            }
        }
        return false;
    }
}
