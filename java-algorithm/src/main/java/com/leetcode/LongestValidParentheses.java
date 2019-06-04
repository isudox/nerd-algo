package com.leetcode;

import java.util.Stack;

/**
 * 32. Longest Valid Parentheses
 * https://leetcode.com/problems/longest-valid-parentheses/
 * <p>
 * Given a string containing just the characters '(' and ')', find the length
 * of the longest valid (well-formed) parentheses substring.
 * <p>
 * Example 1:
 * <p>
 * Input: "(()"
 * Output: 2
 * Explanation: The longest valid parentheses substring is "()"
 * <p>
 * Example 2:
 * <p>
 * Input: ")()())"
 * Output: 4
 * Explanation: The longest valid parentheses substring is "()()"
 */
public class LongestValidParentheses {

    /**
     * An easy method with {@link Stack}
     */
    public int longestValidParentheses(String s) {
        int max = 0, count, len = s.length();
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < len; i++) {
            if (s.charAt(i) == ')'
                    && !stack.isEmpty()
                    && s.charAt(stack.peek()) == '(') {
                stack.pop();
                count = stack.isEmpty() ? i + 1 : i - stack.peek();
                max = count > max ? count : max;
            } else {
                stack.push(i);
            }
        }

        return max;
    }
}
