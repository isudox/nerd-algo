package com.leetcode;

/**
 * 600. Non-negative Integers without Consecutive Ones
 * https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
 */
public class Problem600 {
    public int findIntegers(int n) {
        int len = getLen(n);
        return dfs(n, len, 0, 0);
    }

    private int dfs(int n, int len, int pos, int bits) {
        if (pos == len)
            return 1;
        int ret = 0;
        int pre_bit = bits & 1;
        bits = bits << 1;
        if (bits <= n)
            ret += dfs(n, len, pos + 1, bits);
        if (pre_bit == 0 && bits + 1 <= n)
            ret += dfs(n, len, pos + 1, bits + 1);
        return ret;
    }

    private int getLen(int n) {
        for (int i = 31; i >= 0; i--) {
            if (((n >> i) & 1) == 1)
                return i;
        }
        return 0;
    }
}
