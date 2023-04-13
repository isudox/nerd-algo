package com.leetcode;

/**
 * 7. Reverse Integer
 * https://leetcode.com/problems/reverse-integer/
 *
 * Given a 32-bit signed integer, reverse digits of an integer.
 *
 * Example 1:
 *
 * Input: 123
 * Output: 321
 *
 * Example 2:
 *
 * Input: -123
 * Output: -321
 *
 * Example 3:
 *
 * Input: 120
 * Output: 21
 *
 * Note:
 * Assume we are dealing with an environment which could only store integers
 * within the 32-bit signed integer range: [−231,  231 − 1].
 * For the purpose of this problem, assume that your function returns 0
 * when the reversed integer overflows.
 */
public class Problem7 {

    public int reverse(int x) {
        boolean isNeg = false;
        long result = 0L;
        if (x == -2147483648) {
            return 0;
        }
        if (x < 0) {
            isNeg = true;
            x = -x;
        }
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        if (result > Integer.MAX_VALUE) {
            return 0;
        }
        if (isNeg) {
            result = -result;
        }

        return Math.toIntExact(result);
    }

    public int reverse2(int x) {
        int hi = Integer.MAX_VALUE / 10;
        int lo = Integer.MIN_VALUE / 10;
        int ans = 0;
        while (x != 0) {
            if (ans > hi || ans < lo) {
                return 0;
            }
            ans = ans * 10 + x % 10;
            x = x / 10;
        }
        return ans;
    }
}
