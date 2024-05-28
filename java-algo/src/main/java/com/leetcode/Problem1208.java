package com.leetcode;

/**
 * 1208. Get Equal Substrings Within Budget
 * https://leetcode.com/problems/get-equal-substrings-within-budget/
 */
public class Problem1208 {
    public int equalSubstring(String s, String t, int maxCost) {
        int n = s.length();
        int[] presum = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            presum[i] += presum[i - 1] + Math.abs(t.charAt(i - 1) - s.charAt(i - 1));
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int target = presum[i] - maxCost;
            int idx = binsearch(presum, target);
            if (idx >= 0) {
                ans = Math.max(ans, i - idx);
            }
        }
        return ans;
    }

    private int binsearch(int[] nums, int target) { // find first num >= target
        int lo = 0, hi = nums.length - 1, mid;
        while (lo < hi) {
            mid = (lo + hi) >> 1;
            if (nums[mid] >= target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
