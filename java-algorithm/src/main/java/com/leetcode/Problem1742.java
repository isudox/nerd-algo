package com.leetcode;

/**
 * 1742. Maximum Number of Balls in a Box
 * https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
 */
public class Problem1742 {
    public int countBalls(int lowLimit, int highLimit) {
        int ans = 0;
        int[] count = new int[50];
        for (int i = lowLimit; i <= highLimit; i++) {
            int box = 0;
            int j = i;
            while (j > 0) {
                box += j % 10;
                j /= 10;
            }
            if (++count[box] > ans) {
                ans = count[box];
            }
        }
        return ans;
    }
}
