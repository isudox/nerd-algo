package com.leetcode.solution;

import java.util.Stack;

/**
 * 946. Validate Stack Sequences
 * https://leetcode.com/problems/validate-stack-sequences/
 *
 * Given two sequences pushed and popped with distinct values,
 * return true if and only if this could have been the result of
 * a sequence of push and pop operations on an initially empty stack.
 *
 * Example 1:
 *
 *   Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
 *   Output: true
 *   Explanation: We might do the following sequence:
 *   push(1), push(2), push(3), push(4), pop() -> 4,
 *   push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
 *
 * Example 2:
 *
 *   Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
 *   Output: false
 *   Explanation: 1 cannot be popped before 2.
 *
 * Note:
 *
 *   0 <= pushed.length == popped.length <= 1000
 *   0 <= pushed[i], popped[i] < 1000
 *   pushed is a permutation of popped.
 *   pushed and popped have distinct values.
 */
public class ValidateStackSequences {

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
}
