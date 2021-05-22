package com.leetcode;

/**
 * 161. One Edit Distance
 * https://leetcode-cn.com/problems/one-edit-distance/
 *
 * Given two strings s and t, return true if they are both one
 * edit distance apart, otherwise return false.
 *
 * A string s is said to be one distance apart from a string t if you can:
 *
 * Insert exactly one character into s to get t.
 * Delete exactly one character from s to get t.
 * Replace exactly one character of s with a different character to get t.
 *
 * Example 1:
 *
 * Input: s = "ab", t = "acb"
 * Output: true
 * Explanation: We can insert 'c' into s to get t.
 * Example 2:
 *
 * Input: s = "", t = ""
 * Output: false
 * Explanation: We cannot get t from s by only one step.
 * Example 3:
 *
 * Input: s = "a", t = ""
 * Output: true
 * Example 4:
 *
 * Input: s = "", t = "A"
 * Output: true
 *
 * Constraints:
 *
 * 0 <= s.length <= 10^4
 * 0 <= t.length <= 10^4
 * s and t consist of lower-case letters, upper-case letters and/or digits.
 */
public class Problem161 {
    public boolean isOneEditDistance(String s, String t) {
        if (Math.abs(s.length() - t.length()) > 1) {
            return false;
        }
        Boolean[][] memo = new Boolean[s.length()][t.length()];
        return dfs(s, 0, t, 0, memo, 1);
    }

    private boolean dfs(String s, int x, String t, int y, Boolean[][] memo, int edit) {
        if (x == s.length())
            return y + edit == t.length();
        if (y == t.length())
            return x + edit == s.length();
        if (memo[x][y] != null)
            return memo[x][y];
        if (s.charAt(x) == t.charAt(y)) {
            memo[x][y] = dfs(s, x + 1, t, y + 1, memo, edit);
        } else if (edit == 1) {
            memo[x][y] = dfs(s, x + 1, t, y, memo, 0)
                    || dfs(s, x, t, y + 1, memo, 0)
                    || dfs(s, x + 1, t, y + 1, memo, 0);
        } else {
            memo[x][y] = false;
        }
        return memo[x][y];
    }

    public boolean isOneEditDistance2(String s, String t) {
        int m = s.length(), n = t.length();
        if (m > n) return isOneEditDistance2(t, s);
        if (n - m > 1) return false;
        for (int i = 0; i < m; i++) {
            if (s.charAt(i) != t.charAt(i)) {
                if (m == n)
                    return s.substring(i + 1).equals(t.substring(i + 1));
                else
                    return s.substring(i).equals(t.substring(i + 1));
            }
        }
        return m != n;
    }
}
