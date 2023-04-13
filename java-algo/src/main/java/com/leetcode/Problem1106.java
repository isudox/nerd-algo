package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1106. Parsing A Boolean Expression
 * https://leetcode.com/problems/parsing-a-boolean-expression/
 */
public class Problem1106 {
    public boolean parseBoolExpr(String expression) {
        Deque<Character> stack = new ArrayDeque<>();
        int n = expression.length();
        for (int i = 0; i < n; i++) {
            char c = expression.charAt(i);
            if (c == ',') {
                continue;
            }
            if (c != ')') {
                stack.push(c);
            } else {
                int t = 0, f = 0;
                while (stack.peek() != '(') {
                    char val = stack.pop();
                    if (val == 't') {
                        t++;
                    } else {
                        f++;
                    }
                }
                stack.pop();
                char op = stack.pop();
                if (op == '!') {
                    stack.push(f == 1 ? 't' : 'f');
                } else if (op == '&') {
                    stack.push(f == 0 ? 't' : 'f');
                } else if (op == '|') {
                    stack.push(t > 0 ? 't' : 'f');
                }
            }
        }
        return stack.pop() == 't';
    }
}
