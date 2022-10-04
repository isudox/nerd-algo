package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 921. Minimum Add to Make Parentheses Valid
 * https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/
 */
public class Problem921 {
    public int minAddToMakeValid(String s) {
        int ans = 0;
        Deque<Character> deque = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                deque.offerLast('(');
            } else if (!deque.isEmpty()) {
                deque.pollLast();
            } else {
                ans++;
            }
        }
        return ans + deque.size();
    }
}
