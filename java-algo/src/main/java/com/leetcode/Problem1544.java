package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1544. Make The String Great
 * https://leetcode.com/problems/make-the-string-great/
 */
public class Problem1544 {
    public String makeGood(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty()) {
                char pre = stack.peekFirst();
                if (pre != c && Character.toLowerCase(pre) == Character.toLowerCase(c)) {
                    stack.pollFirst();
                    continue;
                }
            }
            stack.push(c);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pollLast());
        }
        return sb.toString();
    }
}
