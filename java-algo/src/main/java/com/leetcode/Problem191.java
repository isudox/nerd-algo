package com.leetcode;

/**
 * 191. Number of 1 Bits
 * https://leetcode.com/problems/number-of-1-bits/
 */
public class Problem191 {
    public int hammingWeight(int n) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & (1 << i)) != 0) {
                ans++;
            }
        }
        return ans;
    }
}
