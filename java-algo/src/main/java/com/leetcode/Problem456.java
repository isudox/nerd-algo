package com.leetcode;

import java.util.Stack;

/**
 * 456. 132 Pattern
 * https://leetcode.com/problems/132-pattern/
 */
public class Problem456 {
    public boolean find132pattern(int[] nums) {
        int n = nums.length;
        Stack<Integer> stack = new Stack<>();
        int k = Integer.MIN_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] < k) {
                return true;
            }
            while (!stack.isEmpty() && stack.peek() < nums[i]) {
                k = stack.pop();
            }
            stack.add(nums[i]);
        }
        return false;
    }
}
