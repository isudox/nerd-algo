package com.leetcode;

/**
 * 878. Nth Magical Number
 * https://leetcode.com/problems/nth-magical-number/
 */
public class Problem878 {
    public int nthMagicalNumber(int n, int a, int b) {
        int base = (int) 1e9 + 7;
        long lo = Math.min(a, b), hi = (long) n * lo;
        int c = lcm(a, b);
        while (lo <= hi) {
            long mid = lo + (hi - lo) / 2;
            long cnt = mid / a + mid / b - mid / c;
            if (cnt >= n) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return (int) ((hi + 1) % base);
    }

    private int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    private int gcd(int a, int b) {
        return b != 0 ? gcd(b, a % b) : a;
    }
}
