package com.leetcode;

/**
 * 70. Climbing Stairs
 * https://leetcode.com/problems/climbing-stairs/
 */
public class Problem70 {
    public int climbStairs(int n) {
        int a, b = 0, c = 1;
        for (int i = 1; i <= n; i++) {
            a = b;
            b = c;
            c = a + b;
        }
        return c;
    }
}
