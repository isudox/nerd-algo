package com.leetcode;

/**
 * 11. Container With Most Water
 * https://leetcode.com/problems/container-with-most-water/
 */
public class Problem11 {

    public int maxArea(int[] height) {
        int maxV = 0, curV = 0;
        int i = 0, j = height.length - 1;
        while (i < j) {
            if (height[i] < height[j]) {
                curV = (j - i) * (height[i++]);
            } else if (height[i] > height[j]) {
                curV = (j - i) * (height[j--]);
            } else {
                curV = (j - i) * (height[i++]);
                j--;
            }
            maxV = Math.max(maxV, curV);
        }
        return maxV;
    }
}
