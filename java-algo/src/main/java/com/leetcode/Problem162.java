package com.leetcode;

public class Problem162 {
    public int findPeakElement(int[] nums) {
        if (nums.length == 1) {
            return 0;
        }
        int ans = -1;
        int lo = 0, hi = nums.length - 1, mid;
        while (lo <= hi) {
            mid = (lo + hi) / 2;
            if (compare(nums, mid - 1, mid) < 0 && compare(nums, mid, mid + 1) > 0) {
                return mid;
            }
            if (compare(nums, mid, mid + 1) < 0) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }

    private int compare(int[] nums, int i, int j) {
        int[] x = get(nums, i);
        int[] y = get(nums, j);
        if (x[0] != y[0]) {
            return x[0] > y[0] ? 1 : -1;
        }
        if (x[1] == y[1]) {
            return 0;
        }
        return x[1] > y[1] ? 1 : -1;
    }

    private int[] get(int[] nums, int i) {
        if (i == -1 || i == nums.length) {
            return new int[]{0, 0};
        }
        return new int[]{1, nums[i]};
    }
}
