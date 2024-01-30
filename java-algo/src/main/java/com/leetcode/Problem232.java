package com.leetcode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.Stack;

/**
 * 232. Implement Queue using Stacks
 * https://leetcode.com/problems/implement-queue-using-stacks/
 */
public class Problem232 {
    static class MyQueue {
        Stack<Integer> instack;
        Stack<Integer> outstack;

        public MyQueue() {
            instack = new Stack<>();
            outstack = new Stack<>();
        }

        public void push(int x) {
            instack.push(x);
        }

        public int pop() {
            if (outstack.isEmpty()) {
                trans();
            }
            return outstack.pop();
        }

        public int peek() {
            if (outstack.isEmpty()) {
                trans();
            }
            return outstack.peek();
        }

        public boolean empty() {
            return instack.isEmpty() && outstack.isEmpty();
        }

        private void trans() {
            while (!instack.isEmpty()) {
                outstack.push(instack.pop());
            }
        }
    }
}
