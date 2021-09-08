package com.leetcode;

/**
 * 5. Longest Palindromic Substring
 * https://leetcode.com/problems/longest-palindromic-substring/
 */
public class Problem5 {

    public String longestPalindrome(String s) {
        int len = s.length();
        if (len <= 1) {
            return s;
        }
        int maxLen = 0;
        String palindrome = "";

        for (int i = 0; i < len - 1; i++) {
            // odd
            String oddStr = check(s, i, i, len);
            int oddLen = oddStr.length();
            if (oddLen > maxLen) {
                maxLen = oddLen;
                palindrome = oddStr;
            }
            // even
            String evenStr = check(s, i, i + 1, len);
            int evenLen = evenStr.length();
            if (evenLen > maxLen) {
                maxLen = evenLen;
                palindrome = evenStr;
            }
        }

        return palindrome;
    }

    private String check(String s, int start, int end, int len) {
        while (start >= 0 && end <= len - 1 && s.charAt(start) == s.charAt(end)) {
            start--;
            end++;
        }
        return s.substring(start + 1, end);
    }

    public String longestPalindrome2(String s) {
        int maxLen = 0, n = s.length();
        String ans = "";
        for (int i = 0; i < n; i++) {
            String a = expand(s, i, i);
            String b = expand(s, i, i + 1);
            String temp = a.length() > b.length() ? a : b;
            if (temp.length() > maxLen) {
                maxLen = temp.length();
                ans = temp;
            }
        }
        return ans;
    }

    private String expand(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return s.substring(left + 1, right);
    }
}
