package com.leetcode;

/**
 * 67. Add Binary
 * https://leetcode.com/problems/add-binary
 */
public class Problem67 {
    public String addBinary(String a, String b) {
        if (a.length() > b.length()) {
            return addBinary(b, a);
        }
        if (a.length() == 0) {
            return b;
        }
        int n = a.length();
        String b0 = b.substring(b.length() - n), b1 = b.substring(0, b.length() - n);
        char[] ans = new char[n];
        int add = 0;
        for (int i = n - 1; i >= 0; i--) {
            int ai = a.charAt(i) - '0';
            int bi = b0.charAt(i) - '0';
            int ci = ai + bi + add;
            add = ci > 1 ? 1 : 0;
            ci = ci % 2;
            ans[i] = ci > 0 ? '1' : '0';
        }
        if (add == 0) {
            return b1 + new String(ans);
        }
        return addBinary("1", b1) + new String(ans);
    }
}
