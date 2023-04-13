package com.leetcode;

/**
 * 172. Factorial Trailing Zeroes
 * https://leetcode.com/problems/factorial-trailing-zeroes/
 */
public class Problem172 {
    public int trailingZeroes(int n) {
        if (n == 0) return 0;
        return n / 5 + trailingZeroes(n / 5);
    }
}
