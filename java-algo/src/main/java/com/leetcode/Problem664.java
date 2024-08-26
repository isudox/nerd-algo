package com.leetcode;

import java.util.*;

/**
 * 664. Strange Printer
 * https://leetcode.com/problems/strange-printer/
 */
public class Problem664 {
    public int strangePrinter(String s) {
        StringBuilder sb = new StringBuilder();
        char pre = '0';
        for (char c : s.toCharArray()) {
            if (c != pre) {
                pre = c;
                sb.append(c);
            }
        }
        s = sb.toString();
        int n = s.length();
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (s.charAt(j) == s.charAt(i)) {
                    dp[i][j] = dp[i][j - 1];
                } else {
                    dp[i][j] = n;
                    for (int k = i; k < j; k++) {
                        dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j]);
                    }
                }
            }
        }
        return dp[0][n - 1];
    }

    public int strangePrinter2(String s) {
        StringBuilder sb = new StringBuilder();
        char pre = '0';
        for (char c : s.toCharArray()) {
            if (c != pre) {
                pre = c;
                sb.append(c);
            }
        }
        s = sb.toString();
        int[][] dp = new int[s.length()][s.length()];
        Map<Character, List<Integer>> posMap = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            List<Integer> list = posMap.getOrDefault(s.charAt(i), new ArrayList<>());
            list.add(i);
            posMap.put(s.charAt(i),list);
        }
        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = i; j < s.length(); j++) {
                if (j == i) {
                    dp[i][j] = 1;
                } else if (s.charAt(j) == s.charAt(i)) {
                    dp[i][j] = dp[i][j - 1];
                } else {
                    dp[i][j] = dp[i][j - 1] + 1;
                    for (int pos : posMap.get(s.charAt(i))) {
                        if (pos < j && pos >= i) {
                            dp[i][j] = Math.min(dp[i][j], dp[i][pos] + dp[pos + 1][j]);
                        }
                    }
                    for (int pos : posMap.get(s.charAt(j))) {
                        if (pos < j && pos >= i) {
                            dp[i][j] = Math.min(dp[i][j], dp[i][pos] + dp[pos + 1][j]);
                        }
                    }
                }
            }
        }
        return dp[0][s.length() - 1];
    }

    public int strangePrinter3(String s) {
        StringBuilder sb = new StringBuilder();
        char pre = '0';
        for (char c : s.toCharArray()) {
            if (c != pre) {
                pre = c;
                sb.append(c);
            }
        }
        s = sb.toString();
        int size = s.length();
        int[][] dp = new int[size][size];
        int[][] posMap = new int[26][101];
        for (int i = size - 1; i >= 0; i--) {
            int[] posList = posMap[s.charAt(i) - 'a'];
            posList[++posList[0]] = i;
            for (int j = i; j < size; j++) {
                if (i == j) {
                    dp[i][j] = 1;
                } else if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = dp[i][j - 1];
                } else {
                    dp[i][j] = Integer.MAX_VALUE;

                    int[] jPosList = posMap[s.charAt(j) - 'a'];

                    for (int k = jPosList[0]; k >= 1; k--) {
                        int pos = jPosList[k];
                        if (j < pos) {
                            break;
                        }
                        dp[i][j] = Math.min(dp[i][j], dp[i][pos - 1] + dp[pos][j]);
                    }
                }
            }
        }
        return dp[0][size - 1];
    }
}
