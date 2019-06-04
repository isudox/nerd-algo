package com.leetcode;

import java.util.Objects;

/**
 * 8. String to Integer (atoi)
 * https://leetcode.com/problems/string-to-integer-atoi/
 *
 * Implement atoi which converts a string to an integer.
 *
 * The function first discards as many whitespace characters as necessary until
 * the first non-whitespace character is found. Then, starting from this
 * character, takes an optional initial plus or minus sign followed by as many
 * numerical digits as possible, and interprets them as a numerical value.
 *
 * The string can contain additional characters after those that form the
 * integral number, which are ignored and have no effect on the behavior of
 * this function.
 *
 * If the first sequence of non-whitespace characters in str is not a valid
 * integral number, or if no such sequence exists because either str is empty
 * or it contains only whitespace characters, no conversion is performed.
 *
 * If no valid conversion could be performed, a zero value is returned.
 *
 * Note:
 *
 * Only the space character ' ' is considered as whitespace character.
 * Assume we are dealing with an environment which could only store integers
 * within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical
 * value is out of the range of representable values, INT_MAX (231 − 1)
 * or INT_MIN (−231) is returned.
 *
 * Example 1:
 *
 * Input: "42"
 * Output: 42
 *
 * Example 2:
 *
 * Input: "   -42"
 * Output: -42
 * Explanation: The first non-whitespace character is '-', which is the minus sign.
 *              Then take as many numerical digits as possible, which gets 42.
 *
 * Example 3:
 *
 * Input: "4193 with words"
 * Output: 4193
 * Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
 *
 * Example 4:
 *
 * Input: "words and 987"
 * Output: 0
 * Explanation: The first non-whitespace character is 'w', which is not a numerical
 *              digit or a +/- sign. Therefore no valid conversion could be performed.
 *
 * Example 5:
 *
 * Input: "-91283472332"
 * Output: -2147483648
 * Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
 *              Thefore INT_MIN (−231) is returned.
 */
public class StringToInteger {

    public int myAtoi(String str) {
        if (str == null || Objects.equals(str, ""))
            return 0;
        if (str.charAt(0) == '-')
            return subAtoi(str.substring(1), true);
        if (str.charAt(0) == '+')
            return subAtoi(str.substring(1), false);
        if (str.charAt(0) == ' ')
            return myAtoi(str.substring(1));
        return subAtoi(str, false);
    }

    private int subAtoi(String str, boolean neg) {
        if (str == null || str.equals("")) {
            System.out.println("a");
            return 0;
        }
        int res = 0;
        for (int i = 0; i < str.length(); i++) {
            if (!Character.isDigit(str.charAt(i)))
                return res;
            int digit = Character.getNumericValue(str.charAt(i));
            if (neg) {
                if (i == 9) {
                    int diff = res - Integer.MIN_VALUE / 10;
                    if (diff < 0 || (diff == 0 && digit > 8))
                        return Integer.MIN_VALUE;
                }
                if (i >= 10)
                    return Integer.MIN_VALUE;
                res = 10 * res - digit;
            } else {
                if (i == 9) {
                    int diff = res - Integer.MAX_VALUE / 10;
                    if (diff > 0 || (diff == 0 && digit > 7))
                        return Integer.MAX_VALUE;
                }
                if (i >= 10)
                    return Integer.MAX_VALUE;
                res = digit + 10 * res;
            }
        }
        return res;
    }
}