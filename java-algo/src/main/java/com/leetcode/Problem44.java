package com.leetcode;

/**
 * 44. Wildcard Matching
 * https://leetcode.com/problems/wildcard-matching/
 */
public class Problem44 {

    /**
     * DP.
     * Time complexity: O(mn)
     * Space complexity: O(mn)
     */
    public boolean isMatch(String s, String p) {
        int lenS = s.length(), lenP = p.length();
        // dp[i][j] means s[0, i-1] matches p[0, j-1]
        boolean[][] dp = new boolean[lenS + 1][lenP + 1];
        dp[0][0] = true;
        for (int i = 1; i <= lenP; i++) {
            if (p.charAt(i - 1) == '*') {
                dp[0][i] = true;
            } else {
                break;
            }
        }
        for (int i = 1; i <= lenS; i++) {
            dp[i][0] = false;
        }
        for (int i = 1; i <= lenS; i++) {
            for (int j = 1; j <= lenP; j++) {
                char c = p.charAt(j - 1);
                if (c == '*') {
                    // * matches no characters or matches one more characters
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                } else if (c == '?' || c == s.charAt(i - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }
        return dp[lenS][lenP];
    }
}
