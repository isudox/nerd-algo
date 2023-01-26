package com.leetcode;

/**
 * 1663. Smallest String With A Given Numeric Value
 * https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
 */
public class Problem1663 {
    public String getSmallestString(int n, int k) {
        int countZ = (k - n) / 25;
        int countA = (k - n) % 25 == 0 ? n - countZ : n - countZ - 1;
        StringBuilder sb = new StringBuilder();
        sb.append("a".repeat(countA));
        if ((k - n) % 25 > 0) {
            sb.append((char)('a' + (k - n) % 25));
        }
        sb.append("z".repeat(countZ));
        return sb.toString();
    }
}
