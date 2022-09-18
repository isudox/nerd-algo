package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 42. Trapping Rain Water
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it is able to trap after raining.
 *
 * ![img](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
 *
 * The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 * In this case, 6 units of rain water (blue section) are being trapped.
 *
 * Example:
 *
 * Input: [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
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
