package com.leetcode;

public class Problem806 {
    public int[] numberOfLines(int[] widths, String s) {
        int rows = 1, cols = 0;
        for (char c : s.toCharArray()) {
            cols += widths[c - 'a'];
            if (cols > 100) {
                rows++;
                cols = widths[c - 'a'];
            }
        }
        return new int[]{rows, cols};
    }
}
