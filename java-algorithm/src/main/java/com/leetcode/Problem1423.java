package com.leetcode;

/**
 * 1423. Maximum Points You Can Obtain from Cards
 * https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
 */
class Problem1423 {
    public int maxScore(int[] cardPoints, int k) {
        int sum = 0;
        int cur = 0;
        int window = cardPoints.length - k;
        for (int i = 0; i < cardPoints.length; i++) {
            sum += cardPoints[i];
            if (i == window - 1) {
                cur = sum;
            }
        }
        int min = cur;
        for (int i = window; i < cardPoints.length; i++) {
            cur += cardPoints[i] - cardPoints[i - window];
            if (cur < min) {
                min = cur;
            }
        }
        return sum - min;
    }
}
