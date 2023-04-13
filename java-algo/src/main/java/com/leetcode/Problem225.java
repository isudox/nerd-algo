package com.leetcode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 225. Implement Stack using Queues
 * https://leetcode.com/problems/implement-stack-using-queues/
 */
public class Problem225 {
    private static class MyStack {

        private final Queue<Integer> queue = new LinkedList<>();

        public MyStack() {
        }

        public void push(int x) {
            queue.offer(x);
        }

        public int pop() {
            int n = queue.size(), i = 0;
            while (i < n - 1) {
                queue.offer(queue.poll());
                i++;
            }
            return queue.poll();
        }

        public int top() {
            int ret = 0;
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                ret = queue.poll();
                queue.offer(ret);
            }
            return ret;
        }

        public boolean empty() {
            return queue.isEmpty();
        }
    }
}
