package com.leetcode;

public class Problem1422 {
    public int maxScore(String s) {
        int n = s.length();
        int[] cnt0 = new int[n + 1];
        int total0 = 0;
        for (int i = 1; i <= n; i++) {
            cnt0[i] = cnt0[i - 1];
            if (s.charAt(i - 1) == '0') {
                cnt0[i]++;
                total0++;
            }
        }
        int ans = 0;
        for (int i = 0; i < n - 1; i++) {
            int cur = cnt0[i + 1] + (n - 1 - i) - (total0 - cnt0[i + 1]);
            ans = Math.max(ans, cur);
        }
        return ans;
    }
}
