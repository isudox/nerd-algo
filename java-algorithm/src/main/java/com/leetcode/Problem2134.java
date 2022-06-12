package com.leetcode;

/**
 * 2134. Minimum Swaps to Group All 1's Together II
 * https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
 */
public class Problem2134 {
    public int minSwaps(int[] nums) {
        int k = 0;
        for (int num : nums) {
            if (num == 1) {
                k++;
            }
        }
        int ans = nums.length;
        int cur = 0;
        for (int i = 0; i < k; i++) {
            if (nums[i] == 1) {
                cur++;
            }
        }
        int tmp = k - cur;
        if (tmp == 0) {
            return 0;
        }
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] == 1) {
                tmp++;
            }
            if (nums[(i + k - 1) % nums.length] == 1) {
                tmp--;
            }
            if (tmp < ans) {
                ans = tmp;
            }
        }
        return ans;
    }
}
