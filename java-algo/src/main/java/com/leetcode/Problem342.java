package com.leetcode;

/**
 * 342. Power of Four
 * https://leetcode.com/problems/power-of-four/
 */
class Problem342 {
    public boolean isPowerOfFour(int n) {
        if (n < 1) return false;
        if (n == 1) return true;
        if (n % 4 != 0) return false;
        return isPowerOfFour(n / 4);
    }
}
