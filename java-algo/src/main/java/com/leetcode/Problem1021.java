package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1021. Remove Outermost Parentheses
 * https://leetcode.com/problems/remove-outermost-parentheses/
 */
public class Problem1021 {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        Deque<Character> q = new ArrayDeque<>();
        StringBuilder cur = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            cur.append(s.charAt(i));
            if (s.charAt(i) == '(') {
                q.addLast('(');
            } else {
                q.pollLast();
                if (q.isEmpty()) {
                    sb.append(cur.subSequence(1, cur.length() - 1));
                    cur = new StringBuilder();
                }
            }
        }
        return sb.toString();
    }
}
