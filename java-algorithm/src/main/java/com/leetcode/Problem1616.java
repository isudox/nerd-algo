package com.leetcode;

/**
 * 1616. Split Two Strings to Make Palindrome
 * https://leetcode.com/problems/split-two-strings-to-make-palindrome/
 */
public class Problem1616 {
    public boolean checkPalindromeFormation(String a, String b) {
        return check(a, a) || check(b, b) || check(a, b) || check(b, a);
    }

    private boolean check(String a, String b) {
        int i = 0, j = b.length() - 1;
        while (i < j && a.charAt(i) == b.charAt(j)) {
            i++;
            j--;
        }
        if (i >= j) {
            return true;
        }
        return check0(a, i, j) || check0(b, i, j);
    }

    private boolean check0(String s, int i, int j) {
        while (i < j) {
            if (s.charAt(i++) != s.charAt(j--)) {
                return false;
            }
        }
        return true;
    }
}
