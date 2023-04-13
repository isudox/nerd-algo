package com.leetcode;

/**
 * 357. Count Numbers with Unique Digits
 * https://leetcode.com/problems/count-numbers-with-unique-digits/
 */
public class Problem357 {
    public int countNumbersWithUniqueDigits(int n) {
        if (n == 0) {
            return 1;
        }
        int ans = 10;
        int pre = 9;
        for (int i = 1; i <= n; i++) {
            pre *=  11 - i;
            ans += pre;
        }
        return ans;
    }
}
