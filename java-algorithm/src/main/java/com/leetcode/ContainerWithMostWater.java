package com.leetcode;

/**
 * 11. Container With Most Water
 * https://leetcode.com/problems/container-with-most-water/
 *
 * Given n non-negative integers a1, a2, ..., an , where each represents a
 * point at coordinate (i, ai). n vertical lines are drawn such that the
 * two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
 * which together with x-axis forms a container, such that the container
 * contains the most water.
 *
 * Note: You may not slant the container and n is at least 2.
 *
 * <img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg">
 * The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
 * In this case, the max area of water (blue section) the container can contain is 49.
 *
 * Example:
 *
 * <pre>
 *     Input: [1,8,6,2,5,4,8,3,7]
 *     Output: 49
 * </pre>
 */
public class ContainerWithMostWater {

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