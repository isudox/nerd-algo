package com.leetcode;

/**
 * 20. Valid Parentheses
 * https://leetcode.com/problems/valid-parentheses/
 *
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 *
 * An input string is valid if:
 *
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Note that an empty string is also considered valid.
 *
 * Example 1:
 *
 * Input: "()"
 * Output: true
 * Example 2:
 *
 * Input: "()[]{}"
 * Output: true
 *
 * Example 3:
 *
 * Input: "(]"
 * Output: false
 * Example 4:
 *
 * Input: "([)]"
 * Output: false
 * Example 5:
 *
 * Input: "{[]}"
 * Output: true
 */
public class ValidParentheses {

    public boolean isValid(String s) {
        char[] stack = new char[s.length()];
        int index = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{') {
                stack[index++] = s.charAt(i);
            } else if (s.charAt(i) == ')') {
                if (index == 0 || stack[--index] != '(') return false;
            } else if (s.charAt(i) == ']') {
                if (index == 0 || stack[--index] != '[') return false;
            } else {
                if (index == 0 || stack[--index] != '{') return false;
            }
        }
        return index == 0;
    }
}
