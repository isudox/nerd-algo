package com.leetcode;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * 65. Valid Number
 * https://leetcode.com/problems/valid-number/
 * <p>
 * "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"
 */
public class Problem65 {
    public boolean isNumber(String s) {
        return true;
    }

    public static void main(String[] args) {
        Problem65 sol = new Problem65();
        String[] arr = "e1e".split("[eE]");
        System.out.println(sol.isNumber("0e")); // false
        System.out.println(sol.isNumber("-.1")); // true
        System.out.println(sol.isNumber(".1")); // false
        System.out.println(sol.isNumber(".")); // false
        System.out.println(sol.isNumber("3.")); // true
        System.out.println(sol.isNumber("e9")); // false
        System.out.println(sol.isNumber("3.e3")); // false
        System.out.println(sol.isNumber(".1E1")); // false
        System.out.println(sol.isNumber("0")); // false
        System.out.println(sol.isNumber("e")); // false
    }
}
