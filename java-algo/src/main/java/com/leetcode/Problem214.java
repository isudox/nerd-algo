package com.leetcode;

/**
 * 214. Shortest Palindrome
 * https://leetcode.com/problems/shortest-palindrome/
 */
public class Problem214 {
    public String shortestPalindrome(String s) {
        String rs = new StringBuilder(s).reverse().toString();
        for (int i = 0; i < s.length(); i++) {
            if (s.substring(0, s.length() - i).equals(rs.substring(i))) {
                return rs.substring(0, i) + s;
            }
        }
        return "";
    }
}
