package com.leetcode;

import java.util.Stack;

/**
 * 946. Validate Stack Sequences
 * https://leetcode.com/problems/validate-stack-sequences/
 */
public class Problem946 {

    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int size = pushed.length;
        if (popped.length != size) return false;
        if (size == 0 || size == 1) return true;

        int pushedIndex = 0, poppedIndex = 0;
        Stack<Integer> stack = new Stack<>();

        while (pushedIndex < size) {
            if (pushed[pushedIndex] == popped[poppedIndex]) {
                if (poppedIndex == size - 1)
                    break;
                poppedIndex++;
                pushedIndex++;
            } else {
                if (stack.size() == 0 || stack.lastElement() != popped[poppedIndex]) {
                    stack.push(pushed[pushedIndex]);
                    pushedIndex++;
                } else {
                    stack.pop();
                    poppedIndex++;
                }
            }
        }

        while (!stack.empty()) {
            if (stack.pop() == popped[poppedIndex]) {
                poppedIndex++;
            } else {
                return false;
            }
        }

        return true;
    }

    public boolean ans(int[] pushed, int[] popped) {
        int n = popped.length;
        Stack<Integer> stack = new Stack<>();

        int j = 0;
        for (int x: pushed) {
            stack.push(x);
            while (!stack.isEmpty() && j < n && stack.peek() == popped[j]) {
                stack.pop();
                j++;
            }
        }

        return j == n;
    }
}
