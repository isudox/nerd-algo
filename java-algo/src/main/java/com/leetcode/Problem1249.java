package com.leetcode;

import java.util.Stack;

/**
 * 1249. Minimum Remove to Make Valid Parentheses
 * https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
 */
public class Problem1249 {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> stack = new Stack<>();
        boolean[] removed = new boolean[s.length()];
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } if (s.charAt(i) == ')') {
                if (stack.isEmpty()) {
                    removed[i] = true;
                } else {
                    stack.pop();
                }
            }
        }
        while (!stack.isEmpty()) {
            removed[stack.pop()] = true;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (!removed[i]) {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}
