package com.leetcode;

/**
 * 278. First Bad Version
 * https://leetcode.com/problems/first-bad-version/
 */
public class Problem278 {
    public int firstBadVersion(int n) {
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (isBadVersion(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private boolean isBadVersion(int n) {
        return true;
    }
}
