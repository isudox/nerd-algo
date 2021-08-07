package com.leetcode;

/**
 * 132. Palindrome Partitioning II
 * https://leetcode.com/problems/palindrome-partitioning-ii/
 */
public class Problem132 {
    public int minCut(String s) {
        int[] dp = new int[s.length()];
        boolean[][] memo = new boolean[s.length()][s.length()];
        for (int i = 0; i < s.length(); i++) {
            int cut = i;
            for (int j = 0; j < i + 1; j++) {
                if (s.charAt(i) == s.charAt(j) && (j + 1 > i - 1 || memo[j + 1][i - 1])) {
                    memo[j][i] = true;
                    cut = j == 0 ? 0 : Math.min(cut, dp[j - 1] + 1);
                }
            }
            dp[i] = cut;
        }
        return dp[s.length() - 1];
    }

    public static void main(String[] args) {
        Problem132 sol = new Problem132();
        System.out.println(sol.minCut("aab"));
        System.out.println(sol.minCut("a"));
        System.out.println(sol.minCut("ab"));
    }
}
