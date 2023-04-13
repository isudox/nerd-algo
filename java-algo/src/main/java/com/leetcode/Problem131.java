package com.leetcode;


import java.util.ArrayList;
import java.util.List;

/**
 * 131. Palindrome Partitioning
 * https://leetcode.com/problems/palindrome-partitioning/
 */
public class Problem131 {
    public List<List<String>> partition(String s) {
        List<List<String>> ans = new ArrayList<>();
        backtrack(s, ans, new ArrayList<>(), 0);
        return ans;
    }

    private void backtrack(String s, List<List<String>> ans, List<String> cur, int start) {
        if (start >= s.length()) {
            ans.add(new ArrayList<>(cur));
        }
        for (int i = start; i < s.length(); i++) {
            if (isPalindrome(s, start, i)) {
                cur.add(s.substring(start, i + 1));
                backtrack(s, ans, cur, i + 1);
                cur.remove(cur.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s, int x, int y) {
        while (x < y) {
            if (s.charAt(x++) != s.charAt(y--)) return false;
        }
        return true;
    }
}
