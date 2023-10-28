package com.leetcode;

/**
 * 2520. Count the Digits That Divide a Number
 */
public class Problem2520 {
    public int countDigits(int num) {
        boolean[] memo = new boolean[10];
        int ans = 0, tmp = num;
        while (tmp > 0) {
            int digit = tmp % 10;
            if (memo[digit]) {
                ans++;
            } else if (num % digit == 0) {
                memo[digit] = true;
                ans++;
            }
            tmp /= 10;
        }
        return ans;
    }
}
