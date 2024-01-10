package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class Problem2696 {
    public int minLength(String s) {
        int ans = 0;
        Deque<Character> q = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (q.isEmpty()) {
                q.offerLast(cur);
                continue;
            }
            char pre = q.getLast();
            if ((pre == 'A' && cur == 'B') || (pre == 'C' && cur == 'D')) {
                q.pollLast();
                ans += 2;
            } else {
                q.offerLast(cur);
            }
        }
        return s.length() - ans;
    }
}
