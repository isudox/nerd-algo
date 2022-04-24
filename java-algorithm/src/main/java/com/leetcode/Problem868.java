package com.leetcode;

/**
 * 868. Binary Gap
 * https://leetcode.com/problems/binary-gap/
 */
public class Problem868 {
    public int binaryGap(int n) {
        int ans = 0;
        int pre = -1;
        int cur = 0;
        while (n > 0) {
            int bit = n & 1;
            if (bit == 1) {
                if (pre > -1) {
                    int gap = cur - pre;
                    if (gap > ans) {
                        ans = gap;
                    }
                }
                pre = cur;
            }
            n = n >> 1;
            cur++;
        }
        return ans;
    }
}
