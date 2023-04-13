package com.leetcode;

/**
 * 1374. Generate a String With Characters That Have Odd Counts
 * https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
 */
public class Problem1374 {
    public String generateTheString(int n) {
        if (n % 2 == 0) return generateTheString(n - 1) + "b";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) sb.append("a");
        return sb.toString();
    }
}
