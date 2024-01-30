package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

/**
 * 150. Evaluate Reverse Polish Notation
 * https://leetcode.com/problems/evaluate-reverse-polish-notation/
 */
public class Problem150 {
    private static Set<String> ops = new HashSet<>();

    static {
        ops.add("+");
        ops.add("-");
        ops.add("/");
        ops.add("*");
    }

    public int evalRPN(String[] tokens) {
        Deque<Integer> q = new ArrayDeque<>();
        for (String s : tokens) {
            if (!ops.contains(s)) {
                q.push(Integer.valueOf(s));
                continue;
            }
            int a = q.pop(), b = q.pop(), c = 0;
            c = switch (s) {
                case "+" -> b + a;
                case "-" -> b - a;
                case "*" -> b * a;
                default -> b / a;
            };
            q.push(c);
        }
        return q.pop();
    }
}
