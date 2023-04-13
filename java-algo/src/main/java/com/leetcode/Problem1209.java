package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

/**
 * 1209. Remove All Adjacent Duplicates in String II
 * https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
 */
public class Problem1209 {
    public String removeDuplicates(String s, int k) {
        if (s.length() < k) {
            return s;
        }
        char[] chars = s.toCharArray();
        Deque<Character> queue = new ArrayDeque<>();
        Stack<Character> backup = new Stack<>();
        int repeat = 1;
        char pre = chars[0];
        queue.offer(chars[0]);
        for (int i = 1; i < chars.length; i++) {
            queue.offer(chars[i]);
            if (chars[i] == pre) {
                repeat++;
            } else {
                repeat = 1;
                pre = chars[i];
            }
            if (repeat == k) {
                for (int j = 0; j < k; j++) {
                    queue.pollLast();
                }
                if (queue.isEmpty()) {
                    pre = '0';
                    repeat = 0;
                } else {
                    pre = queue.peekLast();
                    while (!queue.isEmpty() && queue.peekLast() == pre) {
                        backup.add(queue.pollLast());
                    }
                    repeat = backup.size();
                    while (!backup.isEmpty()) {
                        queue.offer(backup.pop());
                    }
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            sb.append(queue.pollFirst());
        }
        return sb.toString();
    }
}
