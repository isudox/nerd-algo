package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 42. Trapping Rain Water
 * https://leetcode.com/problems/trapping-rain-water/
 */
public class Problem42 {

    public int trap(int[] height) {
        int ans = 0;
        int left = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        for (int h : height) {
            if (stack.isEmpty() || h >= left) {
                for (int s : stack) ans += left - s;
                stack.clear();
                stack.add(h);
                left = h;
                continue;
            }
            if (h <= stack.peekLast()) {
                stack.add(h);
            } else {
                int cnt = 0;
                while (stack.peekLast() < h) {
                    ans += h - stack.removeLast();
                    cnt++;
                    if (stack.isEmpty()) break;
                }
                while (cnt >= 0) {
                    stack.add(h);
                    cnt--;
                }
            }
        }
        return ans;
    }
}
