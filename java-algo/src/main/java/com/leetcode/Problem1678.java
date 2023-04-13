package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1678. Goal Parser Interpretation
 * https://leetcode.com/problems/goal-parser-interpretation/
 */
public class Problem1678 {
    public String interpret(String command) {
        StringBuilder sb = new StringBuilder();
        Deque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < command.length(); i++) {
            char c = command.charAt(i);
            if (c == 'G') {
                sb.append("G");
            } else if (c == ')') {
                if (stack.size() > 1) {
                    for (int j = 0; j < 3; j++) {
                        stack.pop();
                    }
                    sb.append("al");
                } else {
                    stack.pop();
                    sb.append("o");
                }
            } else {
                stack.push(c);
            }
        }
        return sb.toString();
    }
}
