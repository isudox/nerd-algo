package com.leetcode;

public class Problem2645 {
    public int addMinimum(String word) {
        int n = word.length();
        int ans = word.charAt(0) - word.charAt(n - 1) + 2;
        for (int i = 1; i < n; i++) {
            ans += (word.charAt(i) - word.charAt(i - 1) + 2) % 3;
        }
        return ans;
    }
}
