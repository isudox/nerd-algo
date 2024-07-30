package com.leetcode;

/**
 * 1653. Minimum Deletions to Make String Balanced
 * https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
 */
public class Problem1653 {
    public int minimumDeletions(String s) {
        int ans = s.length(), n = s.length();
        int[] cntA = new int[n + 1], cntB = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            if (s.charAt(i - 1) == 'a') {
                cntA[i] = cntA[i - 1] + 1;
                cntB[i] = cntB[i - 1];
            } else {
                cntA[i] = cntA[i - 1];
                cntB[i] = cntB[i - 1] + 1;
            }
        }
        for (int i = 0; i < n; i++) {
            int tmp = cntB[i] + cntA[n] - Math.max(cntA[i + 1], cntA[i]);
            ans = Math.min(ans, tmp);
        }
        return ans;
    }
}
