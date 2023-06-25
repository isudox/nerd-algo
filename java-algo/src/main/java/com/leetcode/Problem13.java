package com.leetcode;

/**
 * 13. Roman to Integer
 * https://leetcode.com/problems/roman-to-integer/
 */
public class Problem13 {
    public int romanToInt1(String s) {
        String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] ints = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        int res = 0;
        for (int i = 0; i < romans.length; ) {
            int index = s.indexOf(romans[i]);
            if (index == 0) {
                res += ints[i];
                s = s.substring(index + romans[i].length());
            } else {
                i++;
            }
        }
        return res;
    }

    public int romanToInt2(String s) {
        int pre = 0, cur = 0, res = 0;
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case 'M': cur = 1000;
                    break;
                case 'D': cur = 500;
                    break;
                case 'C': cur = 100;
                    break;
                case 'L': cur = 50;
                    break;
                case 'X': cur = 10;
                    break;
                case 'V': cur = 5;
                    break;
                case 'I': cur = 1;
                    break;
            }

            if (cur > pre) {
                res += cur - pre * 2;
            } else {
                res += cur;
            }
            pre = cur;
        }
        return res;
    }
}
