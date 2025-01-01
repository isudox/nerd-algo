package com.leetcode;

/**
 * 1422. Maximum Score After Splitting a String
 * https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
 */
public class Problem1422 {
    public int maxScore(String s) {
        int ans = 0, cnt0 = 0, cnt1 = 0;
        for (int i = 0; i < s.length(); i++) {
            cnt1 += s.charAt(i) - '0';
        }
        for (int i = 0; i < s.length() - 1; i++) { // split s[:i] and s[i+1:]
            if (s.charAt(i) == '0') {
                cnt0++;
            }
            ans = Math.max(cnt0 + cnt1 - (i - cnt0 + 1), ans);
        }
        return ans;
    }
}
