package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 224. Basic Calculator
 * https://leetcode.com/problems/basic-calculator/
 */
public class Problem224 {
    public int calculate(String s) {
        Deque<Integer> deque = new ArrayDeque<>();
        deque.push(1);
        int sign = 1;

        int ans = 0;
        int n = s.length();
        int i = 0;
        while (i < n) {
            if (Character.isDigit(s.charAt(i))) {
                long num = 0;
                while (i < n && Character.isDigit(s.charAt(i))) {
                    num = num * 10 + s.charAt(i) - '0';
                    i++;
                }
                ans += sign * num;
                continue;
            }
            if (s.charAt(i) == '+') {
                sign = deque.peek();
            } else if (s.charAt(i) == '-') {
                sign = -deque.peek();
            } else if (s.charAt(i) == '(') {
                deque.push(sign);
            } else if (s.charAt(i) == ')') {
                deque.pop();
            }
            i++;
        }
        return ans;
    }
}
