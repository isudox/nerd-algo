package com.leetcode;

/**
 * 1583. Count Unhappy Friends
 * https://leetcode.com/problems/count-unhappy-friends/
 */
public class Problem1583 {
    public int unhappyFriends(int n, int[][] preferences, int[][] pairs) {
        int[][] scores = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                int k = 0;
                while (preferences[i][k] != j)
                    k++;
                scores[i][j] = k;
            }
        }
        int[] friends = new int[n];
        for (int[] pair : pairs) {
            friends[pair[0]] = pair[1];
            friends[pair[1]] = pair[0];
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int j = friends[i];
            for (int k : preferences[i]) {
                if (k == j) break;
                int score1 = scores[k][i];
                int score2 = scores[k][friends[k]];
                if (score1 < score2) {
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
}
