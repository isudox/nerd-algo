package com.leetcode;

/**
 * 1017. Convert to Base -2
 * https://leetcode.com/problems/convert-to-base-2/
 */
public class Problem1017 {
    public String baseNeg2(int n) {
        if (n == 0) {
            return "0";
        }
        StringBuilder ans = new StringBuilder();
        while (n != 0) {
            int rem = Math.abs(n % -2);
            ans = new StringBuilder(rem == 0 ? "0" : "1").append(ans);
            n = (n - rem) / -2;
        }
        return ans.toString();
    }
}
