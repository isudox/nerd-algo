package com.leetcode;

/**
 * 1328. Break a Palindrome
 * https://leetcode.com/problems/break-a-palindrome/
 */
public class Problem1328 {
    public String breakPalindrome(String palindrome) {
        int n = palindrome.length();
        if (n == 1) {
            return "";
        }
        for (int i = 0; i < n; i++) {
            if (palindrome.charAt(i) != 'a') {
                if (n % 2 == 1 && n / 2 == i) {
                    continue;
                }
                if (palindrome.charAt(n - 1 - i) == 'a') {
                    continue;
                }
                return palindrome.substring(0, i) + "a" + palindrome.substring(i + 1);
            }
        }
        return palindrome.substring(0, n - 1) + "b";
    }
}
