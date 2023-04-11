package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class Problem2390 {
    public String removeStars(String s) {
        Deque<Character> q = new ArrayDeque<>();
        int i = 0;
        for (char c : s.toCharArray()) {
            if (c == '*') {
                q.pollLast();
            } else {
                q.offerLast(s.charAt(i));
            }
            i++;
        }
        StringBuilder ans = new StringBuilder();
        while (!q.isEmpty()) {
            ans.append(q.pollFirst());
        }
        return ans.toString();
    }
}
