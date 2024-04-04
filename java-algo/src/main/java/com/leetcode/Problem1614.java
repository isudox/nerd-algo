package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1614. Maximum Nesting Depth of the Parentheses
 * https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
 */
public class Problem1614 {
    public int maxDepth(String s) {
        int ans = 0, depth = 0;
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                depth++;
                ans = Math.max(ans, depth);
            } else if (c == ')') {
                depth--;
            }
        }
        return ans;
    }
}
