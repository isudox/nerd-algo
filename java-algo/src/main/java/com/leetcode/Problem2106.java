package com.leetcode;

/**
 * 2106. Maximum Fruits Harvested After at Most K Steps
 * https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
 */
public class Problem2106 {
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        int ans = 0;
        int sum = 0;
        int left = 0, right = 0;
        while (right < fruits.length) {
            sum += fruits[right][1];
            while (left <= right && step(fruits, startPos, left, right) > k) {
                sum -= fruits[left][1];
                left++;
            }
            ans = Math.max(ans, sum);
            right++;
        }
        return ans;
    }

    private int step(int[][] fruits, int startPos, int left, int right) {
        return Math.min(Math.abs(startPos - fruits[right][0]), Math.abs(startPos - fruits[left][0])) + fruits[right][0] - fruits[left][0];
    }
}
