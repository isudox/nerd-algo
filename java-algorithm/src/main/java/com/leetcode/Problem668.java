package com.leetcode;

/**
 * 668. Kth Smallest Number in Multiplication Table
 * https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
 */
public class Problem668 {
    public int findKthNumber(int m, int n, int k) {
        int lo = 1, hi = m * n, mid;
        while (lo < hi) {
            mid = lo + (hi - lo) / 2;
            int cnt = mid / n * n;
            for (int i = mid / n + 1; i <= m; i++) {
                cnt += mid / i;
            }
            if (cnt >= k) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
