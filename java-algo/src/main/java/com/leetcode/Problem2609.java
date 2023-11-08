package com.leetcode;

/**
 * 2609. Find the Longest Balanced Substring of a Binary String
 * https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string
 */
public class Problem2609 {
    public int findTheLongestBalancedSubstring(String s) {
        int ans = 0;
        int[] cnt = new int[2];
        for (int i = 0; i < s.length(); i++) {
            if (i > 0 && s.charAt(i) == '0' && s.charAt(i - 1) == '1') {
                cnt[0] = 0;
                cnt[1] = 0;
            }
            cnt[s.charAt(i) - '0']++;
            if (cnt[1] <= cnt[0]) {
                ans = Math.max(ans, 2 * cnt[1]);
            } else {
                cnt[0] = 0;
                cnt[1] = 0;
            }
        }
        return ans;
    }
}
