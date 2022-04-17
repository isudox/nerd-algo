package com.leetcode;

/**
 * 479. Largest Palindrome Product
 * https://leetcode.com/problems/largest-palindrome-product/
 */
public class Problem479 {
    public int largestPalindrome(int n) {
        if (n == 1) {
            return 9;
        }
        int max = (int) (Math.pow(10, n) - 1);
        for (int left = max; left >= 0; left--) {
            long p = left;
            for (int x = left; x > 0; x /= 10) {
                p = p * 10 + x % 10;  // left & right
            }
            for (long x = max; x * x >= p; x--) {
                if (p % x == 0) {
                    return (int) (p % 1337);
                }
            }
        }
        return -1;
    }
}
