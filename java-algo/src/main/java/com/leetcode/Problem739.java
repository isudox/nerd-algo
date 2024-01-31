package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 739. Daily Temperatures
 * https://leetcode.com/problems/daily-temperatures/
 */
public class Problem739 {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] ans = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            int t = temperatures[i];
            while (!stack.isEmpty() && t > temperatures[stack.peek()]) {
                int preIdx = stack.pop();
                ans[preIdx] = i - preIdx;
            }
            stack.push(i);
        }
        return ans;
    }
}
