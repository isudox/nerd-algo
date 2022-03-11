package com.leetcode;

/**
 * 2049. Count Nodes With the Highest Score
 * https://leetcode.com/problems/count-nodes-with-the-highest-score/
 */
public class Problem2049 {
    public int countHighestScoreNodes(int[] parents) {
        int n = parents.length;
        int[][] graph = new int[n][2];
        for (int i = 1; i < n; i++) {
            if (graph[parents[i]][0] == 0) {
                graph[parents[i]][0] = i;
            } else {
                graph[parents[i]][1] = i;
            }
        }
        int[] memo = new int[n];
        long maxScore = 0;
        int maxCnt = 0;
        for (int i = 0; i < n; i++) {
            long cur = n - count(graph, i, memo);
            cur = cur == 0 ? 1 : cur;
            for (int x : graph[i]) {
                if (x > 0) {
                    cur *= count(graph, x, memo);
                }
            }
            if (cur == maxScore) {
                maxCnt++;
            } else if (cur > maxScore) {
                maxScore = cur;
                maxCnt = 1;
            }
        }
        return maxCnt;
    }

    private int count(int[][] graph, int x, int[] memo) {
        if (memo[x] > 0) {
            return memo[x];
        }
        int ret = 1;
        for (int y : graph[x]) {
            if (y > 0) {
                ret += count(graph, y, memo);
            }
        }
        return memo[x] = ret;
    }
}
