package com.leetcode;

/**
 * 476. Number Complement
 * https://leetcode.com/problems/number-complement/
 */
public class Problem476 {
    public int findComplement(int num) {
        int ans = 0, i = 0;
        while (num != 0) {
            int bit = 1 - (num & 1);
            ans += (bit << i);
            num >>= 1;
            i++;
        }
        return ans;
    }
}
