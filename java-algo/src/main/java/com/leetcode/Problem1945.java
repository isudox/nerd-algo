package com.leetcode;

/**
 * 1945. Sum of Digits of String After Convert
 * https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
 */
public class Problem1945 {
    public int getLucky(String s, int k) {
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            int val = s.charAt(i) - 'a' + 1;
            ans += val % 10 + val / 10;
        }
        while (k > 1) {
            int tmp = 0;
            while (ans > 0) {
                tmp += ans % 10;
                ans /= 10;
            }
            ans = tmp;
            k--;
        }
        return ans;
    }
}
