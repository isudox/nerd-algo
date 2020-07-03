package com.leetcode;

/**
 * 29. Divide Two Integers
 * https://leetcode.com/problems/divide-two-integers/
 * Given two integers dividend and divisor, divide two integers without using
 * multiplication, division and mod operator.
 *
 * Return the quotient after dividing dividend by divisor.
 *
 * The integer division should truncate toward zero.
 *
 * Example 1:
 *
 * Input: dividend = 10, divisor = 3
 * Output: 3
 * Example 2:
 *
 * Input: dividend = 7, divisor = -3
 * Output: -2
 * Note:
 *
 * Both dividend and divisor will be 32-bit signed integers.
 * The divisor will never be 0.
 * Assume we are dealing with an environment which could only store integers
 * within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
 * this problem, assume that your function returns 231 − 1 when the division
 * result overflows.
 */
public class Problem29 {

    public int divide(int dividend, int divisor) {
        if (divisor == 0 || dividend == Integer.MIN_VALUE && divisor == -1)
            return Integer.MAX_VALUE;
        int result = 0;
        boolean positive = dividend > 0 == divisor > 0;
        long dividend1 = dividend == Integer.MIN_VALUE ? 2147483648L : Math.abs(dividend);
        long divisor1 = divisor == Integer.MIN_VALUE ? 2147483648L : Math.abs(divisor);
        int i = 0;
        while (divisor1 << (i + 1) <= dividend1)
            i++;
        while (dividend1 >= divisor1) {
            if (dividend1 >= divisor1 << i) {
                result = result + (1 << i);
                dividend1 = dividend1 - (divisor1 << i);
            }
            i--;
        }
        return positive ? result : -result;
    }
}
