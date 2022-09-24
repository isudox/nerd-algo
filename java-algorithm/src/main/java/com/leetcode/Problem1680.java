package com.leetcode;

/**
 * 1680. Concatenation of Consecutive Binary Numbers
 * https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
 */
public class Problem1680 {
    public int concatenatedBinary(int n) {
        int mod = (int) 1e9 + 7;
        long ans = 0L;
        for (int i = 1; i <= n; i++) {
            ans = ((ans << countBit(i)) + i) % mod;
        }
        return (int) ans % mod;
    }

    private int countBit(int num) {
        int bits = 0;
        while (num > 0) {
            num = num >> 1;
            bits++;
        }
        return bits;
    }
}
