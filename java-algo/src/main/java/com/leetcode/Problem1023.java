package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1023. Camelcase Matching
 * https://leetcode.com/problems/camelcase-matching/
 */
public class Problem1023 {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        List<Boolean> ans = new ArrayList<>();
        for (String query : queries) {
            ans.add(helper(query, pattern));
        }
        return ans;
    }

    private boolean helper(String query, String pattern) {
        int i = 0;
        for (char c : query.toCharArray()) {
            if (!Character.isLowerCase(c)) {
                if (i >= pattern.length() || c != pattern.charAt(i)) {
                    return false;
                }
            }
            if (i < pattern.length() && c == pattern.charAt(i)) {
                i++;
            }
        }
        return i >= pattern.length();
    }
}
