package com.leetcode;

import java.util.PriorityQueue;

/**
 * 1405. Longest Happy String
 * https://leetcode.com/problems/longest-happy-string
 */
public class Problem1405 {
    public String longestDiverseString(int a, int b, int c) {
        StringBuilder ans = new StringBuilder();
        PriorityQueue<int[]> q = new PriorityQueue<>((x, y) -> Integer.compare(y[0], x[0]));
        if (a > 0) q.offer(new int[]{a, 0});
        if (b > 0) q.offer(new int[]{b, 1});
        if (c > 0) q.offer(new int[]{c, 2});
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int n = ans.length();
            if (n >= 2 && ans.charAt(n - 1) - 'a' == cur[1] && ans.charAt(n - 2) - 'a' == cur[1]) {
                if (q.isEmpty()) {
                    break;
                }
                int[] next = q.poll();
                ans.append((char) (next[1] + 'a'));
                if (--next[0] > 0) {
                    q.offer(next);
                }
                q.offer(cur);
            } else {
                ans.append((char) (cur[1] + 'a'));
                if (--cur[0] > 0) {
                    q.offer(cur);
                }
            }
        }
        return ans.toString();
    }
}
