package com.leetcode;

import java.util.Arrays;

/**
 * 2976. Minimum Cost to Convert String I
 * https://leetcode.com/problems/minimum-cost-to-convert-string-i/
 */
public class Problem2976 {
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        long ans = 0;
        long[][] minCost = new long[26][26];
        for (long[] row : minCost) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        for (int i = 0; i < original.length; ++i) {
            int startChar = original[i] - 'a';
            int endChar = changed[i] - 'a';
            minCost[startChar][endChar] = Math.min(minCost[startChar][endChar], cost[i]);
        }
        for (int k = 0; k < 26; ++k) {
            for (int i = 0; i < 26; ++i) {
                for (int j = 0; j < 26; ++j) {
                    minCost[i][j] = Math.min(minCost[i][j], minCost[i][k] + minCost[k][j]);
                }
            }
        }
        for (int i = 0; i < source.length(); ++i) {
            if (source.charAt(i) == target.charAt(i)) {
                continue;
            }
            int sourceChar = source.charAt(i) - 'a';
            int targetChar = target.charAt(i) - 'a';
            if (minCost[sourceChar][targetChar] >= Integer.MAX_VALUE) {
                return -1;
            }
            ans += minCost[sourceChar][targetChar];
        }
        return ans;
    }
}
