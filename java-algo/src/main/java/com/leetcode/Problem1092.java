package com.leetcode;

public class Problem1092 {
    public String shortestCommonSupersequence(String str1, String str2) {
        if (str1.isBlank()) {
            return str2;
        }
        if (str2.isEmpty()) {
            return str1;
        }
        String s1 = str1.substring(0, str1.length() - 1);
        String s2 = str2.substring(0, str2.length() - 1);
        char c1 = str1.charAt(str1.length() - 1);
        char c2 = str2.charAt(str2.length() - 1);
        if (c1 == c2) {
            return shortestCommonSupersequence(s1, s2) + c1;
        }
        String ans1 = shortestCommonSupersequence(s1, str2);
        String ans2 = shortestCommonSupersequence(str2, s2);
        if (ans1.length() < ans2.length()) {
            return ans1 + c1;
        }
        return ans2 + c2;
    }
}
