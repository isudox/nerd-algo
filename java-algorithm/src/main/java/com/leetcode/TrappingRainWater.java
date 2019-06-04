package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 42. Trapping Rain Water
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it is able to trap after raining.
 *
 * ![img](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
 *
 * The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 * In this case, 6 units of rain water (blue section) are being trapped. Thanks
 * Marcos for contributing this image!
 *
 * Example:
 *
 *
 * Input: [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 */
public class TrappingRainWater {

    public int trap(int[] height) {
        int ans = 0;
        int left = 0;
        List<Integer> stack = new ArrayList<>();

        for (int h : height) {
            if (stack.isEmpty()) {
                stack.add(h);
                left = h;
            } else if (h < left) {
                if (h <= stack.get(stack.size() - 1)) {
                    stack.add(h);
                } else {
                    int cnt = 0;
                    while (stack.get(stack.size() - 1) < h) {
                        ans += h - stack.remove(stack.size() - 1);
                        cnt++;
                        if (stack.isEmpty()) {
                            break;
                        }
                    }
                    while (cnt >= 0) {
                        stack.add(h);
                        cnt--;
                    }
                }
            } else {
                int top = Math.min(left, h);
                for (int s : stack) {
                    ans += top - s;
                }
                stack.clear();
                stack.add(h);
                left = h;
            }
        }

        return ans;
    }
}
