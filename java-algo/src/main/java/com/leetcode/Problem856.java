package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class Problem856 {
    public int scoreOfParentheses(String s) {
        Deque<String> q = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                q.offerLast("(");
            } else {
                int num = 0;
                while (!"(".equals(q.peekLast())) {
                    num += Integer.parseInt(q.pollLast());
                }
                num = num == 0 ? 1 : num * 2;
                q.pollLast();
                q.offerLast(String.valueOf(num));
            }
        }
        int ans = 0;
        while (!q.isEmpty()) {
            ans += Integer.parseInt(q.pollLast());
        }
        return ans;
    }
}
