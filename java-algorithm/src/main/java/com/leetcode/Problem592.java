package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 592. Fraction Addition and Subtraction
 * https://leetcode.com/problems/fraction-addition-and-subtraction/
 */
public class Problem592 {
    public String fractionAddition(String expression) {
        List<String> segments = new ArrayList<>();
        List<Character> signs = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < expression.length(); i++) {
            char ch = expression.charAt(i);
            if (ch == '+' || ch == '-') {
                segments.add(sb.toString());
                sb = new StringBuilder();
                signs.add(ch);
            } else {
                sb.append(ch);
            }
        }
        segments.add(sb.toString());
        int[] nums = parse(segments.get(0));
        for (int i = 0; i < signs.size(); i++) {
            char sign = signs.get(i);
            int[] next = parse(segments.get(i + 1));
            cal(nums, next, sign);
        }
        int gcd = gcd(Math.abs(nums[0]), Math.abs(nums[1]));
        nums[0] /= gcd;
        nums[1] /= gcd;
        return String.format("%d/%d", nums[0], nums[1]);
    }

    private int[] parse(String expr) {
        if (expr.length() == 0) return new int[]{0, 1};
        int[] ret = new int[2];
        int num = 0;
        boolean neg = false;
        for (int i = 0; i < expr.length(); i++) {
            char ch = expr.charAt(i);
            if (ch == '-') {
                neg = true;
            } else if (ch == '/') {
                ret[0] = neg ? -num : num;
                neg = false;
                num = 0;
            } else {
                num = num * 10 + (ch - '0');
            }
        }
        ret[1] = neg ? -num : num;
        return ret;
    }

    private void cal(int[] x, int[] y, char sign) {
        int denominator = scm(x[1], y[1]);
        x[0] *= denominator / x[1];
        y[0] *= denominator / y[1];
        x[1] = denominator;
        if (sign == '+') {
            x[0] += y[0];
        } else {
            x[0] -= y[0];
        }
    }

    private int scm(int a, int b) {
        return a * b / gcd(a, b);
    }

    private int gcd(int a, int b) {
        return b > 0 ? gcd(b, a % b) : a;
    }
}
