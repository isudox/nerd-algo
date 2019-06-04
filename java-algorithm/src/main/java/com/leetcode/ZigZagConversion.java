package com.leetcode;

/**
 * 6. ZigZag Conversion
 * https://leetcode.com/problems/zigzag-conversion/
 * <p>
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
 * of rows like this:
 * (you may want to display this pattern in a fixed font for better legibility)
 * <p>
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * And then read line by line: "PAHNAPLSIIGYIR"
 * <p>
 * Write the code that will take a string and make this conversion given
 * a number of rows:
 * <p>
 * string convert(string s, int numRows);
 * Example 1:
 * <p>
 * Input: s = "PAYPALISHIRING", numRows = 3
 * Output: "PAHNAPLSIIGYIR"
 * Example 2:
 * <p>
 * Input: s = "PAYPALISHIRING", numRows = 4
 * Output: "PINALSIGYAHRPI"
 * Explanation:
 * <p>
 * P     I    N
 * A   L S  I G
 * Y A   H R
 * P     I
 */
public class ZigZagConversion {

    public String convert(String s, int numRows) {
        int len = s.length();
        if (len <= 2 || numRows == 1) {
            return s;
        }
        StringBuilder result = new StringBuilder();
        for (int currRow = 0; currRow < numRows; currRow++) {
            for (int currIndex = currRow; currIndex < len; currIndex += 2 * (numRows - 1)) {
                result.append(s.charAt(currIndex));
                if (currRow != 0 && currRow != numRows - 1 && currIndex + 2 * (numRows - currRow - 1) < len) {
                    result.append(s.charAt(currIndex + 2 * (numRows - currRow - 1)));
                }
            }
        }
        return result.toString();
    }
}