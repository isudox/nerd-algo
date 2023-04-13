package com.leetcode;

/**
 * 374. Guess Number Higher or Lower
 * https://leetcode.com/problems/guess-number-higher-or-lower/
 */
public class Problem374 {
    public int guessNumber(int n) {
        int lo = 1, hi = n;
        while(lo < hi) {
            int mid = lo + ((hi - lo) >> 1);
            int ret = guess(mid);
            if (ret == 0) return mid;
            if (ret > 0) lo = mid + 1;
            else hi = mid - 1;
        }
        return lo;
    }

    private int guess(int num) {
        return num;
    }
}
