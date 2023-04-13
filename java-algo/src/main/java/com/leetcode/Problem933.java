package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 933. Number of Recent Calls
 * https://leetcode.com/problems/number-of-recent-calls/
 */
public class Problem933 {
    private static class RecentCounter {

        private Deque<Integer> queue;

        public RecentCounter() {
            queue = new ArrayDeque<>();
        }

        public int ping(int t) {
            queue.offer(t);
            int l = t < 3000 ? 0 : t - 3000;
            while (queue.peek() < l) {
                queue.poll();
            }
            return queue.size();
        }
    }
}
