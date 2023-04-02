package com.leetcode;

/**
 * 831. Masking Personal Information
 * https://leetcode.com/problems/masking-personal-information/
 */
public class Problem831 {
    public String maskPII(String s) {
        int atPos = s.indexOf('@');
        if (atPos < 0) { // phone number
            for (String c : new String[]{"+", "-", "(", ")", " "}) {
                s = s.replace(c, "");
            }
            int n = s.length();
            if (n == 10) {
                return "***-***-" + s.substring(s.length() - 4);
            }
            return "+" + "*".repeat(n - 10) + "-***-***-" + s.substring(n - 4);
        }
        s = s.toLowerCase();
        return s.charAt(0) + "*****" + s.substring(atPos - 1);
    }
}
