package com.leetcode;

/**
 * 509. Fibonacci Number
 */
class Problem509 {
    public int fib(int n) {
        if (n < 2) return n;
        return fib(n - 1) + fib(n - 2);
    }
}
