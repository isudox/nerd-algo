package com.leetcode;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * 2707. Extra Characters in a String
 * https://leetcode.com/problems/extra-characters-in-a-string/
 */
public class Problem2707 {
    public int minExtraChar(String s, String[] dictionary) {
        int n = s.length();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, n + 1);
        dp[0] = 0;
        Set<String> dicts = new HashSet<>(Arrays.asList(dictionary));
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1] + 1;
            for (int j = i - 1; j >= 0; j--) {
                if (dicts.contains(s.substring(j, i))) {
                    dp[i] = Math.min(dp[i], dp[j]);
                }
            }
        }
        return dp[n];
    }
}
