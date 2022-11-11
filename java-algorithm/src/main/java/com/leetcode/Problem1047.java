package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1047. Remove All Adjacent Duplicates In String
 * https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
 */
public class Problem1047 {
    public String removeDuplicates(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            if (stack.isEmpty() || stack.peekLast() != s.charAt(i)) {
                stack.offerLast(s.charAt(i));
            } else {
                stack.pollLast();
            }
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pollFirst());
        }
        return sb.toString();
    }
}
