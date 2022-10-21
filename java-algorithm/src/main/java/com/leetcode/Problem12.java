package com.leetcode;

/**
 * 12. Integer to Roman
 * https://leetcode.com/problems/integer-to-roman/
 */
public class Problem12 {

    public String intToRoman1(int num) {
        String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String[] thousands = {"", "M", "MM", "MMM"};
        String[][] romans = {ones, tens, hundreds, thousands};
        String res = "";
        int len = String.valueOf(num).length();
        for (int i = len - 1; i >= 0; i--) {
            int x = num / pow(10, i);
            res = res + romans[i][x];
            num = num % pow(10, i);
        }
        return res;
    }

    private int pow(int x, int y) {
        int z = 1;
        for (; y > 0; y--) z *= x;
        return z;
    }

    public String intToRoman2(int num) {
        String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String[] thousands = {"", "M", "MM", "MMM"};
        String[][] romans = {ones, tens, hundreds, thousands};
        String res = "";
        int digit = 0;
        while (num > 0) {
            int x = num % 10;
            res = romans[digit][x] + res;
            num = num / 10;
            digit++;
        }
        return res;
    }

    public String intToRoman3(int num) {
        String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] ints = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < ints.length; i++) {
            while (num >= ints[i]) {
                res.append(romans[i]);
                num -= ints[i];
            }
        }
        return res.toString();
    }
}
