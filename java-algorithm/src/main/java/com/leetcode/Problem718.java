package com.leetcode;

/**
 * 718. Maximum Length of Repeated Subarray
 * https://leetcode.com/problems/maximum-length-of-repeated-subarray/
 */
class Problem718 {
    public int findLength(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int ans = 0;
        for (int i = 0; i < m; i++) {
            int len = Math.min(m - i, n);
            ans = Math.max(ans, getLength(nums1, i, nums2, 0, len));
        }
        for (int i = 0; i < n; i++) {
            int len = Math.min(m, n - i);
            ans = Math.max(ans, getLength(nums1, 0, nums2, i, len));
        }
        return ans;
    }

    private int getLength(int[] nums1, int x, int[] nums2, int y, int len) {
        int ret = 0, cur = 0;
        for (int i = 0; i < len; i++) {
            if (nums1[x + i] == nums2[y + i]) {
                if (++cur > ret)
                    ret = cur;
            } else {
                cur = 0;
            }
        }
        return ret;
    }
}
