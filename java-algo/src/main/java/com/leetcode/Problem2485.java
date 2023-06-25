package com.leetcode;

/**
 * 2485. Find the Pivot Integer
 * https://leetcode.com/problems/find-the-pivot-integer/
 */
public class Problem2485 {
    public int pivotInteger(int n) {
        int sum = (n + 1) * n / 2;
        int x = (int) Math.sqrt(sum);
        return x * x == sum ? x : -1;
    }
}
