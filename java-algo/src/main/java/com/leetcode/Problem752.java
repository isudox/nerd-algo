package com.leetcode;

import java.util.*;

/**
 * 752. Open the Lock
 * https://leetcode.com/problems/open-the-lock/
 */
public class Problem752 {
    public int openLock(String[] deadends, String target) {
        if (target.equals("0000")) {
            return 0;
        }
        Set<String> forbidden = new HashSet<>(Arrays.asList(deadends));
        if (forbidden.contains(target) || forbidden.contains("0000")) {
            return -1;
        }
        int ans = 0;
        int[] dirs = {1, -1};
        Queue<String> queue = new LinkedList<>();
        queue.offer("0000");
        Set<String> seen = new HashSet<>();
        seen.add("0000");
        while (!queue.isEmpty()) {
            ans++;
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                String cur = queue.poll();
                for (int j = 0; j < 4; j++) {
                    int c = cur.charAt(j) - '0';
                    for (int d : dirs) {
                        char nc = (char) ('0' + (c + d + 10) % 10);
                        String next = cur.substring(0, j) + nc + cur.substring(j + 1);
                        if (!seen.contains(next) && !forbidden.contains(next)) {
                            if (next.equals(target)) {
                                return ans;
                            }
                            queue.offer(next);
                            seen.add(next);
                        }
                    }
                }
            }
        }
        return -1;
    }
}
