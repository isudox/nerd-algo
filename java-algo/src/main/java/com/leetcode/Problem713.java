package com.leetcode;

/**
 * 713. Subarray Product Less Than K
 * https://leetcode.com/problems/subarray-product-less-than-k/
 */
public class Problem713 {
    /**
     * O(N^2)
     */
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int ans = 0;
        int l = 0, r = 0, n = nums.length;
        long mul = 1;
        while (l < n) {
            if (r < n) {
                mul *= nums[r];
            } else {
                l++;
                r = l;
                mul = 1;
                continue;
            }
            if (mul < k) {
                ans++;
                r++;
            } else {
                l++;
                r = l;
                mul = 1;
            }
        }
        return ans;
    }

    public int numSubarrayProductLessThanK2(int[] nums, int k) {
        if (k <= 1) {
            return 0;
        }
        int ans = 0;
        for (int l = 0, r = 0, mul = 1; r < nums.length; r++) {
            mul *= nums[r];
            while (mul >= k) {
                mul /= nums[l++];
            }
            ans += r - l + 1;
        }
        return ans;
    }
}
