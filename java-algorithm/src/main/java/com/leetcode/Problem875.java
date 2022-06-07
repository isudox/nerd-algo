package com.leetcode;

import java.util.Arrays;

/**
 * 875. Koko Eating Bananas
 * https://leetcode.com/problems/koko-eating-bananas/
 */
public class Problem875 {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int min = 1, max = piles[piles.length - 1];
        while (min < max) {
            int mid = (min + max) / 2;
            if (check(piles, mid, h)) {
                max = mid;
            } else {
                min = mid + 1;
            }
        }
        return min;
    }

    private boolean check(int[] nums, int x, int limit) {
        int cost = 0;
        int idx = Arrays.binarySearch(nums, x);
        if (idx < 0) {
            idx = -idx - 1;
        }
        cost += idx;
        for (int i = idx; i < nums.length; i++) {
            int c = nums[i] / x;
            if (nums[i] % x > 0) {
                c++;
            }
            cost += c;
            if (cost > limit) {
                return false;
            }
        }
        return cost <= limit;
    }
}
