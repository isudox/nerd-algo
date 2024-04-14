package com.leetcode;

import java.util.Stack;

/**
 * 678. Valid Parenthesis String
 * https://leetcode.com/problems/valid-parenthesis-string/
 */
class Problem678 {
    public boolean checkValidString(String s) {
        Stack<Integer> leftStack = new Stack<>(), starStack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                leftStack.push(i);
            } else if (c == '*') {
                starStack.push(i);
            } else if (!leftStack.isEmpty()) {
                leftStack.pop();
            } else if (!starStack.isEmpty()) {
                starStack.pop();
            } else {
                return false;
            }
        }
        if (leftStack.size() > starStack.size()) {
            return false;
        }
        int i = 0, j = starStack.size() - leftStack.size();
        while (i < leftStack.size()) {
            if (leftStack.get(i) > starStack.get(j)) {
                return false;
            }
            i++;
            j++;
        }
        return true;
    }
}
