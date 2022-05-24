package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;
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
public class Problem32 {

    /**
     * An easy method with {@link Stack}
     */
    public int longestValidParentheses(String s) {
        Deque<Integer> deque = new ArrayDeque<>();
        int ans = 0, cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (cur == ')' && !deque.isEmpty() && s.charAt(deque.peekLast()) == '(') {
                deque.pollLast();
                cnt = deque.isEmpty() ? i + 1 : i - deque.peekLast();
                ans = Math.max(ans, cnt);
            } else {
                deque.addLast(i);
            }
        }
        return ans;
    }

    /**
     * DP.
     * Time complexity: O(N)
     * Space complexity: O(N)
     */
    public int longestValidParentheses2(String s) {
        int n = s.length();
        int ans = 0;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++)
            dp[i] = 0;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == ')') {
                if (s.charAt(i - 1) == '(') {
                    dp[i] = 2 + (i > 2 ? dp[i - 2] : 0);
                } else if (i - 1 - dp[i - 1] >= 0 && s.charAt(i - 1 - dp[i - 1]) == '(') {
                    dp[i] = dp[i - 1] + 2 + (i - 2 - dp[i - 1] > 0 ? dp[i - 2 - dp[i - 1]] : 0);
                }
                ans = Math.max(ans, dp[i]);
            }
        }
        return ans;
    }
}
