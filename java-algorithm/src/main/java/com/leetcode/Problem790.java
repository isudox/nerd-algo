package com.leetcode;

/**
 * 790. Domino and Tromino Tiling
 * https://leetcode.com/problems/domino-and-tromino-tiling/
 */
public class Problem790 {
    public int numTilings(int n) {
        if (n == 1) {
            return 1;
        }
        int base = (int) 1e9 + 7;
        long[] dp0 = new long[n + 1];  // end with |
        long[] dp1 = new long[n + 1];  // end with =
        long[] dp2 = new long[n + 1];  // end with 「
        long[] dp3 = new long[n + 1];  // end with 」
        dp0[1] = 1;
        dp0[2] = 1;
        dp1[2] = 1;
        dp2[2] = 1;
        dp3[2] = 1;
        for (int i = 3; i <= n; i++) {
            dp0[i] = (dp0[i - 1] + dp1[i - 1] + dp2[i - 1] + dp3[i - 1]) % base;
            dp1[i] = (dp0[i - 2] + dp1[i - 2]) % base;
            dp2[i] = (dp0[i - 2] + dp1[i - 2] + dp3[i - 1]) % base;
            dp3[i] = (dp0[i - 2] + dp1[i - 2] + dp2[i - 1]) % base;
        }
        return (int) (dp0[n] + dp1[n]) % base;
    }
}
