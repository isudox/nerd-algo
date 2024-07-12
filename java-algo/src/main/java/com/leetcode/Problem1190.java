package com.leetcode;

import java.util.Stack;

/**
 * """1190. Reverse Substrings Between Each Pair of Parentheses
 * https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
 */
public class Problem1190 {
    public String reverseParentheses(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == ')') {
                StringBuilder temp = new StringBuilder();
                char top;
                while ((top = stack.pop()) != '(') {
                    temp.append(top);
                }
                for (char tempC : temp.toString().toCharArray()) {
                    stack.add(tempC);
                }
            } else {
                stack.add(c);
            }
        }
        StringBuilder ans = new StringBuilder();
        for (char c : stack) {
            ans.append(c);
        }
        return ans.toString();
    }

    public String reverseParentheses2(String s) {
        int n = s.length();
        int[] pairs = new int[n];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; ++i) {
            if (s.charAt(i) == '(') {
                stack.add(i);
            } else if (s.charAt(i) == ')') {
                int pre = stack.pop();
                pairs[pre] = i;
                pairs[i] = pre;
            }
        }
        StringBuilder sb = new StringBuilder();
        int i = 0, d = 1;
        while (i < n) {
            char c = s.charAt(i);
            if (c == '(' || c == ')') {
                i = pairs[i];
                d = -d;
            } else {
                sb.append(c);
            }
            i += d;
        }
        return sb.toString();
    }
}
