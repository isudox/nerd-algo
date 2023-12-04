package com.leetcode;

import java.util.List;

/**
 * 2264. Largest 3-Same-Digit Number in String
 */
public class Problem2264 {

    private List<String> sameDigitNumbers = List.of("999", "888", "777", "666", "555", "444", "333", "222", "111", "000");

    public String largestGoodInteger(String num) {
        for (String sameDigitNumber : sameDigitNumbers) {
            if (contains(sameDigitNumber, num)) {
                return sameDigitNumber;
            }
        }
        return "";
    }

    private boolean contains(String sameDigitNumber, String num) {
        for (int index = 0; index <= num.length() - 3; ++index) {
            if (num.charAt(index) == sameDigitNumber.charAt(0) &&
                    num.charAt(index + 1) == sameDigitNumber.charAt(1) &&
                    num.charAt(index + 2) == sameDigitNumber.charAt(2)) {
                return true;
            }
        }
        return false;
    }
}
