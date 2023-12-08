package com.leetcode;

public class Problem1716 {
    public int totalMoney(int n) {
        int x = n / 7, y = n % 7;
        return (7 * x + 49) * x / 2 + (1 + x + x + y) * y / 2;
    }
}
